import math
import time


class Animation:
    def __init__(self, oled, fps=20):
        self.oled = oled
        self.w = oled.width
        self.h = oled.height
        self.frame_ms = 1000 // fps
        self.frame = 0

    def circle(self, cx, cy, r, col=1):
        x = r
        y = 0
        err = -r
        while x >= y:
            self.oled.pixel(cx + x, cy + y, col)
            self.oled.pixel(cx + y, cy + x, col)
            self.oled.pixel(cx - y, cy + x, col)
            self.oled.pixel(cx - x, cy + y, col)
            self.oled.pixel(cx - x, cy - y, col)
            self.oled.pixel(cx - y, cy - x, col)
            self.oled.pixel(cx + y, cy - x, col)
            self.oled.pixel(cx + x, cy - y, col)
            y += 1
            err += 2 * y - 1
            if err > 0:
                x -= 1
                err -= 2 * x + 1

    def fill_circle(self, cx, cy, r, col=1):
        for dy in range(-r, r + 1):
            dx = int(math.sqrt(r * r - dy * dy))
            self.oled.hline(cx - dx, cy + dy, 2 * dx + 1, col)

    def triangle(self, x0, y0, x1, y1, x2, y2, col=1):
        self.oled.line(x0, y0, x1, y1, col)
        self.oled.line(x1, y1, x2, y2, col)
        self.oled.line(x2, y2, x0, y0, col)

    def progress_bar(self, x, y, w, h, pct, col=1):
        self.oled.rect(x, y, w, h, col)
        fill_w = int((w - 2) * max(0, min(pct, 1)))
        if fill_w > 0:
            self.oled.fill_rect(x + 1, y + 1, fill_w, h - 2, col)

    @staticmethod
    def ease_in_out(t):
        if t < 0.5:
            return 2 * t * t
        return -1 + (4 - 2 * t) * t

    @staticmethod
    def lerp(a, b, t):
        return a + (b - a) * t

    def tween(self, a, b, duration_ms):
        t = (self.frame * self.frame_ms % duration_ms) / duration_ms
        return self.lerp(a, b, self.ease_in_out(t))

    def bounce(self, low, high, duration_ms):
        t = (self.frame * self.frame_ms % duration_ms) / duration_ms
        t = 1 - abs(2 * t - 1)
        return self.lerp(low, high, self.ease_in_out(t))

    def run(self, draw_fn):
        while True:
            start = time.ticks_ms()
            self.oled.fill(0)
            draw_fn(self)
            self.oled.show()
            self.frame += 1
            elapsed = time.ticks_diff(time.ticks_ms(), start)
            sleep = self.frame_ms - elapsed
            if sleep > 0:
                time.sleep_ms(sleep)
