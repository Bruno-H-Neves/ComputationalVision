import cv2
import numpy as np
import matplotlib.pyplot as plt

def exit_image(title_win,img):
    while True:
        cv2.imshow(title_win, img)
        key = cv2.waitKey(1)    
        if key == 27 or key==ord('q'): 
            break


imageTypes={'Type1':[1080,1920],
            'Type2': [1080,1080],
            'Type3': [1080,566],
            'Type4': [1080,1350],
            'Type5': [1200,630],
            'Type6': [851,315],
            'Type7': [640,480]}

cap = cv2.VideoCapture(0)
#settings Camera
cap.set(3,imageTypes['Type2'][0])  # channel 3: windows width
cap.set(4,imageTypes['Type2'][1])  # channel 4: windows height
cap.set(10,100)                    # channel 10: Brightness of the image
if cap.isOpened():
    CtrlRead, frame = cap.read()
    while True:
        CtrlRead, frame = cap.read()
        cv2.imshow("WebCam", frame)
        key = cv2.waitKey(1)    
        if key == 27 or key==ord('q'): 
            break
cv2.imwrite("LastFrame.png", frame)   #Save last frame current directory
cap.release()
cv2.destroyAllWindows()

print("Image Operation")
kernel=np.ones((5,5),np.uint8) #one's matrix for using in morphologic operations
img = cv2.imread("LastFrame.png",1)
if np.shape(img) ==():
    print("Invalid Image")
title_win='Original Image  -> Press "ESC"  or "q" for exit'
exit_image(title_win,img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #RGB to Gray scale 
title_win='Gray Image  -> Press "ESC"  or "q" for exit'
exit_image(title_win,imgGray)
imgBlur_rgb = cv2.GaussianBlur(img,(7,7),0)     #Gaussian Filter
title_win='Gaussian Filter RGB Image  -> Press "ESC"  or "q" for exit'
exit_image(title_win,imgBlur_rgb)
imgBlur_gray = cv2.GaussianBlur(imgGray,(7,7),0, cv2.BORDER_TRANSPARENT)
title_win='Gaussian Filter Gray Scale Image  -> Press "ESC"  or "q" for exit'
exit_image(title_win,imgBlur_gray)
imgCanny = cv2.Canny(img, 150, 200) 
title_win='Edge Image -> Press "ESC"  or "q" for exit'
exit_image(title_win,imgCanny)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) 
title_win='Dilate Edge Image -> Press "ESC"  or "q" for exit'
exit_image(title_win,imgDialation)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
title_win='Erode Dilated Image -> Press "ESC"  or "q" for exit'
exit_image(title_win,imgEroded)
gray_eq = cv2.equalizeHist(imgGray)
title_win='Gray Image Equalize -> Press "ESC"  or "q" for exit'
exit_image(title_win,gray_eq)

#version 1.2:  Histogram
hist = cv2.calcHist(imgBlur_gray, [0], None, [256], [0, 256])
hist_norm= hist/hist.sum()
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.subplot(1,2,2)
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel(r"% of Pixels")
plt.plot(hist_norm)
plt.xlim([0, 256])
plt.show()

cv2.destroyAllWindows()






