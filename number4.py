#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
import math
import numpy as n
roll = pitch = yaw = 0.0
target_angle = 90
kP = 2.8

def get_rotation (msg):
    global roll, pitch, yaw
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    

rospy.init_node('my_quaternion_to_euler')

sub = rospy.Subscriber ('/odom', Odometry, get_rotation)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
command= Twist()
r = rospy.Rate(10)
while not rospy.is_shutdown():

    command.linear.x = .15
    lin_x = command.linear.x
    #print(lin_x)
    target_rad = target_angle * math.pi/180
    command.angular.z = kP  * (target_rad - yaw)
    turn_z = command.angular.z
    yaw_deg = n.rad2deg(yaw)
    print (yaw_deg,turn_z)
    pub.publish(command)
    r.sleep()
