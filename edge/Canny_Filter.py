#Imports

import cv2
import numpy as np

#read image

img=cv2.imread('images/A_007.png',1)
img=cv2.resize(img,(500,500))

'''
cv2.imshow("Title",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Converting image to grayscale
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

'''
cv2.imshow("Title",grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Canny filter
edges1=cv2.Canny(grayscale,10,10)
'''
cv2.imshow("Title",edges1)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

edges2=cv2.Canny(grayscale,100,100)
'''
cv2.imshow("Title",edges2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# stacking images to compare them
images=np.hstack((grayscale,edges1,edges2))
cv2.imshow('im', images)
cv2.waitKey(0)
cv2.destroyAllWindows()


