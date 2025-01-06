"""# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # dasher.py is an autonomous Maqueen(TM) that avoids obstacles.
 # Copyright (C) 2024-2025 phan-my.
 # Copyright (C) 2024-2025 Vlad.
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"""
from microbit import *

# automaton mechanisms
def on_forever():
    speed = 120
    
    untilCollision_cm = maqueenPlusV2.read_ultrasonic(DigitalPin.P13,
        DigitalPin.P14)

    # reverse and turn if too close to wall
    if untilCollision_cm < 10:
        # reverse
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.BACKWARD,
            100)
        basic.pause(500)

        # random turn l/r
        turn = randint(0, 1)
        if turn == 0:
            leftWheel = 0
            rightWheel = speed/4
        if turn == 1:
            leftWheel = 0
            rightWheel = speed/4

        # set wheels the random speed
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD, leftWheel)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD, rightWheel)
        basic.pause(randint(250, 500))
    else:
        # default straightforward movement
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD, speed)
basic.forever(on_forever)

CODE = 0xe132

# pause if basher is too close to dasher
def on_received_number(receivedNumber):
    if receivedNumber == CODE:
        if radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) > -100:
            maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
                maqueenPlusV2.MyEnumDir.FORWARD,
                0)
            basic.pause(5000)
radio.on_received_number(on_received_number)
