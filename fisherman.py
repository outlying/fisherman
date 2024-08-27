import logging
import math
import time

import cv2
import numpy as np
from matplotlib import pyplot as plt

from finder.finder import Finder
from gui_io.operator import Operator
from observer.observer import Observer
from utils import run_with_timeout

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Fisherman:

    def __init__(self, operator: Operator, finder: Finder, observer: Observer):
        self.operator = operator
        self.finder = finder
        self.observer = observer
        logger.info("Fisherman initialized.")

    def fish(self):

        fishing_start_time = None
        areas = list()
        logger.info("Starting the fishing cast.")

        while len(areas) != 1:

            see_before_throw = self.operator.see()
            logger.debug("Throwing the bobber.")
            self.operator.throw()
            fishing_start_time = time.time()
            self.operator.wait(2.2)
            see_after_throw = self.operator.see()

            logger.info("Finding bobber based on the images before and after throw.")
            areas = self.finder.find_bobber(see_before_throw, see_after_throw)

            if len(areas) <= 0:
                logger.warning("No bobber found, aborting fishing. Starting another attempt")
            if len(areas) > 1:
                logger.warning(f"Multiple bobber found ({len(areas)} areas) at: {areas}, attempting again")

            if len(areas) != 1:
                self.operator.abort_fishing()
                self.operator.wait(3)

        area = areas[0]

        logger.info(f"Bobber found in area: {area}")

        timeout = max(fishing_start_time + 22 - time.time(), 0)
        logger.info(f"Waiting {timeout}s for the fish")
        result = run_with_timeout(self.observer.observe, timeout, area)

        if result:
            logger.info("Fish spotted, reel in.")
        else:
            logger.info("We missed the fish. Our observer did not detect anything.")


        def get_center(area):
            return area[0] + area[2] / 2, area[1] + area[3] / 2
        center = get_center(areas[0])
        self.operator.get_fish_at(center[0], center[1])

        # print(areas)
        #
        # bobber_detected_img = np.array(see_after_throw).copy()
        # for area in areas:
        #     x, y, w, h = area
        #     cv2.rectangle(bobber_detected_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # plt.figure(figsize=(10, 6))
        # plt.title("Detected Bobber")
        # plt.imshow(bobber_detected_img)
        # plt.axis('off')
        # plt.show()

        logger.info("We are done.")

