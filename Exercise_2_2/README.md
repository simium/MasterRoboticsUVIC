#Creating a ROS workspace
_Initialise the workspace_
```shell
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
```

_Build an empty workspace_
```shell
$ cd ~/catkin_ws/
$ catkin_make
```

_Update your environment_
```shell
$ cd ~/catkin_ws/
$ source devel/setup.bash
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
#Creating a ROS Package
```shell
$ cd ~/catkin_ws/src
$ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
$ catkin_make
$ source ~/catkin_ws/devel/setup.bash
```

```shell
jp@ubuntu:~/catkin_ws$ rospack depends1 beginner_tutorials
roscpp
rospy
std_msgs

jp@ubuntu:~/catkin_ws$ roscd beginner_tutorials
jp@ubuntu:~/catkin_ws/src/beginner_tutorials$ cat package.xml
```
```xml
<?xml version="1.0"?>
<package>
  <name>beginner_tutorials</name>
  <version>0.0.0</version>
  <description>The beginner_tutorials package</description>

  <!-- One maintainer tag required, multiple allowed, one person per tag -->
  <!-- Example:  -->
  <!-- <maintainer email="jane.doe@example.com">Jane Doe</maintainer> -->
  <maintainer email="jp@todo.todo">jplopez</maintainer>


  <!-- One license tag required, multiple allowed, one license per tag -->
  <!-- Commonly used license strings: -->
  <!--   BSD, MIT, Boost Software License, GPLv2, GPLv3, LGPLv2.1, LGPLv3 -->
  <license>TODO</license>


  <!-- Url tags are optional, but mutiple are allowed, one per tag -->
  <!-- Optional attribute type can be: website, bugtracker, or repository -->
  <!-- Example: -->
  <!-- <url type="website">http://wiki.ros.org/beginner_tutorials</url> -->


  <!-- Author tags are optional, mutiple are allowed, one per tag -->
  <!-- Authors do not have to be maintianers, but could be -->
  <!-- Example: -->
  <!-- <author email="jane.doe@example.com">Jane Doe</author> -->


  <!-- The *_depend tags are used to specify dependencies -->
  <!-- Dependencies can be catkin packages or system dependencies -->
  <!-- Examples: -->
  <!-- Use build_depend for packages you need at compile time: -->
  <!--   <build_depend>message_generation</build_depend> -->
  <!-- Use buildtool_depend for build tool packages: -->
  <!--   <buildtool_depend>catkin</buildtool_depend> -->
  <!-- Use run_depend for packages you need at runtime: -->
  <!--   <run_depend>message_runtime</run_depend> -->
  <!-- Use test_depend for packages you need only for testing: -->
  <!--   <test_depend>gtest</test_depend> -->
  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>
  <run_depend>roscpp</run_depend>
  <run_depend>rospy</run_depend>
  <run_depend>std_msgs</run_depend>


  <!-- The export tag contains other, unspecified, tags -->
  <export>
    <!-- Other tools can request additional information be placed here -->

  </export>
```

_Let's clean the final package.xml_
```xml
<?xml version="1.0"?>
<package>
  <name>beginner_tutorials</name>
  <version>0.1.0</version>
  <description>The beginner_tutorials package for UVic Master on Robotics</description>

  <maintainer email="do.not.want.spam@uvic.cat">Juampe</maintainer>
  <license>BSD</license>
  <url type="repository">http://github.com/simium</url>
  <author email="do.not.want.spam@uvic.cat">Juampe</maintainer>


  <buildtool_depend>catkin</buildtool_depend>

  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>

  <run_depend>roscpp</run_depend>
  <run_depend>rospy</run_depend>
  <run_depend>std_msgs</run_depend>

</package>
```

#Building a ROS Package
```shell
jp@ubuntu:~/catkin_ws/src$ ls
beginner_tutorials  CMakeLists.txt

jp@ubuntu:~/catkin_ws/src$ cd ..
jp@ubuntu:~/catkin_ws$ ls
build  devel  src

jp@ubuntu:~/catkin_ws$ catkin_make
Base path: /home/jp/catkin_ws
Source space: /home/jp/catkin_ws/src
Build space: /home/jp/catkin_ws/build
Devel space: /home/jp/catkin_ws/devel
Install space: /home/jp/catkin_ws/install
Invalid package manifest "/home/jp/catkin_ws/src/beginner_tutorials/package.xml": The manifest contains invalid XML:
mismatched tag: line 10, column 52
jp@ubuntu:~/catkin_ws$ catkin_make
Base path: /home/jp/catkin_ws
Source space: /home/jp/catkin_ws/src
Build space: /home/jp/catkin_ws/build
Devel space: /home/jp/catkin_ws/devel
Install space: /home/jp/catkin_ws/install
####
#### Running command: "make cmake_check_build_system" in "/home/jp/catkin_ws/build"
####
-- Using CATKIN_DEVEL_PREFIX: /home/jp/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /home/jp/catkin_ws/devel;/opt/ros/indigo
-- This workspace overlays: /home/jp/catkin_ws/devel;/opt/ros/indigo
-- Using PYTHON_EXECUTABLE: /usr/bin/python
-- Using Debian Python package layout
-- Using empy: /usr/bin/empy
-- Using CATKIN_ENABLE_TESTING: ON
-- Call enable_testing()
-- Using CATKIN_TEST_RESULTS_DIR: /home/jp/catkin_ws/build/test_results
-- Found gtest sources under '/usr/src/gtest': gtests will be built
-- Using Python nosetests: /usr/bin/nosetests-2.7
-- catkin 0.6.14
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 1 packages in topological order:
-- ~~  - beginner_tutorials
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin package: 'beginner_tutorials'
-- ==> add_subdirectory(beginner_tutorials)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/jp/catkin_ws/build
####
#### Running command: "make -j4 -l4" in "/home/jp/catkin_ws/build"
####

jp@ubuntu:~/catkin_ws$ ls
build  devel  src
```
