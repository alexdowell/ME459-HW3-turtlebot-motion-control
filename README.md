# ME459 HW3: TurtleBot Motion Control  

## Description  
This repository contains solutions for **ME459 HW3**, focusing on controlling a TurtleBot's motion using ROS (Robot Operating System). The assignment involves quaternion-to-Euler angle conversion, proportional control for heading correction, and path-following implementation for autonomous navigation.  

## Files Included  

### **Problem 3: Basic TurtleBot Movement**  
- **File:** number3.py  
- **Topics Covered:**  
  - ROS node initialization  
  - Basic velocity commands for TurtleBot movement  

### **Problem 4: Quaternion to Euler Angle Conversion and Heading Control**  
- **File:** number4.py  
- **Topics Covered:**  
  - ROS subscriber for odometry messages  
  - Conversion of quaternion orientation to Euler angles  
  - Proportional control for heading correction  

### **Problem 5: Path-Following Control**  
- **File:** number5.py  
- **Topics Covered:**  
  - TurtleBot autonomous navigation  
  - Path-following implementation using waypoints  
  - Angular correction based on goal angle  

### **Additional Files**  
- **File:** ME 459 HW 3.pdf  
  - Problem statement and theoretical background  
- **File:** ME 459 HW 3 #4.csv  
  - Dataset required for Problem 4  
- **File:** ME 459 HW 3 #5.csv  
  - Dataset required for Problem 5  
- **File:** ME 459 HW 3 new.csv  
  - Updated dataset for additional testing  

## Installation  
Ensure you have ROS installed and running before executing the scripts.  

### Required ROS Packages  
- rospy  
- nav_msgs.msg  
- tf.transformations  
- geometry_msgs.msg  

## Usage  
1. Launch a ROS core service using:  
   `roscore`  
2. Open a new terminal and start the TurtleBot simulation:  
   `roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch`  
3. Run the Python scripts:  
   - For Problem 3: `rosrun me459_hw3 number3.py`  
   - For Problem 4: `rosrun me459_hw3 number4.py`  
   - For Problem 5: `rosrun me459_hw3 number5.py`  

## Example Output  
- **Quaternion to Euler Conversion (Problem 4)**  
  - `Yaw Angle: 90.0 degrees`  
  - `Angular Correction Applied: 0.15 rad/s`  

- **Path-Following (Problem 5)**  
  - TurtleBot navigates through waypoints `[0.0,0.0] → [0.0,1.0] → [2.0,2.0] → [3.0,-3.0]`  
  - Adjusts angular velocity based on heading error  

## Contributions  
This repository is designed for educational and research purposes. Feel free to fork and modify the scripts.  

## License  
This project is open for educational use.  

---  
**Author:** Alexander Dowell  
