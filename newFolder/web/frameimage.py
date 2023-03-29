import cv2
d=cv2.VideoCapture(0)
while(True):
    ret,frame=d.read()
    cv2.imshow('frame',frame)
    if (cv2.waitKey(1) & 0xFF==ord('q')):
        break
cv2.release()
cv2.distroyAllwindows()