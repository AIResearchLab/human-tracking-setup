# ROS Human Detection

A human detection sensor setup for Social Aware Navigation.

To use GPU with docker while on AMD64 systems, install nvidia-container-toolkit with given instructions.

## Docker based Installation

```sh
git clone https://github.com/AIResearchLab/ros-human-sensing.git
```

<details> 
<summary> <h3> on AMD64 </h3> </summary>

### Startup Detection

```sh
cd src/ros-human-sensing/docker
docker compose -f compose.amd64.yml pull
docker compose -f compose.amd64.yml up
```

### Stopping

```sh
docker compose -f compose.amd64.yml down
```

### Remove docker volumes for resetting

```sh
docker volume rm docker_system
```

</details>

<details> 
<summary> <h3> on JetsonNano </h3> </summary>

### Startup

```sh
cd src/ros-human-sensing/docker
docker compose -f compose.jnano.yml pull
docker compose -f compose.jnano.yml up
```

### Stopping

```sh
docker compose -f compose.jnano.yml down
```

### Remove docker volumes for resetting

```sh
docker volume rm docker_system
```
</details>

## ROS based Installation

1) Create a workspace

```bash
mkdir -p workspace/src
cd workspace/src
```

2) Clone packages

```bash
git clone https://github.com/KalanaRatnayake/yolo_ros.git
git clone https://github.com/KalanaRatnayake/detection_msgs.git
git clone https://github.com/KalanaRatnayake/boxmot_ros.git
git clone https://github.com/AIResearchLab/ros-human-sensing.git
```

3) Install dependencies

```bash
pip3 install -r yolo_ros/requirements.txt
pip3 install -r boxmot_ros/requirements.txt
```

4) Setup [AIResearchLab/OrbbecSDK_ROS2](https://github.com/AIResearchLab/OrbbecSDK_ROS2), [AIResearchLab/astra_legacy_ros](https://github.com/AIResearchLab/astra_legacy_ros) or any other camera system that support standard ROS conventions following given instructions. 

5) Build the packages

```bash
colcon build
```

6) Start the system

- Start the camera in one terminal

- Start Detection
```bash
ros2 launch ros-human-sensing detection.launch.py
```
- Start Detection and tracking
```bash
ros2 launch ros-human-sensing tracking.launch.py
```
