#Creating a ROS workspace
_Initialise the workspace_
```shell
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
```

_Build an empty workspace_
```shell
cd ~/catkin_ws/
catkin_make
```

_Update your environment_
```shell
cd ~/catkin_ws/
source devel/setup.bash
```

#Navigating the ROS Filesystem
```shell
jp@ubuntu:~/catkin_ws$ rospack find roscpp
/opt/ros/indigo/share/roscpp

jp@ubuntu:~/catkin_ws$ roscd roscpp
jp@ubuntu:/opt/ros/indigo/share/roscpp$ pwd
/opt/ros/indigo/share/roscpp

jp@ubuntu:/opt/ros/indigo/share/roscpp$ roscd roscpp/cmake
jp@ubuntu:/opt/ros/indigo/share/roscpp/cmake$ pwd
/opt/ros/indigo/share/roscpp/cmake

jp@ubuntu:/opt/ros/indigo/share/roscpp/cmake$ roscd log
No active roscore
jp@ubuntu:~/.ros/log$ rosls roscpp_tutorials
cmake  launch  package.xml  srv
```
