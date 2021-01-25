# Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Image
img=cv2.imread('images/A_007.png',1)
img=cv2.resize(img,(500,500))


def dodgeV2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)

def blend(front,back):
    result=front*255/(255-back)  
    result[result>255]=255 
    result[back==255]=255 
    return result

def render(img_rgb):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        
    #Applying gaussian blur to grayscale image
    img_blur = cv2.GaussianBlur(img_gray, (21,21), 0, 0)
    
    #Invert the blur image
    inverted_img = 255 - img_blur
    
    #Apply the dodgeV2 function
    img_blend = dodgeV2(img_gray,inverted_img)
    
    #Blend the image
    img_final = 1-blend(img_blend,img_gray)

    return img_final



final_image = render(img)




cv2.imshow("Title",final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('output_img.png', (final_image))


