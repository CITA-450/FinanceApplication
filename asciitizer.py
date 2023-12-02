from PIL import Image
import numpy as np

image0 = f'.\website\static\images\Finance_logo.png'
image1 = f'.\website\static\images\plain_logo.png'
image2 = f'.\website\static\images\slogan.png'
image3 = f'.\website\static\images\FA_logo.png'

# ANSI reset code
ANSI_RESET = "\u001b[0m"
 # Map ASCII characters to colors 
 
ANSI_LIGHT_YELLOW = "\u001b[93m"
ANSI_LIGHT_GREEN = "\u001b[92m"
ANSI_LIGHT_BLUE = "\u001b[94m"
ANSI_LIGHT_MAGENTA = "\u001b[95m"
ANSI_LIGHT_CYAN = "\u001b[96m"
ANSI_LIGHT_RED = "\u001b[91m"
ANSI_LIGHT_WHITE = "\u001b[97m"
ANSI_LIGHT_BLACK = "\u001b[90m"
ANSI_WHITE = "\u001b[37m"   
ANSI_BLACK = "\u001b[30m"
ANSI_RED = "\u001b[31m"
ANSI_GREEN = "\u001b[32m"
ANSI_YELLOW = "\u001b[33m"
ANSI_BLUE = "\u001b[34m"
ANSI_MAGENTA = "\u001b[35m"
ANSI_CYAN = "\u001b[36m"

# Background colors
ANSI_LIGHT_YELLOW_BG = "\u001b[103m"
ANSI_LIGHT_GREEN_BG = "\u001b[102m"
ANSI_LIGHT_BLUE_BG = "\u001b[104m"
ANSI_LIGHT_MAGENTA_BG = "\u001b[105m"
ANSI_LIGHT_CYAN_BG = "\u001b[106m"
ANSI_LIGHT_RED_BG = "\u001b[101m"
ANSI_LIGHT_WHITE_BG = "\u001b[107m"
ANSI_LIGHT_BLACK_BG = "\u001b[100m"
ANSI_WHITE_BG = "\u001b[47m"
ANSI_BLACK_BG = "\u001b[40m"
ANSI_RED_BG = "\u001b[41m"
ANSI_GREEN_BG = "\u001b[42m"
ANSI_YELLOW_BG = "\u001b[43m"
ANSI_BLUE_BG = "\u001b[44m"
ANSI_MAGENTA_BG = "\u001b[45m"
ANSI_CYAN_BG = "\u001b[46m"



ANSI_WHITE_BG = "\u001b[47m"

color_map = {
    "@": ANSI_WHITE,
    "#": ANSI_BLACK,
    "S": ANSI_GREEN,
    "%": ANSI_WHITE,
    "?": ANSI_BLUE,
    "*": ANSI_MAGENTA,
    "+": ANSI_YELLOW,
    ";": ANSI_LIGHT_YELLOW,
    ":": ANSI_LIGHT_CYAN,
    ",": ANSI_BLUE,
    ".": ANSI_WHITE
}

# Function to convert the image to ASCII
def image_to_ascii(image_path, new_width):
    # ASCII characters used to build the output text
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    # Load the image and convert it to grayscale
    image = Image.open(image_path)
    image = image.resize((new_width, new_width-50))
    image = image.convert("L")  # convert to grayscale

    # Convert image to numpy array
    pixels = np.array(image)
    # Normalize pixel values to match ASCII_CHARS
    pixels = pixels / 255 * (len(ASCII_CHARS) - 1)
    
    ascii_image = "\n".join("".join(ASCII_CHARS[int(pixel)] for pixel in row) for row in pixels)
    return ascii_image
def save_ascii_to_file(ascii_art, file_path):
    # Create the colored ASCII art and write to a file
    with open(file_path, 'w') as file:
        for line in ascii_art.split("\n"):
            colored_line = "".join(color_map.get(char, ANSI_RESET) + char for char in line)
            file.write(colored_line + ANSI_RESET + "\n")
# Function to print the ASCII art in color
def print_colored_ascii(ascii_art):
    # Print each character in the mapped color
    for line in ascii_art.split("\n"):
        colored_line = "".join(color_map.get(char, ANSI_RESET) + char for char in line)
        print(colored_line + ANSI_RESET)
def print_ascii_from_file(file_path):
    with open(file_path, 'r') as file:
        # Simply print each line from the file
        for line in file:
            print(line, end='')


# Convert image to ASCII and print
ascii_art1 = image_to_ascii(image_path=image3, new_width=156)
save_ascii_to_file(ascii_art1, 'ascii_art_FAlogo.txt')
print_ascii_from_file('ascii_art_FAlogo.txt')


