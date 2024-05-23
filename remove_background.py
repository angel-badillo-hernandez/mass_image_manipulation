import sys
import os
from image_manip import remove_background, ImageTypes


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

    except:
        raise Exception(
            "Improperly formatted arguments. Specify source directory,"
            "destination directory, and new image type."
        )

    return {"source": src, "destination": dest}

args: dict[str, str] = parse_args(sys.argv)

source: str = args["source"]
destination: str = args["destination"]

remove_background(source, destination)