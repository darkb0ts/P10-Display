from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 3
options.parallel = 2
options.multiplexing = 4
options.hardware_mapping = 'regular'  # Adjust if needed
options.gpio_slowdown = 2
options.brightness = 80

matrix = RGBMatrix(options=options)

# Load font and color
font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
textColor = graphics.Color(255, 255, 0)

# Display two lines of text
text1 = "candyscooby"
text2 = "candyscooby"
y_offset = 9  # Y position for the first line

while True:
    matrix.Clear()
    # Draw the first line of text
    for i in range(96):
        len1 = graphics.DrawText(matrix, font, 0, i, textColor, text1)
    # Draw the second line of text
    # len2 = graphics.DrawText(matrix, font, 0, y_offset + 10, textColor, text2)  # Adjust 20 as needed for spacing

    # len2 = graphics.DrawText(matrix, font, 0, y_offset + 20, textColor, text2) 
    
    time.sleep(0.1)  # Adjust the speed as needed
