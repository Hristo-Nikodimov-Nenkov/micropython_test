from machine import Pin
from utime import sleep

board_led = Pin(8, Pin.OUT)
for _ in range(20):
    board_led.toggle()
    sleep(0.1)