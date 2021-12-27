# env: CvEnvPython37
import cv2
import numpy as np
import PySimpleGUI as sg
import os

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

    def circular_boll(image,point,color1=(0,255,0),color2=(0,0,255)):  
        radius_c1=5
        offset_rad_c1=radius_c1+1
        radius_c2=15
        offset_rad_c2=radius_c2+10
        cv2.circle(image,point,radius_c1,color1,1)
        cv2.line(image,(point[0],point[1]+radius_c1),(point[0],point[1]+offset_rad_c1),color1,2)
        cv2.line(image,(point[0],point[1]-radius_c1),(point[0],point[1]-offset_rad_c1),color1,2)
        cv2.line(image,(point[0]+radius_c1,point[1]),(point[0]+offset_rad_c1,point[1]),color1,2)
        cv2.line(image,(point[0]-radius_c1,point[1]),(point[0]-offset_rad_c1,point[1]),color1,2)
        cv2.circle(image,point,radius_c2,color2,1)
        cv2.line(image,(point[0],point[1]+radius_c2),(point[0],point[1]+offset_rad_c2),color2,2)
        cv2.line(image,(point[0],point[1]-radius_c2),(point[0],point[1]-offset_rad_c2),color2,2)
        cv2.line(image,(point[0]+radius_c2,point[1]),(point[0]+offset_rad_c2,point[1]),color2,2)
        cv2.line(image,(point[0]-radius_c2,point[1]),(point[0]-offset_rad_c2,point[1]),color2,2)

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

#Types of images
imageTypes={'Type1':[1080,1920],
            'Type2': [1080,1080],
            'Type3': [1080,566],
            'Type4': [1080,1350],
            'Type5': [1200,630],
            'Type6': [851,315],
            'Type7': [640,480]}

#settings show Camera
cap = cv2.VideoCapture(0)
cap.set(3,imageTypes['Type2'][0])  # channel 3: windows width
cap.set(4,imageTypes['Type2'][1])  # channel 4: windows height
cap.set(10,100)                    # channel 10: Brightness of the image

#initialize infinite cycle
if cap.isOpened():
    CtrlRead, image = cap.read()
    frameGray=img_transfor(image)
    while True:
        CtrlRead, frame = cap.read()
        image=frameGray
        frameGray=img_transfor(frame)
        ImgSub=subtractor(image,frameGray)
        result_max=np.where(ImgSub==np.amax(ImgSub))
        center_img=(int(result_max[1][0]),int(result_max[0][0]))
        Center.Quadratic_Target_2(ImgSub,center_img,(255,255,255))
        Center.Center_Target(ImgSub,center_img,(255,255,255))
        cv2.imshow("Motion Detect", ImgSub)
        result_max=np.where(ImgSub==np.amax(ImgSub))
        center_img=(int(result_max[1][0]),int(result_max[0][0]))
        Center.circular_boll(frame,center_img,(255,255,255))
        cv2.imshow("cam",frame)
        key = cv2.waitKey(5)   
        if key == 27 or key==ord('q'): 
            break
folder = sg.popup_get_folder('File Name','File Search')   #4
os.chdir(folder)
cv2.imwrite("Detect_RGB.png", frame)
cv2.imwrite("Detect_Subtract.png", ImgSub)
cap.release()
cv2.destroyAllWindows()

