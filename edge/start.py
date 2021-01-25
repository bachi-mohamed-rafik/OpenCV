"""
Loads and displays a video.
"""

#Imports

import cv2
import numpy as np

#read video
cap = cv2.VideoCapture('videos/A 015.mp4')

# Camera opened successfuly
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

#read
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Converting the image to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Frame', gray)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('a'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

