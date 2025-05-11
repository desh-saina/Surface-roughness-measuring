from matplotlib import pyplot as plt
import cv2

# Plotting the histogram of grayscale levels

def gray_level_histogram(gray_levels, frequencies, img):
    """ get gray_levels and frequencies from roughness.py corresponding to image 'img' """

    plt.plot(gray_levels, frequencies)
    plt.xlabel('Grey levels')
    plt.ylabel('Pixel frequency')
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    plt.show()