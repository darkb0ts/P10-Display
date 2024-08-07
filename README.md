# p10-colour-display

## Overview
`p10-colour-display` is a project aimed at utilizing the `rpi-rgb-matrix` library to drive a P10 LED display on a Raspberry Pi. This project allows users to display text with features like scrolling, blinking, or both simultaneously. Users can change the displayed data through a web browser interface.

## Features
- **Scroll Text:** Display text with a scrolling effect.
- **Blink Text:** Display text with a blinking effect.
- **Scroll and Blink:** Combine both scrolling and blinking effects on the text.
- **API Integration:** 
  - **Post Data:** `localhost/postapi.php`
  - **Get Data:** `localhost/api.php`

## Installation
An automated installation script is provided to set up the project on your Raspberry Pi.

### Prerequisites
- Raspberry Pi with Raspbian OS installed
- Internet connection for downloading dependencies

### Steps
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/p10-colour-display.git
    cd p10-colour-display
    ```



2. **Run the Installation Script:**
    ```bash
    chmod +x install.sh
    ./install.sh
    ```

   The script will:
   - Install necessary dependencies
   - Set up the `rpi-rgb-matrix` library with custom pin mappings
   - Configure the web server and PHP scripts

## Usage
After installation, the P10 display will be ready to use with the following features:

### API Endpoints
- **Post Data:**
  - Endpoint: `http://localhost/post_api.php`
  - Method: POST
  - Parameters: `text`, `effect` (values: `scroll`, `blink`, `scroll_blink`)

- **Get Data:**
  - Endpoint: `http://localhost/get_data.php`
  - Method: GET



## Call Api Function(Sample Curl cmd And Sample Json Data)
  
  - **GET METHOD**
  ```
    curl -X GET http://localhost/api.php

  ```

  - **Sample Data:**
    ```
        [
       {
          "id":"1",
          "text":"Welcome to Magneto Dynamic ",
          "audio":"luffy",
          "scrolling":"0",
          "blink":"1"
       },
       {
          "id":"2",
          "text":"CandyScooby",
          "audio":"naruto",
          "scrolling":"0",
          "blink":"1"
       },
       {
          "id":"3",
          "text":"P10-Led Display Ip: 192.168.1.14",
          "audio":"hello",
          "scrolling":"0",
          "blink":"1"
       }
      ]
    ```


  - **POST METHOD**
  ```
    curl -X POST http://localhost/api.php

  ```


  - **Sample Data for Post:**
  ```
      curl -X POST http://localhost/api.php \
      -H "Content-Type: application/json" \
      -d '[
          {
              "id": "1",
              "text": "Welcome to Magneto Dynamic",
              "audio": "luffy",
              "scrolling": "0",
              "blink": "1"
          },
          {
              "id": "2",
              "text": "CandyScooby",
              "audio": "naruto",
              "scrolling": "0",
              "blink": "1"
          },
          {
              "id": "3",
              "text": "P10-Led Display Ip: 192.168.1.14",
              "audio": "hello",
              "scrolling": "0",
              "blink": "1"
          }
      ]'
  ```


### Web Interface
Open your web browser and navigate to `http://<your_raspberry_pi_ip_address>` to access the user interface where you can change the displayed text and select effects.

## Custom Pin Mapping
The project uses a modified pin mapping configuration for the P10 display. Ensure your wiring matches the configuration defined in the `rpi-rgb-matrix` library settings.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the project's coding guidelines.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify this template as per your specific requirements.