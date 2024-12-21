from machine import Pin

from cats_door.config import switch_pin_num

switch_pin = Pin(switch_pin_num, Pin.OUT)
switch_pin.value(0)


def change_status(status):
    return switch_pin.value(status)


def status():
    return switch_pin.value()
