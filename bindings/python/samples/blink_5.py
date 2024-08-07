import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import string

options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 3
options.parallel = 2
options.multiplexing = 4
options.brightness = 70  # Example: Set brightness to 50%
options.hardware_mapping = 'regular'  # Adjust if needed
options.gpio_slowdown = 2
options.disable_hardware_pulsing = False
matrix = RGBMatrix(options=options)

# Define the text and colors
text = "HELLO WORLD"
Row1Color = graphics.Color(255, 0, 0)
Row2Color = graphics.Color(0, 255, 0)
Row3Color = graphics.Color(0, 0, 255)
font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")  # Load your preferred font

# Calculate text width for scrolling effect
text_width = graphics.DrawText(matrix, font, 0, 0, Row1Color, text)

try:
    while True:
        for offset in range(text_width + matrix.width):
            matrix.Clear()
            zed = matrix.width - offset
            graphics.DrawText(matrix, font, 0, 10, Row1Color, text)
            graphics.DrawText(matrix, font, zed, 20, Row2Color,
                              string.digits + str(string.ascii_uppercase))
            graphics.DrawText(matrix, font, zed, 30,
                              Row3Color, string.ascii_lowercase)
            time.sleep(0.02)  # Adjust the speed of the scrolling

        # Blink effect: clear the display, then show the text again
        for _ in range(5):  # Number of blinks
            matrix.Clear()
            time.sleep(0.2)  # Blink off duration
            graphics.DrawText(matrix, font, 0, 10, Row1Color, text)
            graphics.DrawText(matrix, font, 0, 20, Row2Color,
                              string.digits + str(string.ascii_uppercase))
            graphics.DrawText(matrix, font, 0, 30, Row3Color,
                              string.ascii_lowercase)
            time.sleep(0.2)  # Blink on duration

except KeyboardInterrupt:
    matrix.Clear()
