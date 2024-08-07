import requests
import json
import logging
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics  # type: ignore
from led_matrix_config import LEDMatrixConfig  # type: ignore
import time

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class ApiCall:
    def __init__(self):
        self.data = None
        self.url = None

    def json_decode_data(self, res: requests.Response) -> list:
        try:
            self.data = res.json()
            return self.data
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return []

    def decode_data(self, data: list) -> list:
        results = []
        for item in data:
            result = {
                'text': item.get('text', ''),
                'scrolling': item.get('scrolling', False),
                'blink': item.get('blink', False)
            }
            results.append(result)
        return results

    def api_call(self, url: str) -> list:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            json_data = self.json_decode_data(response)
            return self.decode_data(json_data)
        except requests.RequestException as e:
            logging.error(f"API request error: {e}")
            return []


class CustomLEDMatrix(LEDMatrixConfig):
    def __init__(self):
        super().__init__()
        try:
            self.matrix = RGBMatrix(options=self._options)
            logging.info("Matrix initialized successfully.")
        except Exception as e:
            logging.error(f"Error initializing matrix: {e}")
            raise

    def display_text(self, texts: list):
        """Display text on the LED matrix."""
        k = 0
        font = graphics.Font()
        try:
            font.LoadFont("../../../fonts/6x12.bdf")
        except Exception as e:
            logging.error(f"Error loading font: {e}")
            raise
        x = graphics.Color(255, 0, 0)
        colors = [graphics.Color(255, 0, 0), graphics.Color(
            0, 255, 0), graphics.Color(0, 0, 255)]

        # while True:
        #     for i, text_info in enumerate(texts):
        #         text = text_info.get('text', '')
        #         scrolling = text_info.get('scrolling', False)
        #         blink = text_info.get('blink', False)
        #         if blink:
        #             color = colors[i % len(colors)] if time.time() % 2 < 1 else graphics.Color(0, 0, 0)
        #         else:
        #             color = colors[i % len(colors)]
        print("matrix width is", self.matrix.width)
        for i, text_info in enumerate(texts):
            k = 0
            text = text_info.get('text', '')
            scrolling = int(text_info.get('scrolling', False))
            blink = int(text_info.get('blink', False))
            print(
                f"text is {text},scrolling {scrolling},blink {blink}")
            # if blink:
            #     color = graphics.Color(0, 0, 0)
            #     print("blink is working and index - {i} and color")
            # else:
            #     color = colors[i % len(colors)]
            #     print("blink is not working", i)
            if scrolling:
                print("scrolling is working", i)
                # 7 best time scroll the three text with one by one time , 10 little long
                text_width = len(text) * 7
                for offset in range(text_width + self.matrix.width):
                    self.matrix.Clear()
                    x_position = self.matrix.width - offset
                    graphics.DrawText(self.matrix, font,
                                      x_position, (i + 1) * 10, color, text)
                    time.sleep(0.02)
            else:
                print("scrolling is not working", i)
                for xyk in range(10):
                    if xyk % 2 == 0:
                        co = graphics.Color(0, 0, 0)
                    else:
                        co = graphics.Color(255, 0, 0)
                    graphics.DrawText(self.matrix, font, 0,
                                      (i + 1) * 10, co, text)
                    time.sleep(0.2)

                # self.matrix.Clear()
                # graphics.DrawText(self.matrix, font, 0,
                #                   (i + 1) * 10, x, text)
                # k += 1
                # time.sleep(0.3)
                # black = graphics.Color(0, 0, 0)
                # graphics.DrawText(self.matrix, font, 0,
                #                   (i + 1) * 10, black, text)
                # time.sleep(0.2)

            print("------------------------------------------")


# Example usage
if __name__ == "__main__":
    api = ApiCall()
    matrix = CustomLEDMatrix()
    matrix.brightness = 80

    url = "http://localhost/api.php"
    text_data = api.api_call(url)
    matrix.display_text(text_data)
