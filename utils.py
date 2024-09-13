import os


def get_version():
    version_file = "version.txt"
    if os.path.exists(version_file):
        with open(version_file, "r") as file:
            version = file.read().strip()
            if version:
                return version
    return "[development]"