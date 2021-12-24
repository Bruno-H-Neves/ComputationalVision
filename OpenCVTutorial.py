import cv2

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



