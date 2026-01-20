from machine import Pin
from uasyncio import sleep_ms, run

board_led = Pin(8, Pin.OUT)

async def start():
    timeout_ms = 100
    while True:
        for _ in range(20):
            board_led.toggle()
            await sleep_ms(timeout_ms)
        
        board_led.on()
        await sleep_ms(1000)
        timeout_ms = timeout_ms + 50

run(start())