#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import  Twist
from math import atan2

x = 0.0
y = 0.0 
yaw = 0.0

def newOdom(msg):
    global x
    global y
    global yaw

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, yaw) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

#rospy.init_node("speed_controller")
rospy.init_node("me_459_hw3_5")

sub = rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)

speed = Twist()

r = rospy.Rate(20)

#goal = Point()
#goal.x = 5
#goal.y = 5
path_list =[[0.0,0.0],[0.0,1.0],[2.0,2.0],[3.0,-3.0]]
while not rospy.is_shutdown():
    for point in path_list:
        while abs(point[0]-x) > .1 and abs(point[1]-y) > .1 :
            inc_x = point[0] - x
            inc_y = point[1] - y

            angle_to_goal = atan2(inc_y, inc_x)

            if abs(angle_to_goal - yaw) > 0.1:
                speed.linear.x = 0.0
                speed.angular.z = 0.2
            else:
                speed.linear.x = 0.15
                speed.angular.z = 0.0

            pub.publish(speed)
            r.sleep()    
