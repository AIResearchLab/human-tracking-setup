#---------------------------------------------------------------------------------------------------------------------------
#----
#----   Start base image
#----
#---------------------------------------------------------------------------------------------------------------------------

FROM ros:humble-ros-base-jammy as base

## Parameters
ENV WORKSPACE_ROOT=/system

#############################################################################################################################
#####
#####   Install Dependencies
#####
#############################################################################################################################

WORKDIR /

RUN apt-get update -y

RUN apt-get install -y --no-install-recommends  python3-pip \
                                                libboost-python-dev \
                                                ros-dev-tools \
                                                ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
                                                ros-$ROS_DISTRO-vision-opencv

RUN apt-get clean

#############################################################################################################################
#####
#####   Clone and build Yolo packages
#####
#############################################################################################################################

WORKDIR ${WORKSPACE_ROOT}/src

RUN git clone https://github.com/KalanaRatnayake/yolo_ros.git
RUN git clone https://github.com/KalanaRatnayake/detection_msgs.git
RUN git clone https://github.com/KalanaRatnayake/boxmot_ros.git
RUN git clone https://github.com/AIResearchLab/ros-human-sensing.git

RUN pip3 install --no-cache-dir -r ${WORKSPACE_ROOT}/src/boxmot_ros/requirements.txt
RUN pip3 install --no-cache-dir -r ${WORKSPACE_ROOT}/src/yolo_ros/requirements.txt

RUN rosdep install --from-paths ${WORKSPACE_ROOT}/src -y --ignore-src

WORKDIR ${WORKSPACE_ROOT}

RUN . /opt/ros/humble/setup.sh && colcon build

WORKDIR /

#############################################################################################################################
#####
#####   Remove workspace source and build files that are not relevent to running the system
#####
#############################################################################################################################

RUN rm -rf ${WORKSPACE_ROOT}/src
RUN rm -rf ${WORKSPACE_ROOT}/log
RUN rm -rf ${WORKSPACE_ROOT}/build

RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /tmp/*

RUN apt-get clean

#---------------------------------------------------------------------------------------------------------------------------
#----
#----   Start final release image
#----
#---------------------------------------------------------------------------------------------------------------------------


FROM ros:humble-ros-base-jammy as final

## Parameters

ENV WORKSPACE_ROOT=/system

ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

WORKDIR /

COPY --from=base / /

COPY docker/workspace_entrypoint.sh /workspace_entrypoint.sh

RUN chmod +x /workspace_entrypoint.sh

ENTRYPOINT [ "/workspace_entrypoint.sh" ]

WORKDIR ${WORKSPACE_ROOT}

CMD ros2 launch ros-human-sensing tracking.launch.py
        