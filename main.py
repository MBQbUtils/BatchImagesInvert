from datetime import datetime
from multiprocessing import Pool
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from traceback import print_exc

from PIL import Image
from PIL import ImageOps


def invert(filename: str):
    try:
        image = Image.open(filename)
        if image.mode == 'RGBA':
            *rgb, alpha = image.split()
            rgb_image = Image.merge('RGB', rgb)
            inverted_image = ImageOps.invert(rgb_image)
            rgb2 = inverted_image.split()
            inverted_image = Image.merge('RGBA', (*rgb2, alpha))
        else:
            inverted_image = ImageOps.invert(image)
        inverted_image.save(filename)
    except:
        print_exc()
    print(f"'{filename}' - Done!")


def main():
    Tk().withdraw()
    filenames = askopenfilenames(title='Select images to invert', multiple=True)
    start = datetime.now()
    with Pool() as p:
        p.map(invert, filenames)
    stop = datetime.now()
    diff = stop-start
    print(f"All done in {diff.total_seconds()}s!")


if __name__ == '__main__':
    main()
