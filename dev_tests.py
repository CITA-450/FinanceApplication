def checkLedgerDB():
    from sqlalchemy import create_engine, MetaData, Table
    from sqlalchemy.orm import sessionmaker

    DB_NAME = "instance/liteDB_cita450.db"

    # Create an engine
    engine = create_engine(f"sqlite:///{DB_NAME}")

    # Initialize MetaData without the bind parameter
    metadata = MetaData()

    # Reflect your ledger table
    ledger_table = Table('ledger', metadata, autoload_with=engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Print column names to test
    print(ledger_table.columns.keys())
    
def create_pdf_report(data):
    # Create a PDF report using a library like reportlab
    # This will depend on the structure of your data and the desired format of the report
    pass

from PIL import Image
import numpy as np
image0 = f'.\website\static\images\Finance_logo.png'
image1 = f'.\website\static\images\plain_logo.png'
image2 = f'.\website\static\images\slogan.png'

ANSI_BLACK = "\u001b[30m"
ANSI_RED = "\u001b[31m"
ANSI_GREEN = "\u001b[32m"
ANSI_YELLOW = "\u001b[33m"
ANSI_BLUE = "\u001b[34m"
ANSI_MAGENTA = "\u001b[35m"
ANSI_CYAN = "\u001b[36m"
ANSI_WHITE = "\u001b[37m"
ANSI_RESET = "\u001b[0m"
 # Map ASCII characters to colors 
color_map = {
        "@": ANSI_WHITE,
        "#": ANSI_BLACK,
        "S": ANSI_GREEN,
        "%": ANSI_WHITE,
        "?": ANSI_BLUE,
        "*": ANSI_MAGENTA,
        "+": ANSI_YELLOW,
        ";": ANSI_YELLOW,
        ":": ANSI_YELLOW,
        ",": ANSI_BLUE,
        ".": ANSI_WHITE
    }

# Function to convert the image to ASCII
def image_to_ascii(image_path, new_width):
    # ASCII characters used to build the output text
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    # Load the image and convert it to grayscale
    image = Image.open(image_path)
    image = image.resize((new_width, new_width))
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

# Convert image to ASCII and print
ascii_art1 = image_to_ascii(image_path=image1, new_width=200)
print_colored_ascii(ascii_art1)



#ascii_art2 = image_to_ascii(image_path=image2, new_width=200)
#ascii_art3 = image_to_ascii(image_path=image0, new_width=200)
#print_colored_ascii(ascii_art2)
#print_colored_ascii(ascii_art3)
