# ROS Human Detection

A human detection sensor setup for Social Aware Navigation.

To use GPU with docker while on AMD64 systems, install nvidia-container-toolkit with given instructions.

## Docker based Installation

```sh
git clone https://github.com/AIResearchLab/ros-human-detection.git
```

<details> 
<summary> <h3> on AMD64 </h3> </summary>

### Startup

```sh
cd ros-human-detection
docker compose -f compose.amd64.yml pull
docker compose -f compose.amd64.yml up
```

### Stopping

```sh
docker compose -f compose.amd64.yml down
```

### Remove docker volumes for resetting

```sh
docker volume rm ros-human-detection_yolo
```

</details>

<details> 
<summary> <h3> on JetsonNano </h3> </summary>

### Startup

```sh
cd ros-human-detection
docker compose -f compose.jnano.yml pull
docker compose -f compose.jnano.yml up
```

### Stopping

```sh
docker compose -f compose.jnano.yml down
```

### Remove docker volumes for resetting

```sh
docker volume rm ros-human-detection_yolo
```
</details>

## ROS based Installation

1) Create a workspace.

1) Setup [AIResearchLab/OrbbecSDK_ROS2](https://github.com/AIResearchLab/OrbbecSDK_ROS2), [AIResearchLab/astra_legacy_ros](https://github.com/AIResearchLab/astra_legacy_ros) or any other camera system that support standard ROS conventions following given instructions.

2) Setup [KalanaRatnayake/yolo_ros](https://github.com/KalanaRatnayake/yolo_ros) following given instructions.

3) Build the workspace and start the camera system and yolo_ros package
