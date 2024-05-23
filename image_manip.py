from glob import glob
import os
import sys
from PIL import Image
from rembg import remove
from enum import StrEnum, auto


class ImageTypes(StrEnum):
    JPG: str = auto()
    JPEG: str = auto()
    PNG: str = auto()
    ICO: str = auto()
    WEBP: str = auto()
    BLP1: str = auto()
    BLP2: str = auto()
    BMP: str = auto()
    DIB: str = auto()
    EPS: str = auto()
    GIF: str = auto()
    ICNS: str = auto()
    IM: str = auto()
    JFIF: str = auto()
    JPX: str = auto()
    J2K: str = auto()
    JP2: str = auto()
    MSP: str = auto()
    PCX: str = auto()
    PFM: str = auto()
    PPM: str = auto()
    PBM: str = auto()
    PGM: str = auto()
    PNM: str = auto()
    SGI: str = auto()
    SPIDER: str = auto()
    TGA: str = auto()
    TIFF: str = auto()
    XBM: str = auto()
    PDF: str = auto()


class OutputOnlyImageTypes(StrEnum):
    PDF: str = auto()


def glob_image_paths(source: str) -> list[str]:
    img_paths: list[str] = []

    img_types = set(ImageTypes).difference(set(OutputOnlyImageTypes))

    for img_type in img_types:
        # Build path for glob
        path: str = os.path.join(source, f"*.{img_type}")
        # Add files to list
        img_paths.extend(glob(path))

    return img_paths


def image_conversion(source: str, destination: str, conversion: ImageTypes) -> None:
    # Retreive all paths to image files
    img_paths: list[str] = glob_image_paths(source)

    # Create destination directory, if necessary
    if img_paths and not os.path.exists(destination):
        os.mkdir(destination)

    for idx, img_path in enumerate(img_paths, 0):

        save_path = os.path.join(destination, f"logo{idx}.{conversion}")

        with Image.open(img_path, "r") as image:
            image.save(save_path)


def remove_background(source: str, destination: str) -> None:
    # Retreive all paths to image files
    img_paths: list[str] = glob_image_paths(source)

    # Create destination directory, if necessary
    if img_paths and not os.path.exists(destination):
        os.mkdir(destination)

    for idx, img_path in enumerate(img_paths, 0):
        file_name, file_type = os.path.splitext(img_path)
        save_path = os.path.join(destination, f"logo{idx}.{file_type}")

        # Open image
        with Image.open(img_path, "r") as image:
            remb_image: Image.Image = remove(image)

            remb_image.save(save_path)
