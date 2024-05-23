import sys
import os
from image_manip import image_conversion, ImageTypes


def parse_args(args: list[str]) -> dict[str, str]:
    """Parses command-line arguments.

    Args:
        args (list[str]): Command line arguments for the script.

    Raises:
        Exception: Raises exception for invalid or improperly formatted arguments.

    Returns:
        dict[str, str]: Dictionary of parsed arguments.
    """
    arg_list = args[1:]

    try:
        src: str = os.path.abspath(arg_list[0])
        dest: str = os.path.abspath(arg_list[1])
        conversion = arg_list[2]

        if not conversion in ImageTypes:
            raise Exception("Not a valid image file type.")

    except:
        raise Exception(
            "Improperly formatted arguments. Specify source directory,"
            "destination directory, and new image type."
        )

    return {"source": src, "destination": dest, "conversion": conversion}


args: dict[str, str] = parse_args(sys.argv)

source: str = args["source"]
destination: str = args["destination"]
conversion: str = args["conversion"]

image_conversion(source, destination, conversion)
