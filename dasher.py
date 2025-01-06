"""# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # basher.py.
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
def on_forever():
    speed = 120
    untilCollision_cm = maqueenPlusV2.read_ultrasonic(DigitalPin.P13,
        DigitalPin.P14)

    if maqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14) < 10:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.BACKWARD,
            100)
        basic.pause(500)

        turn = randint(0, 1)
        
        if turn == 0:
            leftWheel = 0
            rightWheel = speed/4
        
        if turn == 1:
            leftWheel = 0
            rightWheel = speed/2
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD, leftWheel)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD, rightWheel)
        basic.pause(randint(250, 500))
    else:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD, speed)
basic.forever(on_forever)

"""
distance = 0

def on_forever():

global distance

radio.send_number(0)

pins.digital_write_pin(DigitalPin.P0, 0)

control.wait_micros(2)

pins.digital_write_pin(DigitalPin.P0, 1)

control.wait_micros(10)

pins.digital_write_pin(DigitalPin.P0, 0)

distance = Math.idiv(pins.pulse_in(DigitalPin.P11, PulseValue.HIGH), 58)

basic.show_number(distance)

basic.pause(100)

distance = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)

basic.show_number(distance)

basic.forever(on_forever)

"""