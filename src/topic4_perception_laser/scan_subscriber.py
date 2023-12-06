import rospy
from sensor_msgs.msg import LaserScan
import math

def scan_callback(scan_data):
    #this function will return the minimum range and the index of the minimum range
    min_value,min_index = min_range_index(scan_data,ranges)
    #lets print them
    print "\nThe minimum range value is :  ",min_value
    print "\nThe minimum range index is :  ",min_index

    #this function will return the maximum range and the index of the maximum range
    max_value,max_index = max_range_index(scan_data,ranges)
    #lets print them
    print "\nThe maximum range value is :  ",max_value
    print "\nThe maximum range index is :  ",max_index

    avg_value = average_range(scan_data, ranges)
    print "\nThe average range value is ",avg_value

if __name__ =='__main__':
    #init new node and give it a name
    rospy.init_node('scan_node',anonymous=True)

    #subscriber to the topic scan
    rospy.subscriber("scan", LaserScan, scan_callback)

    #keep the python from exiting until the node is stopped
    rospy.spin()