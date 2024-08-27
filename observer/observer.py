from abc import ABC, abstractmethod

import numpy as np
from PIL.Image import Image
from PIL import ImageChops

from gui_io.operator import Operator


class Observer(ABC):

    @abstractmethod
    def observe(self, area):
        pass

class StandardObserver(Observer):

    def __init__(self, operator: Operator):
        self.operator = operator

    def observe(self, area):
        previous = None
        while True:
            current = self.operator.see_area(area)

            if previous:
                change_value = self.calculate_change(previous, current)
                if change_value > 0.03:
                    return True

            previous = current


    @staticmethod
    def calculate_change(img1: Image, img2: Image):
        # Convert images to grayscale
        img1_gray = img1.convert('L')
        img2_gray = img2.convert('L')

        # Compute the difference image
        diff = ImageChops.difference(img1_gray, img2_gray)

        # Calculate the RMS (Root Mean Square) error between the images
        diff_np = np.array(diff)
        rms = np.sqrt(np.mean(diff_np ** 2))

        # Normalize RMS by the maximum possible value (255)
        rms_normalized = rms / 255.0

        return rms_normalized