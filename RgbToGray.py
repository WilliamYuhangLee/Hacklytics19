from PIL import Image
import glob
import os


class RgbToGray:

    def folder_to_gray(folder_address, new_address):
        new_address = new_address + "\\"
        for img in glob.glob(folder_address + "\\*.jpg"):
            head, tail = os.path.split(img)
            image = Image.open(img)
            new_image = image.convert("L")
            tail = tail.strip(".jpg")
            new_image.save(new_address + tail + "_grayscale.png", "PNG")
        for img in glob.glob(folder_address + "\\*.npg"):
            head, tail = os.path.split(img)
            image = Image.open(img)
            new_image = image.convert("L")
            tail = tail.strip(".npg")
            new_image.save(new_address + tail + "_grayscale.png", "PNG")


