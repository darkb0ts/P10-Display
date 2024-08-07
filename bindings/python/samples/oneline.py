from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time 
# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 3
options.parallel = 2
options.multiplexing = 4
options.hardware_mapping = 'regular'  # If you have a different hardware setup, adjust accordingly
options.gpio_slowdown = 2

matrix = RGBMatrix(options=options)

# Load font and color
font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
textColor = graphics.Color(255, 255, 0)

# Display text
text = "Your Text Here"
pos = 0

while True:
    # Clear previous frame
    matrix.Clear()
    # Draw the text
    len = graphics.DrawText(matrix, font, pos,10, textColor, text)
    # Move text position
    pos -= 1
    # Reset position if the text is out of the screen
    if (pos + len < 0):
        pos = matrix.width

    time.sleep(0.05)  # Adjust the speed of the text
