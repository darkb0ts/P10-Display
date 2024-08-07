import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import string

# Configure the LED matrix
options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 3
options.parallel = 2
options.multiplexing = 4
options.brightness = 70  # Set brightness to 70%
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
font2 = graphics.Font()
font2.LoadFont("../../../fonts/6x12.bdf")  
font3 = graphics.Font()
font3.LoadFont("../../../fonts/6x13.bdf")  


# Calculate text width for scrolling effect
text_width = graphics.DrawText(matrix, font, 0, 0, Row1Color, text)

def draw_text(offset, show=True):
    """Draw or clear text based on the show flag."""
    zed = matrix.width - offset
    if show:
        graphics.DrawText(matrix, font2, 0, 10, Row1Color, text)
        graphics.DrawText(matrix, font, zed, 20, Row2Color, 'CANDYMAN')
        graphics.DrawText(matrix, font3, zed, 30, Row3Color, 'india')
    else:
        # To "clear" the text, we draw it in black (or the background color)
        black = graphics.Color(0, 0, 0)
        graphics.DrawText(matrix, font, 0, 10, black, text)
        graphics.DrawText(matrix, font, zed, 20, black, string.digits + str(string.ascii_uppercase))
        graphics.DrawText(matrix, font, zed, 30, black, string.ascii_lowercase)

try:
    blink_state = True
    blink_interval = 0.3  # Time in seconds for blink on/off
    last_blink_time = time.time()
    offset = 0

    while True:
        current_time = time.time()

        # Scroll the text
        matrix.Clear()
        draw_text(offset, show=blink_state)
        offset = (offset + 1) % (text_width + matrix.width)
        time.sleep(0.03)  # Adjust the speed of the scrolling

        # Handle blinking
        if current_time - last_blink_time >= blink_interval:
            blink_state = not blink_state
            last_blink_time = current_time

except KeyboardInterrupt:
    matrix.Clear()
