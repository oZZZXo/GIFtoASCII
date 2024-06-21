import sys
import time
from ascii_magic import AsciiArt # type: ignore
from PIL import Image

def load_gif_frames(gif_path):
    frames = []
    with Image.open(gif_path) as img:
        for frame_number in range(img.n_frames):
            img.seek(frame_number)
            frames.append(img.copy())  
            # Store a copy of the frame
    return frames

def convert_frames_to_ascii(frames):
    ascii_frames = []
    for frame in frames:
        ascii_frame = AsciiArt\
            .from_pillow_image(frame).to_ascii()
        ascii_frames.append(ascii_frame)
    return ascii_frames

def load_parameters():
    import sys
    # Retrieve arguments
    if len(sys.argv)<2:
        print("Usage: python3 animate.py ",
              "<gif_location> <delay_ms>")
        sys.exit(1)
    gif_path = sys.argv[1]
    speed = sys.argv[2] if len(sys.argv)>2 else 0.04
    return gif_path, speed

if __name__ == "__main__":
    gif_path, speed = load_parameters()
    frames = load_gif_frames(gif_path)
    ascii_frames = convert_frames_to_ascii(frames)
    while (True):
        for ascii_frame in ascii_frames:
            print(ascii_frame)
            time.sleep(float(speed))  # Adjust frame rate
            print('\033c', end='')  # Clear console

