#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from pyfirmata import Arduino, SERVO
from time import sleep

board = Arduino('/dev/ttyACM0') 
pin_13=board.digital[13] # base
pin_11=board.digital[11] # shoulder
pin_9 = board.digital[9] # elbow
pin_7 = board.digital[7] # gripper

pin_13.mode=SERVO
pin_11.mode=SERVO 
pin_9.mode=SERVO
pin_7.mode=SERVO

i=76  # base
j=88 # shoulder
k=133 # elbow
l=166 # gripper
m=0

pin_13.write(i)
pin_11.write(j)
pin_9.write(k)
pin_7.write(l)

def callback(data):
    key = data.data
    if key == 'a':
        print('a pressed : ',i)
        i += 1
        if i>=145:
            i=145
        pin_13.write(i)
        sleep(0.02)
    elif key == 'd':
        print('d pressed : ',i)
        i -= 1
        if i<=27:
            i=27
        pin_13.write(i)
        sleep(0.02)
    elif key == 's':
        print('s pressed : ',j)
        j -= 1
        if j<=80:
            j=80
        pin_11.write(j)
        sleep(0.02)    
    elif key == 'w':
        print('w pressed : ',j)
        j += 1
        if j>=165:
            j=165
        pin_11.write(j)
        sleep(0.02)
    elif key == '2':
        print('down pressed : ',k)
        k -= 1
        if k<=80 :
            k=80
        pin_9.write(k)
        sleep(0.02)
    elif key == '8':
        print('up pressed : ',k)
        k += 1
        if k>=178:
            k=178
        pin_9.write(k)
        sleep(0.02)
    
    elif key == ' ':
        m+=1
        print('space pressed')

        if m==1:
            for l in range (150,167,1):
                pin_7.write(l)
                sleep(0.02)

        if m==2:
            m=0
            for l in range (167,150,-1):
                pin_7.write(l)
                sleep(0.02)

def listener():
    rospy.init_node('keyboard_subscriber')
    rospy.Subscriber('keys', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()