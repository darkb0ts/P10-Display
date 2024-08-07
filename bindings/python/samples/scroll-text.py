from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
import string

# Configuration for the matrix
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

# Load font and color
font = graphics.Font()
font.LoadFont("../../../fonts/6x12.bdf")
textColor = graphics.Color(255, 255, 0)
textColor2 = graphics.Color(255, 0, 0)
textColor3 = graphics.Color(255, 155, 0)
print("print matix widtch",matrix.width)
# Scroll text
text = "Welcome to Magdyn Dynamics"
text2 = "Keep clean. Keep safe."
text3 = ''
text_width = len(text) * 10  # Adjust 10 based on font width
print("text width is",text_width,len(text))

while True:
    for offset in range(text_width + matrix.width):
        matrix.Clear()
        z = matrix.width - offset
        graphics.DrawText(matrix, font, 0, 10, textColor, text)
        graphics.DrawText(matrix, font, z, 20, textColor,
                          string.digits+str(string.ascii_uppercase))
        graphics.DrawText(matrix, font, z, 30, textColor,
                          string.ascii_lowercase)
        time.sleep(0.03)  # Adjust the speed of the scrolling
