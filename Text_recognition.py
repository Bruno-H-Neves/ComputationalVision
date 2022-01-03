import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
cap = cv2.VideoCapture(0)

if cap.isOpened():
    CtrlRead, frame = cap.read()
    while True:
        CtrlRead, frame = cap.read()
        hei_fr= frame.shape[0]
        detect=pytesseract.image_to_boxes(frame)
        for box in detect.splitlines():
            box=box.split(' ')
            x,y,w,h= int(box[1]),int(box[2]),int(box[3]),int(box[4])
            cv2.rectangle(frame,(x,hei_fr-y),(w,hei_fr-h),(0,0,255),1)
            cv2.putText(frame,box[0],(x,hei_fr-y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0),1)
        cv2.imshow("WebCam", frame)
        key = cv2.waitKey(1)   
        if key == 27 or key==ord('q'): 
            break
cv2.imwrite("LastFrame.png", frame)   #Save last frame current directory
cap.release()
cv2.destroyAllWindows()



##detecting words digits
cap = cv2.VideoCapture(0)
cong=r'--oem 3 --psm 6 outputbase digits'

if cap.isOpened():
    CtrlRead, frame = cap.read()
    while True:
        CtrlRead, frame = cap.read()
        hei_fr= frame.shape[0]
        detect=pytesseract.image_to_data(frame,config=cong)
        for index,box in enumerate(detect.splitlines()):
            if index!=0:
                box=box.split(' ')
                if len(box)==12:
                    x,y,w,h= int(box[6]),int(box[7]),int(box[8]),int(box[9])
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
                    cv2.putText(frame,box[-1],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0),1)
            
        cv2.imshow("WebCam", frame)
        key = cv2.waitKey(1)   
        if key == 27 or key==ord('q'): 
            break
cv2.imwrite("LastFrame_digits.png", frame)   #Save last frame current directory
cap.release()
cv2.destroyAllWindows()
