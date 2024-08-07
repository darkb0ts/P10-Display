from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.parallel = 2
options.multiplexing = 4
options.chain_length = 3
options.gpio_slowdown = 2
options.hardware_mapping = 'regular'  # If you are using Adafruit HAT

# Create an instance of the matrix
matrix = RGBMatrix(options=options)

# Set colors for the specific LEDs


def set_leds(matrix):
    matrix.Clear()

    # Set color for [0,1] and [1,1]
    color = graphics.Color(255, 0, 0)  # Red color
    k = 0
    for i in range(96):
        matrix.SetPixel(i, 0, color.red, color.green,
                        color.blue)  # LED at (0,1)
        # k += 1
        # if k == 16:
        #     k = 0
    # matrix.SetPixel(0, 2, color.red, color.green, color.blue)  # LED at (1,1)


if __name__ == "__main__":
    try:
        set_leds(matrix)
        input("Press Enter to exit...\n")
    except KeyboardInterrupt:
        pass
    finally:
        matrix.Clear()
