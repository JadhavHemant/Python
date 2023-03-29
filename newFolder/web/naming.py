import cv2
d=cv2.VideoCapture("abc.mp4")
i=1
while(True):
    ret,frame=d.read()
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'wel-come',(50,45),font,1,(0,287,255),2,cv2.LINE_4)
    cv2.imshow('frame',frame)
    if (cv2.waitKey(1) & 0xFF==ord('q')):
           break
d.release()
cv2.distroyAllWindows() 