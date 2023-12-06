#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    #create a new publisher. 
    #we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('chatter',String,queue_size=10)
#choose a unique name for our talker name
    rospy.init_node('talker',anonymous=True)    
    rate=rospy.Rate(1)

    i=0
    while not rospy.is_shutdown():
        hello_str="hello world %s" %i
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass