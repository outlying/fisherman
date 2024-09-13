import logging
import os

from utils import resource_path

logger = logging.getLogger("Version")

def get_version():
    version_file = resource_path("version.txt")
    if os.path.exists(version_file):
        with open(version_file, "r") as file:
            version = file.read().strip()
            if version:
                return version
    logger.info("No version file found, this is development version")
    return "[development]"