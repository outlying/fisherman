from abc import abstractmethod, ABC

import PIL.Image
import cv2
import numpy as np
from matplotlib import pyplot as plt


class Finder(ABC):

    @abstractmethod
    def find_bobber(self, before_img, after_img):
        pass

class StandardFinder(Finder):

    def __init__(self):
        bobber_img = cv2.imread("bobber.png", cv2.IMREAD_UNCHANGED)
        self.bobber_gray = cv2.cvtColor(bobber_img, cv2.COLOR_BGR2GRAY)

    def find_bobber(self, before_img, after_img):

        before_img = np.array(before_img)
        after_img = np.array(after_img)
        PIL.Image.fromarray(after_img).save("ccc.png")

        # Convert to grayscale
        before_gray = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)
        bobber_gray = self.bobber_gray

        # Calculate the absolute difference between the images
        diff = cv2.absdiff(before_gray, after_gray)

        # Apply a threshold to highlight the differences
        _, thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around detected contours
        bobber_detected_img = after_img.copy()
        for contour in contours:
            # Filter out small contours that are unlikely to be the bobber
            if cv2.contourArea(contour) > 50:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(bobber_detected_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Convert image to RGB for displaying using matplotlib
        bobber_detected_img_rgb = cv2.cvtColor(bobber_detected_img, cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(10, 6))
        plt.title("Detected Bobber")
        plt.imshow(bobber_detected_img_rgb)
        plt.axis('off')
        plt.show()
        pass


class TemplateFinder(Finder):

    def __init__(self):
        self.bobber_img = cv2.imread("bobber.png", cv2.IMREAD_UNCHANGED)
        self.bobber_gray = cv2.cvtColor(self.bobber_img, cv2.COLOR_BGR2GRAY)

    def find_bobber(self, before_img, after_img):

        # Load the images
        bobber_img_path = 'bobber.png'

        before_img = np.array(before_img)
        after_img = np.array(after_img)
        bobber_img = cv2.imread(bobber_img_path, cv2.IMREAD_UNCHANGED)

        # Convert the after image to HSV for better color segmentation
        hsv_after = cv2.cvtColor(after_img, cv2.COLOR_BGR2HSV)

        # Define the HSV range for red color
        # Red in HSV has two ranges, due to the circular nature of the hue component in HSV
        lower_red1 = np.array([0, 70, 50])
        upper_red1 = np.array([10, 255, 255])

        lower_red2 = np.array([170, 70, 50])
        upper_red2 = np.array([180, 255, 255])

        # Create masks for the red color in both hue ranges
        mask_red1 = cv2.inRange(hsv_after, lower_red1, upper_red1)
        mask_red2 = cv2.inRange(hsv_after, lower_red2, upper_red2)

        # Combine the masks
        mask_red = cv2.bitwise_or(mask_red1, mask_red2)

        # Perform morphological operations to remove noise
        kernel = np.ones((5, 5), np.uint8)
        mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
        mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)

        # Use the red mask to extract the potential bobber region
        result_red = cv2.bitwise_and(after_img, after_img, mask=mask_red)

        # Convert the result to grayscale and apply edge detection to refine the bobber location
        gray_result_red = cv2.cvtColor(result_red, cv2.COLOR_BGR2GRAY)
        edges_red = cv2.Canny(gray_result_red, 50, 150)

        # Find contours in the edge-detected image
        contours_red, _ = cv2.findContours(edges_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around the contours that match the bobber's approximate size
        detected_img_red = after_img.copy()
        for cnt in contours_red:
            x, y, w, h = cv2.boundingRect(cnt)
            if 20 < w < 50 and 20 < h < 50:  # The bobber's approximate size
                cv2.rectangle(detected_img_red, (x, y), (x + w, y + h), (0, 255, 0), 2)



        # Display the result
        plt.figure(figsize=(10, 10))
        plt.imshow(cv2.cvtColor(detected_img_red, cv2.COLOR_BGR2RGB))
        plt.title('Bobber Detection Focusing on Red Color')
        plt.show()