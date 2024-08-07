import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Api_call:
    def __init__(self) -> None:
        self.First_Line = None
        self.Second_Line = None
        self.Third_Line = None
        self.scroll_text = False
        self.Scroll_First_Line = 0
        self.Scroll_Second_Line = 0
        self.Scroll_Third_Line = 0
        self.Blink_First_Line = 0
        self.Blink_Second_Line = 0
        self.Blink_Third_Line = 0
