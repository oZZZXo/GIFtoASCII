# GIFtoASCII

A small Python script that converts a GIF into an ASCII animation.

## Video Demonstration

Watch a video of the script in action [here](https://youtube.com/shorts/FlFdEifu_Dw?feature=share).

## Features

- Load frames from a GIF.
- Convert each frame to ASCII art.
- Display the ASCII art animation in the console.

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/oZZZXo/GIFtoASCII.git
   cd GIFtoASCII
   ```

2. Install the required dependencies:

   ```sh
   pip install pillow ascii-magic
   ```

## Usage

1. Place your GIF file in the project directory or provide the path to your GIF file.

2. Run the script:

   ```sh
   python3 animate.py <gif_location> <delay_ms>
   ```

   - `<gif_location>`: Path to the GIF file.
   - `<delay_ms>`: Optional. Delay between frames in milliseconds (default: 40ms).

### Example

```sh
python3 animate.py test.gif 0.04
```
## License

This project is licensed under the MIT License.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
