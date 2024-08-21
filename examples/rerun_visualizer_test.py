import pinocchio as pin
from pinocchio.visualize import BaseVisualizer

import os
import warnings
import numpy as np
from typing import List

try:
    import rerun as rr
    import rerun.blueprint as rrb
except ImportError:
    import_rerun_succeed = False
else:
    import_rerun_succeed = True

# DaeMeshGeometry
import xml.etree.ElementTree as Et
import base64

from typing import Optional, Any, Dict, Union, Set
from uuid import uuid4
from warnings import warn
from dataclasses import dataclass

try:
    import hppfcl
    WITH_HPP_FCL_BINDINGS = True
except ImportError:
    WITH_HPP_FCL_BINDINGS = False

@dataclass
class MeshDescription:
    vertices: list[list[float]]
    normals: list[list[float]]
    faceTriangles: list[list[int]]
    colors: list[int]

#################################################

DEFAULT_COLOR_PROFILES = {
    "gray": ([0.98, 0.98, 0.98], [0.8, 0.8, 0.8]),
    "white": ([1.0, 1.0, 1.0], [1.0, 1.0, 1.0]),
}
COLOR_PRESETS = DEFAULT_COLOR_PROFILES.copy()

FRAME_AXIS_POSITIONS = (
    np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]])
    .astype(np.float32)
    .T
)
FRAME_AXIS_COLORS = (
    np.array([[1, 0, 0], [1, 0.6, 0], [0, 1, 0], [0.6, 1, 0], [0, 0, 1], [0, 0.6, 1]])
    .astype(np.float32)
    .T
)

def getColor(color):
    assert color is not None
    color = np.asarray(color)
    assert color.shape == (3,)
    return color.clip(0.0, 1.0)

def hasMeshFileInfo(geometry_object):
    """Check whether the geometry object contains a Mesh supported by MeshCat"""
    if geometry_object.meshPath == "":
        return False

    _, file_extension = os.path.splitext(geometry_object.meshPath)
    if file_extension.lower() in [".dae", ".obj", ".stl"]:
        return True

    return False

if import_rerun_succeed:
    class DaeMeshGeometry():
        def __init__(self, dae_path: str, cache: Optional[Set[str]] = None) -> None:
            # Attributes to be specified by the user
            self.path = None
            self.material = None

            # Raw file content
            dae_dir = os.path.dirname(dae_path)
            with open(dae_path, "r") as text_file:
                self.dae_raw = text_file.read()

            # Parse the image resource in Collada file
            img_resource_paths = []
            img_lib_element = Et.parse(dae_path).find(
                "{http://www.collada.org/2005/11/COLLADASchema}library_images"
            )
            if img_lib_element:
                img_resource_paths = [
                    e.text for e in img_lib_element.iter() if e.tag.count("init_from")
                ]

            # Convert textures to data URL for Three.js ColladaLoader to load them
            self.img_resources = {}
            for img_path in img_resource_paths:
                # Return empty string if already in cache
                if cache is not None:
                    if img_path in cache:
                        self.img_resources[img_path] = ""
                        continue
                    cache.add(img_path)

                # Encode texture in base64
                img_path_abs = img_path
                if not os.path.isabs(img_path):
                    img_path_abs = os.path.normpath(os.path.join(dae_dir, img_path_abs))
                if not os.path.isfile(img_path_abs):
                    raise UserWarning(f"Texture '{img_path}' not found.")
                with open(img_path_abs, "rb") as img_file:
                    img_data = base64.b64encode(img_file.read())
                img_uri = f"data:image/png;base64,{img_data.decode('utf-8')}"
                self.img_resources[img_path] = img_uri

        def lower(self) -> Dict[str, Any]:
            """Pack data into a dictionary containing the information to 
            be sent to server.
            """
            data = {
                "type": "set_object",
                "path": self.path.lower() if self.path is not None else "",
                "object": {
                    "metadata": {"version": 4.5, "type": "Object"},
                    "geometries": [],
                    "materials": [],
                    "object": {
                        "uuid": self.uuid,
                        "type": "_meshfile_object",
                        "format": "dae",
                        "data": self.dae_raw,
                        "resources": self.img_resources,
                    },
                },
            }
            if self.material is not None:
                self.material.lower_in_object(data)
            return data

if (
    WITH_HPP_FCL_BINDINGS
    and tuple(map(int, hppfcl.__version__.split("."))) >= (3, 0, 0)
    and hppfcl.WITH_OCTOMAP
):
    def loadOctree(octree: hppfcl.OcTree):
        boxes = octree.toBoxes()

        if len(boxes) == 0:
            return
        bs = boxes[0][3] / 2.0
        num_boxes = len(boxes)

        box_corners = np.array(
            [
                [bs, bs, bs],
                [bs, bs, -bs],
                [bs, -bs, bs],
                [bs, -bs, -bs],
                [-bs, bs, bs],
                [-bs, bs, -bs],
                [-bs, -bs, bs],
                [-bs, -bs, -bs],
            ]
        )

        all_points = np.empty((8 * num_boxes, 3))
        all_faces = np.empty((12 * num_boxes, 3), dtype=int)
        face_id = 0
        for box_id, box_properties in enumerate(boxes):
            box_center = box_properties[:3]

            corners = box_corners + box_center
            point_range = range(box_id * 8, (box_id + 1) * 8)
            all_points[point_range, :] = corners

            A = box_id * 8
            B = A + 1
            C = B + 1
            D = C + 1
            E = D + 1
            F = E + 1
            G = F + 1
            H = G + 1

            all_faces[face_id] = np.array([C, D, B])
            all_faces[face_id + 1] = np.array([B, A, C])
            all_faces[face_id + 2] = np.array([A, B, F])
            all_faces[face_id + 3] = np.array([F, E, A])
            all_faces[face_id + 4] = np.array([E, F, H])
            all_faces[face_id + 5] = np.array([H, G, E])
            all_faces[face_id + 6] = np.array([G, H, D])
            all_faces[face_id + 7] = np.array([D, C, G])
            # # top
            all_faces[face_id + 8] = np.array([A, E, G])
            all_faces[face_id + 9] = np.array([G, C, A])
            # # bottom
            all_faces[face_id + 10] = np.array([B, H, F])
            all_faces[face_id + 11] = np.array([H, B, D])

            face_id += 12

        colors = np.empty((all_points.shape[0], 3))
        colors[:] = np.ones(3)

        # indices = []
        # for i in range(numTris):
        #     indices.append([mesh.faceTriangles[i][0], mesh.faceTriangles[i][1], mesh.faceTriangles[i][2]])

        rrMesh = rr.archetypes.Mesh3D(
            vertex_positions=all_points,
            # triangle_indices=indices,
            vertex_normals=all_faces,
            vertex_colors=colors,
        )

        return rrMesh
else:
    def loadOctree(octree):
        raise NotImplementedError("loadOctree need hppfcl with octomap support")


if WITH_HPP_FCL_BINDINGS:

    def loadMesh(mesh):
        if isinstance(mesh, (hppfcl.HeightFieldOBBRSS, hppfcl.HeightFieldAABB)):
            heights = mesh.getHeights()
            x_grid = mesh.getXGrid()
            y_grid = mesh.getYGrid()
            min_height = mesh.getMinHeight()

            X, Y = np.meshgrid(x_grid, y_grid)

            nx = len(x_grid) - 1
            ny = len(y_grid) - 1

            num_cells = (nx) * (ny) * 2 + (nx + ny) * 4 + 2

            num_vertices = X.size
            num_tris = num_cells

            faces = np.empty((num_tris, 3), dtype=int)
            vertices = np.vstack(
                (
                    np.stack(
                        (
                            X.reshape(num_vertices),
                            Y.reshape(num_vertices),
                            heights.reshape(num_vertices),
                        ),
                        axis=1,
                    ),
                    np.stack(
                        (
                            X.reshape(num_vertices),
                            Y.reshape(num_vertices),
                            np.full(num_vertices, min_height),
                        ),
                        axis=1,
                    ),
                )
            )

            face_id = 0
            for y_id in range(ny):
                for x_id in range(nx):
                    p0 = x_id + y_id * (nx + 1)
                    p1 = p0 + 1
                    p2 = p1 + nx + 1
                    p3 = p2 - 1

                    faces[face_id] = np.array([p0, p3, p1])
                    face_id += 1
                    faces[face_id] = np.array([p3, p2, p1])
                    face_id += 1

                    if y_id == 0:
                        p0_low = p0 + num_vertices
                        p1_low = p1 + num_vertices

                        faces[face_id] = np.array([p0, p1_low, p0_low])
                        face_id += 1
                        faces[face_id] = np.array([p0, p1, p1_low])
                        face_id += 1

                    if y_id == ny - 1:
                        p2_low = p2 + num_vertices
                        p3_low = p3 + num_vertices

                        faces[face_id] = np.array([p3, p3_low, p2_low])
                        face_id += 1
                        faces[face_id] = np.array([p3, p2_low, p2])
                        face_id += 1

                    if x_id == 0:
                        p0_low = p0 + num_vertices
                        p3_low = p3 + num_vertices

                        faces[face_id] = np.array([p0, p3_low, p3])
                        face_id += 1
                        faces[face_id] = np.array([p0, p0_low, p3_low])
                        face_id += 1

                    if x_id == nx - 1:
                        p1_low = p1 + num_vertices
                        p2_low = p2 + num_vertices

                        faces[face_id] = np.array([p1, p2_low, p2])
                        face_id += 1
                        faces[face_id] = np.array([p1, p1_low, p2_low])
                        face_id += 1

            # Last face
            p0 = num_vertices
            p1 = p0 + nx
            p2 = 2 * num_vertices - 1
            p3 = p2 - nx

            faces[face_id] = np.array([p0, p1, p2])
            face_id += 1
            faces[face_id] = np.array([p0, p2, p3])
            face_id += 1

        elif isinstance(mesh, (hppfcl.Convex, hppfcl.BVHModelBase)):
            if isinstance(mesh, hppfcl.BVHModelBase):
                num_vertices = mesh.num_vertices
                num_tris = mesh.num_tris

                call_triangles = mesh.tri_indices
                call_vertices = mesh.vertices

            elif isinstance(mesh, hppfcl.Convex):
                num_vertices = mesh.num_points
                num_tris = mesh.num_polygons

                call_triangles = mesh.polygons
                call_vertices = mesh.points

            faces = np.empty((num_tris, 3), dtype=int)
            for k in range(num_tris):
                tri = call_triangles(k)
                faces[k] = [tri[i] for i in range(3)]

            vertices = call_vertices()
            vertices = vertices.astype(np.float32)

        if num_tris > 0:
            rrMesh = rr.archetypes.Mesh3D(
                vertex_positions=vertices,
                vertex_normals=faces,
            )
        else:
            rrMesh = rr.archetypes.Points3D(
                positions=vertices,
                colors=np.repeat(np.ones((3, 1)), num_vertices, axis=1),
                radii=np.ones(num_vertices) * 0.002,
            )

        return mesh
else:

    def loadMesh(mesh):
        raise NotImplementedError("loadMesh need hppfcl")

    

##########################################

def getEntityPath(obj: hppfcl.GeometryObject, prefix: str) -> str:
    return f"{prefix}/{obj.name}"

# def meshDescriptionToRerun(mesh: MeshDescription) -> rr.archetypes.Mesh3D:
#     numTris = mesh.faceTriangles.size

#     indices = []
#     for i in range(numTris):
#         indices.append([mesh.faceTriangles[i][0], mesh.faceTriangles[i][1], mesh.faceTriangles[i][2]])

#     rrMesh = rr.archetypes.Mesh3D(
#         vertex_positions=mesh.vertices,
#         triangle_indices=indices,
#         vertex_normals=mesh.normals,
#         vertex_colors=mesh.colors,
#     )
#     return rrMesh

class RerunVisualizer(BaseVisualizer):
    def __init__(
        self,
        model=pin.Model(),
        collision_model=None,
        visual_model=None,
        copy_models=False,
        data=None,
        collision_data=None,
        visual_data=None,
        nu=None,
        notebook_embed=False,
        name="Pinocchio Viewer",
    ):
        if not import_rerun_succeed:
            msg = ("Error while importing rerun.\n"
                    "Check whether rerun is correctly installed (cf rerun.io).")
            raise ImportError(msg)

        super(RerunVisualizer, self).__init__(
            model,
            collision_model,
            visual_model,
            copy_models,
            data,
            collision_data,
            visual_data,
        )
        self.recording_id = uuid4()
        rr.init(
            application_id=name,
            recording_id=self.recording_id,
            spawn=True,
        )
        rr.set_time_seconds("stable_time", 0.0)
        self.init_bp_dict()
        self.set_blueprint()
        self.viewer_prefix = "/viewer"
    
    def loadMeshFromFile(self, geometry_object):
        # Mesh path is empty if Pinocchio is built without HPP-FCL bindings
        if geometry_object.meshPath == "":
            msg = "Display of geometric primitives is supported only if pinocchio is build with HPP-FCL bindings."
            warnings.warn(msg, category=UserWarning, stacklevel=2)
            return None

        # Get file type from filename extension.
        _, file_extension = os.path.splitext(geometry_object.meshPath)
        if file_extension.lower() == ".dae":
            obj = DaeMeshGeometry(geometry_object.meshPath)
        elif file_extension.lower() == ".obj":
            obj = mg.ObjMeshGeometry.from_file(geometry_object.meshPath)
        elif file_extension.lower() == ".stl":
            obj = mg.StlMeshGeometry.from_file(geometry_object.meshPath)
        else:
            msg = "Unknown mesh file format: {}.".format(geometry_object.meshPath)
            warnings.warn(msg, category=UserWarning, stacklevel=2)
            obj = None

        return obj

    # def loadPinocchioModel(self, geomModel):
    #     geomObjects = geomModel.geometryObjects
    #     for geom in geomObjects:
    #         self.loadPinocchioGeometry(geom)
        
    # def loadPinocchioGeometry(self, obj: hppfcl.GeometryObject):
    #     geom = obj.geometry
    #     objType = geom.getObjectType()
    #     nodeType = geom.getNodeType()

    #     match objType:
    #         case hppfcl.OT_BVH:
    #             match nodeType:
    #                 case hppfcl.BV_AABB:
    #                     pass
    #                 case hppfcl.BV_OBB:
    #                     pass
    #                 case hppfcl.BV_RSS:
    #                     pass
    #                 case hppfcl.BV_kIOS:
    #                     pass
    #                 case hppfcl.BV_OBBRSS:
    #                     pass
    #                 case hppfcl.BV_KDOP16:
    #                     pass
    #                 case hppfcl.BV_KDOP18:
    #                     pass
    #                 case hppfcl.BV_KDOP24:
    #                     rrmesh = loadMesh(obj.meshPath, float(obj.meshScale), obj.meshColor)
                          # rrMesh = meshDescriptionToRerun(meshDesc)
    #                     rr.log_timeless(getEntityPath(obj, self.viewer_prefix), rrMesh)
    #                 case _:
    #                     warn(f"Unknown or unsupported HPP-FCL node type {nodeType}")
    #         case _:
    #             warn(f"Unknown or unsupported HPP-FCL object type {objType}")

    # def loadViewerModel(self):
    #     self.loadPinocchioModel(self.visual_model)
    #     self.m_initialized = True

    def display(self, q):
        assert len(q) == self.model.nq
        rr.log()

    def init_bp_dict(self):
        ## Define BLUEPRINTS 
        nq, nv = self.model.nq, self.model.nv
        if self.nu is None: 
            nu = nv - 6
        self.blueprints = {
            "viewer_only": rrb.Blueprint(
                rrb.Spatial3DView(
                    name="Viewer",
                    origin=self.viewer_prefix,
                ),
            ),
            "viewer_configuration": rrb.Blueprint(
                rrb.Horizontal(
                    rrb.Spatial3DView(
                        name="Viewer",
                        origin=self.viewer_prefix,
                    ),
                    rrb.Vertical(
                        contents=[
                            rrb.TimeSeriesView(
                                name=f"q{i}",
                                origin=f"/configurations/q{i}",
                            )
                            for i in range(nq)
                        ],
                    )
                ),
                rrb.SelectionPanel(state="collapsed"),
                rrb.TimePanel(state="collapsed"),
            ),
        }
        

    def set_blueprint(self, name="", blueprint=None):
        if name == "" and blueprint is None:
            name = "viewer_only"
        if blueprint is None:
            blueprint = self.blueprints[name]

    def init_viewer(self):
        if self.viewer is None:
            self.viewer = rr.init(
                "rerun_example_external_data_loader_urdf",
                spawn=True,
                default_blueprint=self.blueprint,
            )

    def load_default(self):
        if self.blueprint is None:
            print("No blueprint provided, using default.")


