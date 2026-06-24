from machine import Pin, I2C
import ssd1306
import time

# Initialize I2C on bus 1: GP10 = SDA, GP11 = SCL
i2c = I2C(1, sda=Pin(10), scl=Pin(11), freq=400000)

# 0.96" OLED is 128x64 pixels
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display
oled.fill(0)

# Show a welcome message
oled.text("Hello!", 0, 0)
oled.text("Pico + OLED", 0, 16)
oled.text("Ready to go.", 0, 32)
oled.show()
