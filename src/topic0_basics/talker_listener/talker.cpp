#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
    ros::init(argc,argv,"talker_node");

    ros::NodeHandle n;

    ros::Publisher chatter_publisher =n.advertise<std_msgs::String>("chatter",100);
    ros::Rate loop_rate(1);

    int i=0;    
    while(ros::ok())
    {
        std_msgs::String msg;

        std::stringstream ss;
        ss<<"Hello World"<<i
        msg.data=ss.str();

        ROS_INFO("[Talker] I published %s\n",msg.data.c_str());
        chatter_publisher.Publish(msg);

        ros::spinOnce();  //to enable ROS to process incoming massages

        loop_rate.sleep();
        i++;
    }
    return 0;
}