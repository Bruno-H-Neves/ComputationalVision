import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pytz
import psutil

def exit_image(title_win,img):
    while True:
        cv2.imshow(title_win, img)
        key = cv2.waitKey(1)    
        if key == 27 or key==ord('q'): 
            break
    cv2.destroyAllWindows()

class Center():
    def __init__(self):
        pass

    def Center_Target(image,point,color1=(255,0,0)):
        cv2.line(image,(point[0]-50,point[1]),(point[0]+50,point[1]),color1,1)
        cv2.line(image,(point[0],point[1]-50),(point[0],point[1]+50),color1,1)

    def Quadratic_Target_1(image,point,color2=(255,0,0)):
        cv2.line(image,(point[0]-10,point[1]-3),(point[0]-10,point[1]+3),color2,1)
        cv2.line(image,(point[0]+10,point[1]-3),(point[0]+10,point[1]+3),color2,1)
        cv2.line(image,(point[0]-3,point[1]-10),(point[0]+3,point[1]-10),color2,1)
        cv2.line(image,(point[0]-3,point[1]+10),(point[0]+3,point[1]+10),color2,1)

    def Quadratic_Target_2(image,point,color2=(255,0,0)):
        cv2.line(image,(point[0]-10,point[1]-10),(point[0]-10,point[1]-7),color2,1)
        cv2.line(image,(point[0]+10,point[1]-10),(point[0]+10,point[1]-7),color2,1)
        cv2.line(image,(point[0]-10,point[1]+7),(point[0]-10,point[1]+10),color2,1)
        cv2.line(image,(point[0]+10,point[1]+7),(point[0]+10,point[1]+10),color2,1)
        cv2.line(image,(point[0]-10,point[1]-10),(point[0]-7,point[1]-10),color2,1)
        cv2.line(image,(point[0]+10,point[1]-10),(point[0]+7,point[1]-10),color2,1)
        cv2.line(image,(point[0]-10,point[1]+10),(point[0]-7,point[1]+10),color2,1)
        cv2.line(image,(point[0]+10,point[1]+10),(point[0]+7,point[1]+10),color2,1)
    
    def Circular_Target_2(image,point,color=(255,0,0)):    
        cv2.circle(image,point,20,color,1)

    def Circular_Target_center(image,point,color=(255,0,0)):    
        cv2.circle(image,point,2,color,1)

class Header():
    def __init__(self):
        pass

    def leftH(image, color=(0,0,0)):
        row=image.shape[1]
        col=image.shape[0]
        dt_now = datetime.datetime.now(tz= pytz.UTC)
        date=r'%s-%s-%s' %(dt_now.day,dt_now.month,dt_now.year)
        hour=r'%s:%s:%s' %(dt_now.hour,dt_now.minute,dt_now.second) 
        used_ram='Ram: %s'%(str(psutil.virtual_memory().used))
        battery = psutil.sensors_battery()
        bat_percent ='Bat: %s '%(str(battery.percent))
        cv2.rectangle(image,(int(row*0.8),0),(int(row),20),(100,100,100),cv2.FILLED)
        cv2.rectangle(image,(int(row*0.6),0),(int(row*0.8),20),(0,0,0),cv2.FILLED)
        cv2.rectangle(image,(int(row*0.29),0),(int(row*0.6),20),(250,100,150),cv2.FILLED)
        cv2.rectangle(image,(0,0),(int(row*0.29),20),(100,100,100),cv2.FILLED)
        cv2.putText(image,date,(int(row*0.615),15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,255,50),1)
        cv2.putText(image,hour,(int(row*0.85),15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,255,50),1)
        cv2.putText(image,used_ram,(int(row*0.295),15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,0,50),1)
        cv2.putText(image,bat_percent,(0,15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,0,50),1)
        
        pass

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
        img=frame
        linhas=img.shape[0]
        colunas=img.shape[1]
        center_img=(int(colunas/2),int(linhas/2))
        Header.leftH(img)
        Center.Center_Target(img,center_img,(0,255,0))
        Center.Quadratic_Target_1(img,center_img,(0,255,255))
        Center.Quadratic_Target_2(img,center_img,(0,0,255))
        Center.Circular_Target_2(img,center_img,(255,0,0))
        Center.Circular_Target_center(img,center_img,(0,0,0))

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
title_win='Original Image  -> Press "ESC"  or "q" to continue'
exit_image(title_win,img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #RGB to Gray scale 
title_win='Gray Image  -> Press "ESC"  or "q" to continue'
exit_image(title_win,imgGray)
imgBlur_rgb = cv2.GaussianBlur(img,(7,7),0)     #Gaussian Filter
title_win='Gaussian Filter RGB Image  -> Press "ESC"  or "q" to continue'
exit_image(title_win,imgBlur_rgb)
imgBlur_gray = cv2.GaussianBlur(imgGray,(7,7),0, cv2.BORDER_TRANSPARENT)
title_win='Gaussian Filter Gray Scale Image  -> Press "ESC"  or "q" to continue'
exit_image(title_win,imgBlur_gray)
imgCanny = cv2.Canny(img, 150, 200) 
title_win='Edge Image -> Press "ESC"  or "q" to continue'
exit_image(title_win,imgCanny)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) 
title_win='Dilate Edge Image -> Press "ESC"  or "q" to continue'
exit_image(title_win,imgDialation)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
title_win='Erode Dilated Image -> Press "ESC"  or "q" to continue'
exit_image(title_win,imgEroded)
gray_eq = cv2.equalizeHist(imgGray)
title_win='Gray Image Equalize -> Press "ESC"  or "q" to continue'
exit_image(title_win,gray_eq)
imgHor = np.hstack((gray_eq,imgBlur_gray))
title_win='Dual Gray Image-> Press "ESC"  or "q" to continue'
exit_image(title_win,imgHor)

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
#version 1.3
imgResize = cv2.resize(img,(imageTypes['Type3'][0],imageTypes['Type3'][1])) # para definir nova dimensao da imagem
width, height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)    #rotacao de uma matriz
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
imgCropped = img[0:200, 200:500]
cv2.imshow("Original Image", img)
cv2.imshow("Resize Image", imgResize)
cv2.imshow("Crop Image", imgCropped)
cv2.imshow("Warm prespective", imgOutput)

cv2.waitKey(0)










