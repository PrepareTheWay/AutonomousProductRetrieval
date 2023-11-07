#!/usr/bin/env pybricks-micropython
'''
Anderson Nguyen | nguye4av | 27 Oct 2023 | 2:04 pm 

Subtask 1

'''

import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
center_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=70, axle_track=132)


# robot.turn(360)
ev3.speaker.beep(frequency=800, duration=300)


'''robot.straight(500)
robot.turn(180)
robot.straight(500)
robot.turn(180)'''

#robot.straight(100)
center_motor.run_time(500,2500)
# ev3.speaker.beep(frequency=600, duration=300)
robot.straight(400)
# center_motor.run_time(-500,2500)
#robot.straight(-100)
#robot.turn(180)
# ev3.speaker.play_file(SoundFile.FANTASTIC)