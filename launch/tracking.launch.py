import os

import ament_index_python.packages
import launch
import launch_ros.actions
from launch import LaunchDescription

import yaml


def generate_launch_description():
    share_dir = ament_index_python.packages.get_package_share_directory('ros-human-sensing')
    
    params_file = os.path.join(share_dir, 'config', 'system_ros_params.yaml')

    with open(params_file, 'r') as f:
        yolo_params   = yaml.safe_load(f)['yolo_ros_node']['ros__parameters']

    with open(params_file, 'r') as f:
        boxmot_params = yaml.safe_load(f)['boxmot_ros_node']['ros__parameters']

    yolo_ros_node = launch_ros.actions.Node(package='yolo_ros',
                                              executable='yolo_ros',
                                              output='both',
                                              parameters=[yolo_params]
                                              )

    boxmot_ros_node = launch_ros.actions.Node(package='boxmot_ros',
                                              executable='boxmot_ros',
                                              output='both',
                                              parameters=[boxmot_params]
                                              )

    ld = LaunchDescription()

    ld.add_action(yolo_ros_node)
    ld.add_action(boxmot_ros_node)

    return ld