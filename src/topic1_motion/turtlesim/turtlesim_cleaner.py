#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import math
import sys
pi = 3.14159
forward=False  
up=False
#WE WANT TO RECEIVE A MASSAGE CONTAINING THE INFORMATION ABOUT WHERE THE ROBOT IS
def poseCallback(pose_msg):
    global x, y , yaw
    x=pose_msg.x
    y=pose_msg.y
    yaw=pose_msg.theta
#YOU SEND SPEED MESSAGES TO THE ROBOT TO MOVE IT
def move(vel_pub ,sped,new_x,new_y):
    global forward,up
    global x,y
    vel_msg=Twist()
    
    x0=x
    y0=y

    if(new_x>x0): 
        vel_msg.angular.x=abs(sped)  
        forward=True
    else:   
        vel_msg.angular.x=-abs(sped) 
    if(new_y>y0):
        up=True
        vel_msg.angular.y=abs(sped)  
    else:
        vel_msg.angular.y=-abs(sped) 

    loop_rate=rospy.Rate(10)    
        
    while True :    
        rospy.loginfo("Turtlesim moves")    
        vel_pub.publish(vel_msg)    
        loop_rate.sleep()   
        dist_moved_x =abs(x-x0) 
        dist_moved_y =abs(y-y0)
        print ("x=  ",x )
        print ("y=  ",y)
        #stop the robot then 
        if((new_x<= x and forward )| (new_x>= x and not forward)):
            vel_msg.angular.x=0 
        if((new_y<= y and up)|(new_y>= y and not up)):
            vel_msg.angular.y=0 

        if (vel_msg.angular.y==0 and vel_msg.angular.x==0 ):   
            rospy.loginfo("reached")    
            break   
        
    vel_pub.publish(vel_msg)    

#WHAT ABOUT ROTATING THE ROBOT?   lets try iam sure it will success in shaa Allah
def rotate(vel_pub ,sped,angle_deg,clockwise):
    vel_msg=Twist()
    global yaw
    #converting it to degree
    theta0=yaw*180/pi
    #what is the new angle?
    #It depends upon we are clockwise or counterclockwise
  
    if(clockwise):
        vel_msg.angular.z=-abs(sped)  
        new_angle =theta0 -angle_deg
    else:   
        new_angle =theta0 +angle_deg
        vel_msg.angular.z= abs(sped) 
    while(new_angle>180):
        new_angle=new_angle-360
    while(new_angle<-180):
        new_angle=new_angle+360
    loop_rate=rospy.Rate(10)    
        
    while True :    
        rospy.loginfo("Turtlesim rotates")    
        vel_pub.publish(vel_msg)    
        loop_rate.sleep()   
        print ("theta =  ",yaw*180/pi)
        print ("sped =  ",vel_msg.angular.z )     
        print ("new_angle =  ",new_angle )
        #stop the robot then 
        if(abs((yaw*180/pi)-new_angle)<=1):
            vel_msg.angular.z=0  
            rospy.loginfo("reached")    
            break   
    vel_pub.publish(vel_msg)  

def spiralMove(vel_publ,lin,ang):
    vel_msg=Twist()
    loop_rate=rospy.Rate(10)    
        
    while True :    
        vel_msg.linear.x=lin
        lin=lin+.1
        vel_msg.angular.z=ang
        rospy.loginfo("Turtlesim rotates around itself")    
        vel_pub.publish(vel_msg)    
        loop_rate.sleep()   
        if (x>9 and y>9):  
  #          vel_msg.linear.x=0
   #         vel_msg.angular.z=0
            rospy.loginfo("kefayaa ana habat")    
            break   
if __name__ == '__main__':
    #if move:
    # if len(sys.argv) == 3:
    #     newX = float(sys.argv[1])
    #     newY = float(sys.argv[2])
    # else:
    #     sys.exit(1)
 
    #if rotate
    # if len(sys.argv) == 3:
    #     myangle  = int(sys.argv[1])
    #     clockWise= bool(sys.argv[2])
    # else:
    #     sys.exit(1)

    try:
        rospy.init_node('Turtlesim_motion_Reemoo',anonymous=True)
        cmd_vel_topic = '/turtle1/cmd_vel'
        vel_pub = rospy.Publisher(cmd_vel_topic, Twist , queue_size = 10)
        pos_topic='/turtle1/pose'
        pose_subscriber = rospy.Subscriber(pos_topic,Pose,poseCallback)
        time.sleep(2) #wait a little until it sends
        myspeed=0.5
        #  move(vel_pub,myspeed,newX, newY)
        # rotate(vel_pub,myspeed,myangle,clockWise)
        spiralMove(vel_pub,0.1,4)
    except rospy.ROSInterruptException:
        pass