# import time
# from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics  # type: ignore
# from DisplayConfig import LEDMatrixConfig, logging   # type: ignore
# import pygame as py


# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')


# class Displayfeature(LEDMatrixConfig):

#     def FirstLin(self) -> bool:
#         return True

#     def SecondLine(self) -> bool:
#         return True

#     def ThirdLine(self) -> bool:
#         return True

#     def ClearMatrix(self) -> bool:
#         matrix.Clear()
#         return True


# class CustomLEDMatrix(LEDMatrixConfig):
#     '''
#     Scroll text - First Line, Second Line, Third Third
#     Blink Led - First Line, Second Line, Third Third
#     Play Audio - Play audio
#     Without Scroll Text - First Line, Second Line, Third Third
#     Without Blink Text - First Line, Second Line, Third Third
#     Clear Display - Clear Full Display
#     Self Test - Dummy Text
#     '''

#     def __init__(self):
#         super().__init__()
#         # Additional initialization if needed

#     def update_message(self, first_line, second_line=None, third_line=None):
#         """Update the messages to display on the LED matrix."""
#         self.first_line = first_line or ""
#         self.second_line = second_line or ""
#         self.third_line = third_line or ""
#         logging.info(
#             f"Messages updated: {first_line}, {second_line}, {third_line}")

#     def apply_custom_settings(self):
#         """Apply custom settings to the matrix."""
#         self.apply_settings()  # Apply base settings
#         # Additional custom settings can be applied here


import logging
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
from led_matrix_config import LEDMatrixConfig

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class CustomLEDMatrix(LEDMatrixConfig):
    def __init__(self):
        super().__init__()
        # Initialize the RGBMatrix object with the configured options
        try:
            self.matrix = RGBMatrix(options=self._options)
            logging.info("Matrix initialized successfully.")
        except Exception as e:
            logging.error(f"Error initializing matrix: {e}")
            raise

    def update_message(self, first_line, second_line=None, third_line=None):
        """Update the messages to display on the LED matrix."""
        self.first_line = first_line or "++++"
        self.second_line = second_line or "----"
        self.third_line = third_line or "****"
        logging.info(
            f"Messages updated: {self.first_line}, {self.second_line}, {self.third_line}")

    def apply_custom_settings(self):
        """Apply custom settings to the matrix."""
        try:
            self.apply_settings()  # Apply base settings
            logging.info("Custom settings applied.")
        except Exception as e:
            logging.error(f"Error applying custom settings: {e}")
            raise

    def display_text(self, text1, text2, text3):
        """Display text on the LED matrix."""
        # Set up fonts and colors
        font = graphics.Font()
        try:
            font.LoadFont("../../../fonts/7x13.bdf")
        except Exception as e:
            logging.error(f"Error loading font: {e}")
            raise

        Row1Color = graphics.Color(255, 0, 0)
        Row2Color = graphics.Color(0, 255, 0)
        Row3Color = graphics.Color(0, 0, 255)
        text_width = max(len(text1), len(text2), len(text3)) * 10

        try:
            while True:
                for offset in range(text_width + self.matrix.width):
                    self.matrix.Clear()
                    z = self.matrix.width - offset
                    graphics.DrawText(self.matrix, font, 0,
                                      10, Row1Color, text1)
                    graphics.DrawText(self.matrix, font, z,
                                      20, Row2Color, text2)
                    graphics.DrawText(self.matrix, font, z,
                                      30, Row3Color, text3)
                    time.sleep(0.03)  # Adjust the speed of the scrolling
        except KeyboardInterrupt:
            logging.info("Display loop interrupted by user.")
        except Exception as e:
            logging.error(f"Error during display: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        matrix = CustomLEDMatrix()
        matrix.brightness = 80
        matrix.display_text("Row 1", "Row 2", "Row 3")
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
