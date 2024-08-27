import example_robot_data as robex
import pinocchio as pin
import numpy as np
import rerun.blueprint as rrb
import rerun as rr

from pinocchio_rerun import RerunVisualizer

solo = robex.load("solo12")
model = solo.model
visual_model = solo.visual_model
collision_model = solo.collision_model

rviz = RerunVisualizer(model, collision_model, visual_model)
rviz.loadViewerModel()

rviz.activateInertias()
rviz.display(solo.q0)

print("Done loading model")