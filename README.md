# Raspberry Pi Pico + 0.96" OLED (SSD1306 I2C)

MicroPython project to drive a 0.96" 128x64 I2C OLED display with a Raspberry Pi Pico.

## Wiring

| OLED Pin | Pico Pin       |
|----------|----------------|
| VCC      | 3V3 (pin 36)   |
| GND      | GND (pin 38)   |
| SDA      | GP8 (pin 11)   |
| SCL      | GP9 (pin 12)   |

## Setup

1. Flash your Pico with MicroPython firmware from [micropython.org](https://micropython.org/download/RPI_PICO/).
2. Copy `ssd1306.py` and `main.py` to the Pico using Thonny or `mpremote`.

Using Thonny:
- Open Thonny, select **MicroPython (Raspberry Pi Pico)** as the interpreter.
- Open each file and save it to the Pico (File > Save As > Raspberry Pi Pico).

Using mpremote:
```
mpremote cp ssd1306.py :ssd1306.py
mpremote cp main.py :main.py
mpremote reset
```

## Usage

After copying both files and resetting the Pico, the display will show:

```
Hello!
Pico + OLED
Ready to go.
```

## Drawing API

The display object inherits from `framebuf.FrameBuffer`, so you can use:

```python
oled.fill(0)                      # Clear screen
oled.text("Hello", x, y)         # Draw text at (x, y)
oled.pixel(x, y, 1)              # Set a pixel
oled.line(x0, y0, x1, y1, 1)    # Draw a line
oled.rect(x, y, w, h, 1)        # Draw a rectangle
oled.fill_rect(x, y, w, h, 1)   # Filled rectangle
oled.show()                       # Push buffer to display
```
