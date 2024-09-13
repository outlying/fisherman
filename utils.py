import os
import sys


def resource_path(relative_path):
    """ Get the absolute path to a resource, works for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)