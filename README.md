# Face-Recognition
 An attempt at building a face recognition program with the help of OpenCV.
 
 To be honest the heavy lifting has been done by OpenCV itself and in this project I have only utilised the tools already available to build something useful

### 3 STEP PROCESS

* **CREATE DATA**
* **TRAIN MODEL**
* **RECOGNITION**

### STEP 1 : CREATING THE DATASET


First of all we need to create labelled dataset so that the model can refer to it for labelling new faces it encounters; this is handled by the *create_data* script

* just run the script and user will be prompted to provide a name (a unique label to classify the observed face as!)
* upon entry of a unique name for the face a preview screen will pop up display the camera view with the face enclosed in a box.
* at this poiint the script is recording images of the face detected, stop after sometime (20 seconds of waiting is more than enough)
* in the end simply close the script.

At the end of this step you will find that images of your face have been captured and saved in the ./dataset/<your-username> directory

### STEP 2 : TRAINING MODEL AND GENERATING THE FEATURE SET

Now that we have sufficient data about ( prefferably multiple ) individual faces we go ahead to train our model so that the distinguishing features of the faces can be extracted.

* in this step we simply run the *train_model.py* script, which in the end generates a pickle dump (consider pickle as a format to store data)

* simply run the script and you will find the images being analysed and data stored in ./encodings/encoding.pickle (all the faces are stored in the same pickle file)



### STEP 3 : TESTING YOUR MODEL

Since the model has trained itself and now knows about the facial data of some individuals. You can try to test it's capability by running the *recognition.py* script

* the  user will get a preview of the camera view with the faces detected being in a box with <predicted-username> on top







### resource utilised:
    -> OpenCV ( https://github.com/opencv/opencv )
    -> Face_Recognition ( https://github.com/ageitgey/face_recognition )