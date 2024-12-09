"""
Copyright (c) 2024-2024 phan-my.
Copyright (c) 2024-2024 Vlad.
===============================================================================
"""
import microbit

def on_button_pressed_a():
    radio.send_string("start_" + KEY)
input.on_button_pressed(Button.A, on_button_pressed_a)
 
def on_button_pressed_ab():
    radio.send_string("stop_" + KEY)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
 
def on_received_string(receivedString):
    if receivedString == "start_" + KEY:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            100)
    if receivedString == "stop_" + KEY:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            0)
        music.play(music.string_playable("C D E G E D C - ", 120),
            music.PlaybackMode.IN_BACKGROUND)
    if receivedString == "back_" + KEY:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.BACKWARD,
            100)
radio.on_received_string(on_received_string)
 
def on_button_pressed_b():
    radio.send_string("back_" + KEY)
input.on_button_pressed(Button.B, on_button_pressed_b)
 
KEY = ""
KEY = "phan-my_Vlad_aem_vgkta"