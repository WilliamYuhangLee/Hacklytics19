import numpy as np
from PIL import Image
from os import path, mkdir, listdir


def convert_png_to_nparray(filepath, resize=()):

    image = Image.open(filepath)
    if resize is not ():
        image = image.resize(resize, Image.NEAREST)
        print("Not None")
        image.load()
    return np.asarray(image)


def convert_folder(folder_name):
    """
    Convert a folder of PNG images to a numpy array

    :param folder_name: the name of the folder, e.g. "B0001"
    :return: a numpy array of dimension (number of images, x, y)
    """

    if not path.isdir("data/preprocessed"):
        mkdir("data/preprocessed")
    elif path.isfile(path.join("data/preprocessed", folder_name + ".npz")):
        return np.load("data/preprocessed/{}.npz".format(folder_name))["data"]

    dirpath = "data/baggages/" + folder_name
    files = []
    for file in listdir(dirpath):
        filepath = path.join(dirpath, file)
        if file.endswith(".png") and path.isfile(filepath):
            files.append(filepath)
    arr = np.stack((convert_png_to_nparray(file) for file in files))
    np.savez("data/preprocessed/{}.npz".format(folder_name), data=arr)
    return arr
