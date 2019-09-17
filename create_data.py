import os
import cv2

face_cascade = cv2.CascadeClassifier(os.getcwd()+'\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

path = str(os.getcwd()+'\datasets')
id = input("USER_NAME:\t")

try:
    os.mkdir(path+"\\"+str(id))
    print("Directory ", path+str(id) , "successfully created !")
except FileExistsError:
    print("User name taken!!")

count=0


while True:
    ret, img = cap.read()
    frame= img.copy()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        count = count+1
        cv2.imwrite(path+"\\"+str(id)+'\\'+str(count)+ ".jpg", gray[y:y+h,x:x+w])

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100)

        cv2.imshow('img',img)

        cv2.waitKey(1)

        if count>10:
            break

cap.release()
cv2.destroyAllWindows()
