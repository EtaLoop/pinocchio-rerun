import example_robot_data as robex
import pinocchio as pin
import numpy as np
import rerun.blueprint as rrb
import rerun as rr

from rerun_visualizer_draft import RerunVisualizer

try:
    from example_parallel_robots.loader_tools import completeRobotLoader
    from toolbox_parallel_robots.freeze_joints import freezeJoints
    from toolbox_parallel_robots.projections import configurationProjection
except ImportError:
    print(
        "Please install the `toolbox_parallel_robots` and `example_parallel_robots` packages to run this model"
    )
urdffile = "robot.urdf"
yamlfile = "robot.yaml"
urdfpath = "../../Software_LAAS_INRIA/sobec/examples/walk_without_think/model_robot_virgile/model_6d"
(
    model,
    robot_constraint_models,
    actuation_model,
    visual_model,
    collision_model,
) = completeRobotLoader(urdfpath, urdffile, yamlfile, freeflyer=True)

rviz = RerunVisualizer(model, collision_model, visual_model)
rviz.loadViewerModel()

print("Done loading model")