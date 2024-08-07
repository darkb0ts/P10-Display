import time
import threading
import multiprocessing
import logging
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import requests
import json

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class LEDMatrixDisplay:
    def __init__(self):
        # Configure the LED matrix
        self.options = RGBMatrixOptions()
        self.options.rows = 16
        self.options.cols = 32
        self.options.chain_length = 3
        self.options.parallel = 2
        self.options.multiplexing = 4
        self.options.brightness = 70  # Set brightness to 70%
        self.options.hardware_mapping = 'regular'  # Adjust if needed
        self.options.gpio_slowdown = 2
        self.options.disable_hardware_pulsing = False
        self.matrix = RGBMatrix(options=self.options)

        # Load fonts
        self.font = graphics.Font()
        # Load your preferred font
        self.font.LoadFont("../../../fonts/7x13.bdf")
        self.font2 = graphics.Font()
        self.font2.LoadFont("../../../fonts/6x12.bdf")
        self.font3 = graphics.Font()
        self.font3.LoadFont("../../../fonts/6x13.bdf")

        # Colors
        self.Row1Color = graphics.Color(255, 0, 0)
        self.Row2Color = graphics.Color(0, 255, 0)
        self.Row3Color = graphics.Color(0, 0, 255)

        # Initialize text and blink states
        self.text_data = [{"text": "Loading...",
                           "scrolling": False, "blink": False}] * 3
        self.blink_state = True

    def fetch_api_data(self, url):
        """Fetch data from the API."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.text_data = data
                logging.info("Data fetched successfully.")
            else:
                logging.error(
                    f"Failed to fetch data, status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")

    def draw_text(self, offset, blink):
        """Draw text on the LED matrix."""
        self.matrix.Clear()
        for i, text_info in enumerate(self.text_data):
            font = self.font if i == 0 else (
                self.font2 if i == 1 else self.font3)
            color = self.Row1Color if i == 0 else (
                self.Row2Color if i == 1 else self.Row3Color)
            text = text_info['text']
            scrolling = text_info['scrolling']
            blink = text_info['blink'] and blink

            if scrolling:
                x_pos = self.matrix.width - offset
            else:
                x_pos = 0

            if blink:
                graphics.DrawText(self.matrix, font, x_pos,
                                  10 + i*10, color, text)
            else:
                graphics.DrawText(self.matrix, font, x_pos,
                                  10 + i*10, graphics.Color(0, 0, 0), text)

    def run(self):
        """Run the LED matrix display."""
        offset = 0
        blink_interval = 0.3
        last_blink_time = time.time()

        while True:
            current_time = time.time()
            # Handle scrolling
            offset = (offset + 1) % (self.matrix.width +
                                     len(self.text_data[0]['text']) * 6)

            # Handle blinking
            if current_time - last_blink_time >= blink_interval:
                self.blink_state = not self.blink_state
                last_blink_time = current_time

            self.draw_text(offset, self.blink_state)
            time.sleep(0.03)


def main():
    # URL of the API
    api_url = 'http://localhost/api.php'

    # Create an LEDMatrixDisplay object
    display = LEDMatrixDisplay()

    # Start a thread to fetch data from the API
    api_thread = threading.Thread(
        target=display.fetch_api_data, args=(api_url,))
    api_thread.start()

    # Start the LED matrix display in a separate process
    display_process = multiprocessing.Process(target=display.run)
    display_process.start()

    # Wait for the threads to complete
    api_thread.join()
    display_process.join()


if __name__ == "__main__":
    main()
