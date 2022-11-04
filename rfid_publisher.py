 #! /usr/bin/env python

import rospy
from std_msgs.msg import String
import serial
 
def talker():
    pub = rospy.Publisher('rfid', String, queue_size=10)
    rospy.init_node('rfid', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
    ser.reset_input_buffer()

    while not rospy.is_shutdown():
        if ser.in_waiting > 0:
            id = ser.readline().decode('utf-8').rstrip()
            cmd = String()
            cmd.data = id
            pub.publish(cmd)
            rate.sleep()
   
if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass