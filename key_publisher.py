#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import sys, select, termios, tty

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('keyboard_publisher')
    pub = rospy.Publisher('keys', String, queue_size=10)

    try:
        while not rospy.is_shutdown():
            key = getKey()
            if key:
                rospy.loginfo(key)
                pub.publish(key)
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)