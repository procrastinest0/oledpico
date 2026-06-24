from machine import Pin, SoftI2C
import ssd1306
import math
import time
from animation import Animation

i2c = SoftI2C(sda=Pin(10, Pin.PULL_UP), scl=Pin(11, Pin.PULL_UP), freq=100000)
time.sleep(0.5)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

anim = Animation(oled, fps=20)


def scene(a):
    # Bouncing ball
    ball_y = int(a.bounce(5, 45, 2000))
    ball_x = int(a.bounce(10, 110, 3000))
    a.fill_circle(ball_x, ball_y, 6)

    # Expanding rings
    for i in range(3):
        r = (a.frame * 2 + i * 15) % 45
        a.circle(64, 32, r)

    # Rotating triangle
    angle = a.frame * 0.1
    cx, cy, size = 100, 16, 10
    x0 = int(cx + size * math.cos(angle))
    y0 = int(cy + size * math.sin(angle))
    x1 = int(cx + size * math.cos(angle + 2.094))
    y1 = int(cy + size * math.sin(angle + 2.094))
    x2 = int(cx + size * math.cos(angle + 4.189))
    y2 = int(cy + size * math.sin(angle + 4.189))
    a.triangle(x0, y0, x1, y1, x2, y2)

    # Progress bar that loops
    pct = (a.frame % 100) / 100
    a.progress_bar(4, 56, 120, 7, pct)


anim.run(scene)
