# import cv2
# d=cv2.VideoCapture(0)
# i=1
# while(True):
#     ret,frame=d.read()
#     if(ret):
#         name="images/"+str(i)+'.jpg'
#         cv2.imwrite(name,frame)
#         i+=1
#         cv2.imshow('frame',frame)
#         if (cv2.waitKey(1) & 0xFF==ord('q')):
#            break
# d.release()
# cv2.distroyAllWindows()


import cv2

d= cv2.VideoCapture("abc.mp4")  
frame = d.get(cv2.CAP_PROP_FRAME_COUNT) 
t=d.get(cv2.CAP_PROP_FPS)
print(frame) 
print(t)  



# while(d.isOpened()):                 
#     ret, frame = d.read()
#     if ret==True:
#         cv2.imshow('frame',frame)       
#         if cv2.waitKey(10000) & 0xFF == ord('q'):
#             break
#     else:
#         break
# d.release()
# cv2.destroyAllWindows()