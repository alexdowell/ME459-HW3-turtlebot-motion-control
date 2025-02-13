#!/usr/bin/env python3
import rospy
import time
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
class Turtlebot():
    def __init__(self):
        self.odom_x = None
        self.odom_y = None
        self.odom_z = None
        #declare publishers and subscribe
        self.odom_sub = rospy.Subscriber('odom', Odometry, self.odom_cb)
        self.vel_publisher = rospy.Publisher("cmd_vel", Twist, queue_size=5)

    def odom_cb(self,msg):
        """recieve message of odom"""
        self.odom_x = msg.pose.pose.position.x
        self.odom_y = msg.pose.pose.position.y
        self.odom_z = msg.pose.pose.position.z

    def go_forward(self, speed):
        """commands the turtle to begin going forward at a certain speed"""
        twist = Twist()
        twist.linear.x = speed
        self.vel_publisher.publish(twist)

    def go_turn(self, turn_speed):
        """commands the turtle to begin turning at a angular speed"""
        twist = Twist()
        twist.angular.z = turn_speed
        self.vel_publisher.publish(twist)
    """ def heading(self, msg):
        self.orientation = msg.pose.pose.orientation
        orientation_list = [self.orientation.x, self.orientation.y, self.orientation.z] 
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
        self.vel_publisher.publish(roll, pitch, yaw) """
start_time = time.time()
stop_time_1 = 5
stop_time_2 = 5
turn_time = 2
speed = 1.5
if __name__ == '__main__':
    

    #initiate node
    rospy.init_node('turtlebot_go_python_class', anonymous=False)
    
    #control the rate of the script to recieve messages and or send messages
    rate = rospy.Rate(20)

    #instantiate Turtlebot or create an object of class Turtlebot 
    turtlebot = Turtlebot()

    #this is the main loop you can either use this or use rospy.spin
    
    while not rospy.is_shutdown():
        #print("turtle bot position", turtlebot.odom_x, turtlebot.odom_y, turtlebot.odom_z)
        elapse_time = time.time() - start_time
        print("time is", elapse_time)

        if elapse_time >= 0 and elapse_time <= stop_time_1 :
            turtlebot.go_forward(1.5)
        if elapse_time >= stop_time_1 and elapse_time <= (stop_time_1 + turn_time) :
            turtlebot.go_forward(0.0)
            turtlebot.go_turn(-.15)
        if elapse_time >= (stop_time_1 + turn_time) and elapse_time <= (stop_time_1 + turn_time + stop_time_2) :
            turtlebot.go_turn(0.0)
            turtlebot.go_forward(1.5)
        else:
            turtlebot.go_forward(0.0)
        
    rate.sleep() # sleep at this controlled rate

