# USAGE
# python /home/nmorales/cxgn/DroneImageScripts/VegetativeIndex/VARI.py --image_path /folder/mypic.png --outfile_path /export/mychoppedimages/tgi.png

# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np
import math

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image_path", required=True, help="image path")
ap.add_argument("-o", "--outfile_path", required=True, help="file path where the output will be saved")
args = vars(ap.parse_args())

input_image = args["image_path"]
outfile_path = args["outfile_path"]

img = cv2.imread(input_image)
b,g,r = cv2.split(img)

numerator = g - r
denominator = g + r - b
tgi = cv2.divide(numerator, denominator)

cv2.imwrite(outfile_path, tgi)
