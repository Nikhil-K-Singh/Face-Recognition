import cv2,os
from imutils import paths

import face_recognition
import pickle

dataset = str(os.getcwd()+"\\datasets\\")
module = str(os.getcwd()+"\\encodings\\encoding.pickle")

imagepaths = list(paths.list_images(dataset))
Encodings=[]
Names=[]

for (i,image_path) in enumerate(imagepaths):
    print("[INFO]  processing image{}/{}".format(i+1,len(imagepaths)))
    name = image_path.split(os.path.sep)[-2]
    image = cv2.imread(image_path)
    rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb,model="hog")
    encodings = face_recognition.face_encodings(rgb,boxes)

    for encoding in encodings:
        Encodings.append(encoding)
        Names.append(name)

        print("[INFO]  serializing encodings...")
        data={"encodings":Encodings,"names":Names}
        output= open(module,"wb")
        pickle.dump(data,output)
        output.close()  
