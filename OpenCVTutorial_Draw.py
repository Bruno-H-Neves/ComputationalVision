import cv2
import numpy as np
import time
import datetime
import pytz

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
        cv2.rectangle(image,(int(row*0.8),0),(int(row),20),(100,100,100),cv2.FILLED)
        cv2.rectangle(image,(int(row*0.6),0),(int(row*0.8),20),(0,0,0),cv2.FILLED)
        cv2.putText(image,date,(int(row*0.615),15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,255,50),1)
        cv2.putText(image,hour,(int(row*0.85),15),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,255,50),1)
        pass

img = cv2.imread("LastFrame.png")
linhas=img.shape[0]
colunas=img.shape[1]
print(linhas)
print(colunas)
center_img=(int(colunas/2),int(linhas/2))
print(center_img)
texto=str(img.shape[0]) + str(img.shape[1])
print(img.shape)
Header.leftH(img)
Center.Center_Target(img,center_img,(0,255,0))
Center.Quadratic_Target_1(img,center_img,(0,255,255))
Center.Quadratic_Target_2(img,center_img,(0,0,255))
Center.Circular_Target_2(img,center_img,(255,0,0))
Center.Circular_Target_center(img,center_img,(0,0,0))


cv2.imshow("img", img)
cv2.waitKey(0)
