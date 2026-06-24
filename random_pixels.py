from machine import Pin, SoftI2C
import ssd1306
import time
import urandom

i2c = SoftI2C(sda=Pin(10, Pin.PULL_UP), scl=Pin(11, Pin.PULL_UP), freq=100000)
time.sleep(0.5)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

while True:
    x = urandom.getrandbits(7) % 128
    y = urandom.getrandbits(6) % 64
    oled.pixel(x, y, 1)
    oled.show()
    time.sleep_ms(50)
