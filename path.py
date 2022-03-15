import os
import sys


def get_path(db_path: str) -> str:
    """
    returns an absolut Path.
    :param db_path:
    :return:
    """
    dir_path, file_name = os.path.split(db_path)
    dir_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), dir_path))

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return os.path.join(dir_path, file_name)
