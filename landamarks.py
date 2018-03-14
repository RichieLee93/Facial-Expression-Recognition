import cv2
import numpy as np
import dlib
import pandas as pd
import csv

import datetime

starttime = datetime.datetime.now()
def get_landmark(path):
    image_path = path
    # Create the haar cascade
    faceCascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # create the landmark predictor
    predictor =  dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    image = cv2.imread(image_path)
    #resizing according to the image, done manually for instance
    # image = cv2.resize(image, (1000,700))

    # convert the image to grayscale
    # gray1= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray2 = cv2.equalizeHist(gray1)
    # gray = cv2.normalize(gray2,1, alpha = 0,beta=255, norm_type=cv2.NORM_MINMAX)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        # gray,
        image,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    #print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    position =[]
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


    # Converting the OpenCV rectangle coordinates to Dlib rectangle
        dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

        detected_landmarks = predictor(image, dlib_rect).parts()

        landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])

        # print landmarks

        for idx, point in enumerate(landmarks):
            pos = (point[0, 0], point[0, 1])
            cv2.circle(image,pos,2, color=(0, 0, 255),thickness=3)

            position.append(pos)
            font = cv2.FONT_HERSHEY_SIMPLEX

    # cv2.waitKey(0)

    return position
    # pixel = image[position[0][0],position[0][1]]
#end def


def generate_landmarks():


    csvfile = open('data/data.csv','r')
    data = []
    landmarks_list = []
    full_data_list = []
    for line in csvfile:
        data.append(list(line.split(',')))
    for d in data:
        full = []
        landmarks = get_landmark(d[1].strip())
        print(landmarks)
        endtime = datetime.datetime.now()

        #print (endtime - starttime)
        landmarks_list.append(landmarks[:68])
        for l in landmarks[:68]:
            full.append(l[0])
            full.append(l[1])
        full_data_list.append(full)


    return landmarks_list,full_data_list
#end def



# h = ['a','b']
# d= pd.read_csv('data/data.csv',sep=',',names=h)
# d['c'] = generate_landmarks()
# d.to_csv('data/data_with_landmarks.csv',header=False,index=False)


#with open('data/landmarks.csv','w') as f:
    #writer = csv.writer(f)
    #writer.writerows(generate_landmarks())
landmark_data, full_data = generate_landmarks()

#with open('data/fulldata.csv','w') as f:
 #   writer = csv.writer(f)
  #  writer.writerows(full_data)
