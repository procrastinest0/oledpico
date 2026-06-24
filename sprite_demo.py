from machine import Pin, SoftI2C
import ssd1306
import framebuf
import time

i2c = SoftI2C(sda=Pin(10, Pin.PULL_UP), scl=Pin(11, Pin.PULL_UP), freq=100000)
time.sleep(0.5)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# 8x8 sprite frames — a simple walking figure
# Each frame is 8 bytes (8x8 monochrome, 1 bit per pixel)
FRAMES = [
    bytearray([0x18, 0x18, 0x3C, 0x5A, 0x18, 0x18, 0x24, 0x42]),  # arms out, legs apart
    bytearray([0x18, 0x18, 0x3C, 0x18, 0x18, 0x18, 0x18, 0x18]),  # standing straight
    bytearray([0x18, 0x18, 0x3C, 0x5A, 0x18, 0x18, 0x42, 0x24]),  # arms out, legs crossed
    bytearray([0x18, 0x18, 0x3C, 0x18, 0x18, 0x18, 0x18, 0x18]),  # standing straight
]

# A 16x16 heart icon
HEART = bytearray([
    0x00, 0x00,
    0x66, 0x00,
    0xFF, 0x00,
    0xFF, 0x80,
    0xFF, 0xC0,
    0x7F, 0xC0,
    0x3F, 0x80,
    0x1F, 0x00,
    0x0E, 0x00,
    0x04, 0x00,
    0x00, 0x00,
    0x00, 0x00,
    0x00, 0x00,
    0x00, 0x00,
    0x00, 0x00,
    0x00, 0x00,
])

# Wrap byte arrays in FrameBuffer objects for blit()
sprites = []
for f in FRAMES:
    sprites.append(framebuf.FrameBuffer(f, 8, 8, framebuf.MONO_HLSB))

heart_fb = framebuf.FrameBuffer(HEART, 16, 16, framebuf.MONO_HLSB)

# Animate the walking figure across the screen
frame_idx = 0
x = 0

while True:
    oled.fill(0)

    # Draw the heart icon in the top-right corner
    oled.blit(heart_fb, 108, 4)

    # Draw ground line
    oled.hline(0, 55, 128, 1)

    # Draw the walking sprite
    oled.blit(sprites[frame_idx], x, 47)

    # Scrolling text above
    oled.text("Sprite Demo", 20, 2)

    oled.show()

    frame_idx = (frame_idx + 1) % len(sprites)
    x = (x + 2) % 128

    time.sleep_ms(100)
