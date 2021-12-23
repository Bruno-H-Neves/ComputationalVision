import cv2

cap = cv2.VideoCapture(0)

while True:
    CtrlRead, img = cap.read()
    print(CtrlRead)
    cv2.imshow("Video", img)
    key = cv2.waitKey(1)    
    if key == 27 or key==ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()