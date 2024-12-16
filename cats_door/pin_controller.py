from machine import Pin

from cats_door.config import switch_pin_num


def initial_state():
    switch_pin = Pin(switch_pin_num, Pin.OUT)
    switch_pin.value(0)
