"""# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # basher.py is the send/receive signals for a remote Maqueen(TM).
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
from hashlib import md5

# ensure radio does not interfere
KEY = 0xe1324a4271a642b1fa21d841dc341f01

# set signal macros
START = "_START"
STOP = "_STOP"
BACK = "_BACK"
LEFT = "_LEFT"
NO_LEFT = LEFT + "_NO"
RIGHT = "_RIGHT"
NO_RIGHT = RIGHT + "_NO"

# switching mechanic to start or stop a direction with the same button
isLeft = False
isRight = False
isDriving = False
direction = 1

signal = ""

# send remote control signals
# `a` to turn left
def on_button_pressed_a():
    global isLeft
    global isDriving

    # flick leftward movement or lack thereof
    isLeft = not isLeft

    # cannot turn at standstill
    if isDriving == True:
        # set signal as approprite
        if isLeft:
            signal = LEFT

            # stop rightward movement
            radio.send_string(NO_RIGHT)
        else:
            signal = NO_LEFT
        radio.send_string(signal)
input.on_button_pressed(Button.A, on_button_pressed_a)

# `b` to rurn right
def on_button_pressed_b():
    global isRight
    global isDriving

    # flick rightward movement or lackthereof
    isRight = not isRight

    # cannot turn at standstill
    if isDriving == True:
        # set signal as approprite
        if isRight:
            signal = RIGHT

            # stop leftward movement
            radio.send_string(NO_LEFT)
        else:
            signal = NO_RIGHT
        radio.send_string(signal)
input.on_button_pressed(Button.B, on_button_pressed_b)

# timing for double tap
interval_ms = input.running_time()

# single-tap `a + b` to stop
def on_button_pressed_ab():
    global interval_ms
    global isDriving
    global direction
    isDriving = not isDriving
    inInterval = input.running_time() - interval_ms < 500

    # double-tap `a + b` within 1 s to reverse
    if inInterval:
        direction = -direction
    if not isDriving:
        radio.send_string(STOP)
    if isDriving:
        if direction == -1:
            radio.send_string(BACK)
        if direction == 1:
            radio.send_string(START)
        
    interval_ms = input.running_time()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# basher receives radio signals
speed = 100

def on_received_string(receivedString):
    global direction
    # set motors as approprite
    if receivedString == START:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            direction*speed)
    if receivedString == BACK:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.BACKWARD,
            direction*speed)
    if receivedString == LEFT:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            direction*speed/4)
    if receivedString == NO_LEFT:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            direction*speed)
    if receivedString == RIGHT:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            direction*speed/4)
    if receivedString == NO_RIGHT:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            direction*speed)
    if receivedString == STOP:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            0)
        #music.play(music.string_playable("C D E G E D C - ", 120),
        #    music.PlaybackMode.IN_BACKGROUND)
                
radio.on_received_string(on_received_string)

distanceToDasher = None
def on_forever():
    global distanceToDasher
    for i in range(4):
        maqueenPlusV2.set_index_color(DigitalPin.P15,
            i,
            maqueenPlusV2.rgb(100, 0, 0))
    basic.pause(1000)
    for i in range(4):
        maqueenPlusV2.set_index_color(DigitalPin.P15,
            i,
            maqueenPlusV2.rgb(0, 0, 100))
    basic.pause(1000)

    # thanks to https://wiki.dfrobot.com/micro_Maqueen_for_micro_bit_SKU_ROB0148-EN
    # and https://makecode.microbit.org/reference/radio/received-signal-strength
    distanceToDasher = maqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)
    radio.send_number(int(distanceToDasher))
basic.forever(on_forever)
