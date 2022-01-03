

import cv2

cap = cv2.VideoCapture(0)
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
