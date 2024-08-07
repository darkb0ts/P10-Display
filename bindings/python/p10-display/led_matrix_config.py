import logging
from rgbmatrix import RGBMatrix, RGBMatrixOptions,  graphics

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class LEDMatrixConfig:
    def __init__(self):
        self._options = RGBMatrixOptions()
        self._options.rows = 16
        self._options.cols = 32
        self._options.chain_length = 3
        self._options.parallel = 2
        self._options.multiplexing = 4
        self._options.brightness = 70
        self._options.hardware_mapping = 'regular'
        self._options.gpio_slowdown = 2
        self._options.disable_hardware_pulsing = False
        self.matrix = None
        self.font = "../../../fonts/7x13.bdf"
        self.color = None
        self.first_row = ""
        self.second_row = ""
        self.third_row = ""
        self.first_row_scroll = 0
        self.second_row_scroll = 0
        self.third_row_scroll = 0
        self.first_row_blink = 0
        self.second_row_blink = 0
        self.third_row_blink = 0

    @property
    def brightness(self):
        return self._options.brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self._options.brightness = value
            logging.info(f'Brightness set to {value}%')
        else:
            logging.error(
                f'Invalid brightness value: {value}. Must be between 0 and 100.')

    def apply_settings(self):
        """Apply the current settings to the matrix."""
        logging.info('Applying settings to the LED matrix.')
        self.matrix = RGBMatrix(options=self._options)

    @property
    def display_font(self):
        return self.font

    @display_font.setter
    def display_font(self, value):
        if not value:
            logging.error('Invalid font path for display.')
            raise ValueError("Font path cannot be empty.")
        self.font = graphics.Font()
        self.font.LoadFont(value)
        logging.info(f'Font set to {value}')

    @property
    def display_color(self):
        self.color = graphics.Color(255, 0, 0)
        return self.color

    @display_color.setter
    def display_color(self, rgb_tuple):
        R, G, B = rgb_tuple
        if any(not (0 <= x <= 255) for x in (R, G, B)):
            logging.error(
                f'Invalid color values: {rgb_tuple}. Each must be between 0 and 255.')
            raise ValueError("RGB values must be between 0 and 255.")
        self.color = graphics.Color(R, G, B)
        logging.info(f'Color set to RGB({R}, {G}, {B})')


if __name__ == "__main__":
    matrix_config = LEDMatrixConfig()
    # matrix_config.brightness = 80
    # matrix_config.display_font = "../../../fonts/7x13.bdf"
    # matrix_config.display_color = (255, 0, 0)
    # matrix_config.apply_settings()
