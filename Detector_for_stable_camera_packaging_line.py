import cv2
import numpy as np
import PySimpleGUI as sg
import os

def img_transfor(imgTransform):
    n=5
    imgTransform = cv2.cvtColor(imgTransform, cv2.COLOR_RGB2GRAY)
    #LB Filter    
    kernel = np.ones((n,n),np.float32)/25
    imgTransform = cv2.filter2D(imgTransform,-1,kernel)                # 2D Convolution
    return imgTransform

def subtractor(img1,img2,thr=150):
    ImgSub=abs(img1-img2)
    ImgSub =(ImgSub<thr)*ImgSub
    return ImgSub



cap = cv2.VideoCapture(0)

if cap.isOpened():
    CtrlRead, image = cap.read()
    frameGray=img_transfor(image)
    frameGray=frameGray[200:400, 100:500]
    while True:
        ret, frame=cap.read()
        image_draw=frame[200:400, 100:500]
        image=frameGray
        frameGray=img_transfor(frame)
        frameGray =frameGray[200:400, 100:500] 
        ImgSub=subtractor(image,frameGray)
        mask=ImgSub
        _, mask = cv2.threshold(mask, 50, 100, cv2.THRESH_BINARY)                       #Fine tune
        contours, _ =cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        detections =[]
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100 and area <1000:               #remove element out of limits: Fine tune
                cv2.drawContours(image_draw, [cnt], -1, (0,255,0), 2)
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(image_draw, (x, y),((x+w),(y+h)), (0, 255, 255), 1)
                detections.append([x, y, w, h])

    
        cv2.imshow("original",frame)
        cv2.imshow("Region of interess",image_draw)
        cv2.imshow("Subtrator",mask)
        key = cv2.waitKey(5)   
        if key == 27 or key==ord('q'): 
            break
folder = sg.popup_get_folder('Folder Name','Folder Search')   #4
os.chdir(folder)
cv2.imwrite("Detect_RGB.png", frame)
cv2.imwrite("ROI.png",image_draw )
cv2.imwrite("Detect_Subtract.png", ImgSub)
cap.release()
cv2.destroyAllWindows()
