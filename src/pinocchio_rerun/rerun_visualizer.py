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
import hppfcl

from typing import Optional, Any, Dict, Union, Set
from uuid import uuid4
from warnings import warn
from dataclasses import dataclass
import pyassimp
from pyassimp.postprocess import (
    aiProcess_CalcTangentSpace,
    aiProcess_Triangulate,
    aiProcess_GenSmoothNormals,
    aiProcess_SortByPType,
    aiProcess_GenUVCoords,
    aiProcess_OptimizeMeshes,
    aiProcess_RemoveComponent,
    aiProcess_FindDegenerates,
    aiProcess_ImproveCacheLocality,
)

@dataclass
class MeshDescription:
    name: str
    vertices: list[list[float]]
    normals: list[list[float]]
    faceTriangles: list[list[int]]
    colors: list[int]

def color_float_to_int(f: list[float]) -> int:
    return(np.array(f*255, dtype=int))

COLORS_PREDEFINED = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "yellow": [255, 255, 0],
    "cyan": [0, 255, 255],
    "magenta": [255, 0, 255],
    "white": [255, 255, 255],
    "black": [0, 0, 0],
}

# def matrix4x4_to_np(m):
#     return np.array(
#         [
#             [m.a1, m.a2, m.a3, m.a4],
#             [m.b1, m.b2, m.b3, m.b4],
#             [m.c1, m.c2, m.c3, m.c4],
#             [m.d1, m.d2, m.d3, m.d4],
#         ]
#     )

# def buildMeshLoop(scene, node, vtxOffset, scale, color, mesh):
#     if not node:
#         return 0
    
#     if node[0].mTransformation:
#         tr = matrix4x4_to_np(node[0].mTransformation)
#     parent = node[0].mParent

#     while(parent):
#         if parent[0].mParent:
#             tr = matrix4x4_to_np(parent[0].mTransformation) * tr
#         parent = parent[0].mParent

#     nbVtx = 0
#     for i in range(node[0].mNumMeshes):
#         meshIdx = node[0].mMeshes[i]
#         breakpoint()
#         inMesh = scene.mMeshes[meshIdx]
#         for vId in range(inMesh[0].mNumVertices):
#             pos = inMesh[0].mVertices[vId]
#             pos *= tr
#             p = pos.x
#             mesh.vertices.append(np.diag(scale) * p)
#             c = []
#             for cId in range(4):
#                 c.append(int(color_float_to_int(color[cId])))
#             # c2 = pastel_rgba(c)
#             c2 = c
#             mesh.colors.append(c2)
        
#             if inMesh[0].mNormals:
#                 n = inMesh[0].mNormals[vId]
#                 n = n.x
#                 mesh.normals.append(n)
            
#         for fId in range(inMesh[0].mNumFaces):
#             face = inMesh[0].mFaces[fId]
#             faceIdx = face[0].mIndices
#             mesh.faceTriangles.append(np.array(faceIdx) + vtxOffset)

#         nbVtx += inMesh[0].mNumVertices

#     for cIdx in range(node[0].mNumChildren):
#         nb, mesh = buildMeshLoop(scene, node[0].mChildren[cIdx], nbVtx, scale, color, mesh)
#         nbVtx += nb

#     return nbVtx, mesh

# def buildMesh(scene, vtxOffset, scale, color):
#     mesh = MeshDescription([], [], [], [])
#     _, mesh = buildMeshLoop(scene, scene.mRootNode, vtxOffset, scale, color, mesh)
#     return mesh

def loadMesh(meshPath: str, default_color) -> MeshDescription:
    load_options = (
        aiProcess_CalcTangentSpace
        | aiProcess_Triangulate
        | aiProcess_GenSmoothNormals
        | aiProcess_SortByPType
        | aiProcess_GenUVCoords
        | aiProcess_OptimizeMeshes
        | aiProcess_RemoveComponent
        | aiProcess_FindDegenerates
        | aiProcess_ImproveCacheLocality
    )

    meshDesc = MeshDescription("", [], [], [], [])

    with pyassimp.load(filename=meshPath, processing=load_options) as scene:
        # aiScene = scene

        assert len(scene.meshes) == 1
        mesh = scene.meshes[0]
        meshDesc.name = mesh.name
        meshDesc.vertices = mesh.vertices.tolist()
        meshDesc.normals = mesh.normals.tolist()
        meshDesc.faceTriangles = mesh.faces.tolist()
        if len(mesh.colors) != 0:
            meshDesc.colors = np.array(mesh.colors[0]*255, dtype=int)[:, :3].tolist()
        else:
            meshDesc.colors = np.tile(default_color, (len(mesh.vertices), 1)).tolist()
    
    return meshDesc


def getEntityPath(obj, prefix: str) -> str:
    return f"{prefix}/{obj.name}"


def meshDescriptionToRerun(mesh: MeshDescription) -> rr.archetypes.Mesh3D:
    numTris = len(mesh.faceTriangles)

    indices = []
    for i in range(numTris):
        indices.append(
            [
                mesh.faceTriangles[i][0],
                mesh.faceTriangles[i][1],
                mesh.faceTriangles[i][2],
            ]
        )

    rrMesh = rr.archetypes.Mesh3D(
        vertex_positions=mesh.vertices,
        triangle_indices=indices,
        vertex_normals=mesh.normals,
        vertex_colors=mesh.colors,
    )
    return rrMesh


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
        self.nu = nu
        self.notebook_embed = notebook_embed
        self.name = name
        self.viewer_prefix = '/viewer'
        self.robot_prefix = f"{self.viewer_prefix}/{model.name}"
        self.visual_prefix = f"{self.robot_prefix}/visual"
        self.collision_prefix = f"{self.robot_prefix}/collision"
        self.inertias_prefix = f"{self.robot_prefix}/inertias"
        self.com_prefix = f"{self.robot_prefix}/center-of-mass"
        self.objects_prefix = f"{self.viewer_prefix}/objects"
        if not import_rerun_succeed:
            msg = (
                "Error while importing rerun.\n"
                "Check whether rerun is correctly installed (cf rerun.io)."
            )
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
            application_id=self.name,
            recording_id=self.recording_id,
            spawn=True,
        )
        if self.notebook_embed:
            rr.notebook_show()
        rr.set_time_seconds("stable_time", 0.0)
        self.init_bp_dict()
        self.set_blueprint()

        self.inertias_active = False

    def loadPinocchioModel(self, geomModel):
        geomObjects = geomModel.geometryObjects
        for geom in geomObjects:
            self.loadPinocchioGeometry(geom)

    def loadPinocchioGeometry(self, obj):
        geom = obj.geometry
        objType = geom.getObjectType()
        nodeType = geom.getNodeType()
        match objType:
            case hppfcl.OT_BVH:
                match nodeType:
                    case hppfcl.BV_AABB:
                        pass
                    case hppfcl.BV_OBB:
                        pass
                    case hppfcl.BV_RSS:
                        pass
                    case hppfcl.BV_kIOS:
                        pass
                    case hppfcl.BV_OBBRSS:
                        meshDesc = loadMesh(
                            obj.meshPath,
                            color_float_to_int(obj.meshColor),
                        )
                        rrMesh = meshDescriptionToRerun(meshDesc)
                        # print(obj.meshPath)
                        # rrMesh = rr.Asset3D(path=obj.meshPath)
                        path = getEntityPath(obj, self.visual_prefix)
                        rr.log(path, rrMesh)
                    case hppfcl.BV_KDOP16:
                        pass
                    case hppfcl.BV_KDOP18:
                        pass
                    case hppfcl.BV_KDOP24:
                        meshDesc = loadMesh(
                            obj.meshPath,
                            color_float_to_int(obj.meshColor),
                        )
                        rrMesh = meshDescriptionToRerun(meshDesc)
                        # rrMesh = rr.Asset3D(path=obj.meshPath)
                        rr.log_timeless(getEntityPath(obj, self.visual_prefix), rrMesh)
                    case _:
                        warn(f"Unknown or unsupported HPP-FCL node type {nodeType}")
            case _:
                warn(f"Unknown or unsupported HPP-FCL object type {objType}")

    def loadViewerModel(self):
        self.loadPinocchioModel(self.visual_model)
        self.display(pin.neutral(self.model))
        self.m_initialized = True

    def display(self, q):
        assert len(q) == self.model.nq

        pin.forwardKinematics(self.model, self.data, q)
        pin.updateGeometryPlacements(self.model, self.data, self.visual_model, self.visual_data)

        geomObjects = self.visual_model.geometryObjects
        ngeoms = len(geomObjects)

        for i in range(ngeoms):
            gobj = geomObjects[i]
            M = self.visual_data.oMg[self.visual_model.getGeometryId(gobj.name)]

            path = getEntityPath(gobj, self.visual_prefix)
            xyzquat = pin.SE3ToXYZQUAT(M)
            tr = rr.Transform3D(
                translation=rr.datatypes.Vec3D(xyz=xyzquat[0:3]),
                rotation=rr.datatypes.Quaternion(xyzw=xyzquat[3:7]),
            )
            rr.log(path, tr)
        
        if self.inertias_active:
            self.visualizeInertias()

    def init_bp_dict(self):
        ## Define BLUEPRINTS
        nq, nv = self.model.nq, self.model.nv
        if self.nu is None:
            nu = nv - 6
        self.blueprints = {
            "viewer_only": rrb.Blueprint(
                rrb.Horizontal(
                    rrb.Spatial3DView(
                        name="Viewer",
                        origin=self.viewer_prefix,
                    ),
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
                    ),
                ),
                rrb.SelectionPanel(state="collapsed"),
                rrb.TimePanel(state="collapsed"),
            ),
        }

    def set_blueprint(self, name="", blueprint=None):
        if blueprint is None:
            if name == "":
                name = "viewer_only"
            blueprint = self.blueprints[name]
        rr.send_blueprint(blueprint)

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

    def addBox(self, name, size, color="red", category="objects"):
        if not (len(size) == 3 or len(size) == 1):
            raise AttributeError("size must be a scalar or a 3D vector")
        if not isinstance(color, str):
            if not isinstance(color, list):
                raise AttributeError("color must be a string or a list of 3 to 4 integers")
            elif not (len(color)==3 or len(color)==4):
                raise AttributeError("color list must have 3 or 4 elements")
        if len(size) == 1:
            size = [size, size, size]
        # rrSize = rr.datatypes.Vec3D(xyz=size)
        if isinstance(color, str):
            if color not in COLORS_PREDEFINED.keys():
                raise AttributeError(f"color must be one of {COLORS_PREDEFINED.keys()} or a list of rgb values")
            color = COLORS_PREDEFINED[color]
        box = rr.archetypes.Boxes3D(sizes=[size], colors=[color], fill_mode="solid")

        match category:
            case "objects":
                prefix = self.objects_prefix
            case "collision":
                prefix = self.collision_prefix
            case "visual":
                prefix = self.visual_prefix
            case "inertias":
                prefix = self.inertias_prefix
            case "com":
                prefix = self.com_prefix
            case _:
                raise AttributeError("category must be one of 'objects', 'collision', 'visual', 'inertias', 'com'")
        rr.log(f"{prefix}/{name}", box)

    def addEllipsoid(self, name, radii, color="green", category="objects"):
        if not (len(radii) == 3 or len(radii) == 1):
            raise AttributeError("size must be a scalar or a 3D vector")
        if not isinstance(color, str):
            if not isinstance(color, list):
                raise AttributeError("color must be a string or a list of 3 to 4 integers")
            elif not (len(color)==3 or len(color)==4):
                raise AttributeError("color list must have 3 or 4 elements")
        if len(radii) == 1:
            radii = [radii, radii, radii]
        if isinstance(color, str):
            if color not in COLORS_PREDEFINED.keys():
                raise AttributeError(f"color must be one of {COLORS_PREDEFINED.keys()} or a list of rgb values")
            color = COLORS_PREDEFINED[color]
        ellipsoids = rr.archetypes.Ellipsoids3D(half_sizes=[radii], colors=[color], fill_mode="solid")

        match category:
            case "objects":
                prefix = self.objects_prefix
            case "collision":
                prefix = self.collision_prefix
            case "visual":
                prefix = self.visual_prefix
            case "inertias":
                prefix = self.inertias_prefix
            case "com":
                prefix = self.com_prefix
            case _:
                raise AttributeError("category must be one of 'objects', 'collision', 'visual', 'inertias', 'com'")
        rr.log(f"{prefix}/{name}", ellipsoids)

    def addSphere(self, name, radius, color="blue", category="objects"):
        self.addEllipsoid(name, [radius], color, category)

    def set_pose(self, name, pose, category="objects"):
        if isinstance(pose, pin.SE3):
            pose = pin.SE3ToXYZQUAT(pose)
        else:
            assert len(pose) == 7
        tr = rr.Transform3D(
            translation=rr.datatypes.Vec3D(xyz=pose[0:3]),
            rotation=rr.datatypes.Quaternion(xyzw=pose[3:7]),
        )
        match category:
            case "objects":
                prefix = self.objects_prefix
            case "collision":
                prefix = self.collision_prefix
            case "visual":
                prefix = self.visual_prefix
            case "inertias":
                prefix = self.inertias_prefix
            case "com":
                prefix = self.com_prefix
            case _:
                raise AttributeError("category must be one of 'objects', 'collision', 'visual', 'inertias', 'com'")
        rr.log(f"{prefix}/{name}", tr)

    def activateInertias(self, scale=1.0, scale_com=1.0):
        self.inertias_active = True
        self.scale = 1.0
        self.scale_com = 1.0

    def deactivateInertias(self):
        self.inertias_active = False
        # TODO remove all inertias from viewer

    def visualizeInertias(self, color="green", scale=None, scale_com=None):
        if scale is None:
            scale = self.scale
        if scale_com is None:
            scale_com = self.scale_com
        if not isinstance(color, str):
            if not isinstance(color, list):
                raise AttributeError("color must be a string or a list of 3 to 4 integers")
            elif not (len(color)==3 or len(color)==4):
                raise AttributeError("color list must have 3 or 4 elements")
        if isinstance(color, str):
            if color not in COLORS_PREDEFINED.keys():
                raise AttributeError(f"color must be one of {COLORS_PREDEFINED.keys()} or a list of rgb values")
            color = COLORS_PREDEFINED[color]

        for idJoint in range(self.model.njoints):
            # get inertia tensor
            I = self.model.inertias[idJoint]
            if I.mass == 0:
                continue

            # get box lengthes
            ## diagonalize inertia tensor
            eigenvalues, eigenvectors = np.linalg.eigh(I.inertia)
            I_xx_p, I_yy_p, I_zz_p = eigenvalues

            ## compute box lengthes
            d = np.sqrt(6 * (I_xx_p + I_yy_p - I_zz_p) / (I.mass)) * scale
            w = np.sqrt(6 * (I_xx_p - I_yy_p + I_zz_p) / (I.mass)) * scale
            h = np.sqrt(6 * (-I_xx_p + I_yy_p + I_zz_p) / (I.mass)) * scale

            # get tf between frame link and CoM link
            oMi = self.data.oMi[idJoint]

            iMcom = pin.SE3.Identity()
            iMcom.translation = I.lever
            
            comMinertia = pin.SE3.Identity()
            comMinertia.rotation = eigenvectors

            oMcom = oMi * iMcom
            oMinertia = (oMcom) * comMinertia
            # apply shaped box with tf to MeshCat
            # TODO change this to add objects only if they are not already in the viewer
            self.addBox(f"{self.model.names[idJoint]}", [h, w, d], "red", category="inertias")
            self.set_pose(f"{self.model.names[idJoint]}", oMinertia, category="inertias")

            self.addSphere(f"{self.model.names[idJoint]}_CoM", 0.01*scale_com, "blue", category="inertias")
            self.set_pose(f"{self.model.names[idJoint]}_CoM", oMcom, category="inertias")
    
    def addArrow(self, name, position, vector, radius, length, color="green", prefix="arrows"):
        if not isinstance(color, str):
            if not isinstance(color, list):
                raise AttributeError("color must be a string or a list of 3 to 4 integers")
            elif not (len(color)==3 or len(color)==4):
                raise AttributeError("color list must have 3 or 4 elements")
        if isinstance(color, str):
            if color not in COLORS_PREDEFINED.keys():
                raise AttributeError(f"color must be one of {COLORS_PREDEFINED.keys()} or a list of rgb values")
            color = COLORS_PREDEFINED[color]
        
        complete_prefix = f"{self.objects_prefix}/{prefix}"
        rr.log(
            f"{complete_prefix}/{name}",
            rr.archetypes.Arrows3D(
                origins=[position],
                vectors=[(np.array(vector)*length).tolist()],
                radii=[radius],
                colors=[color],
            ),
        )
    
    def drawFrame(self, name, placement, length=1e-1, radius=1e-3, scaling=1, prefix="frames"):
        length *= scaling
        radius *= scaling
        position = placement.translation
        rotation = placement.rotation
        # X arrow
        self.addArrow(f"{name}_X", position, rotation[:, 0], radius, length, "red", f"{prefix}/{name}")
        # Y arrow
        self.addArrow(f"{name}_Y", position, rotation[:, 1], radius, length, "green", f"{prefix}/{name}")
        # Z arrow
        self.addArrow(f"{name}_Z", position, rotation[:, 2], radius, length, "blue", f"{prefix}/{name}")

    def captureImage(self):
        pass
    def disableCameraControl(self):
        pass
    def displayCollisions(self):
        pass
    def displayVisuals(self):
        pass
    def drawFrameVelocities(self):
        pass
    def enableCameraControl(self):
        pass
    def setBackgroundColor(self):
        pass
    def setCameraPose(self):
        pass
    def setCameraPosition(self):
        pass
    def setCameraTarget(self):
        pass
    def setCameraZoom(self):
        pass
