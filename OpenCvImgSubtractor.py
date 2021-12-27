# env: CvEnvPython37
import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pytz
import psutil


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

