import csv
import re
import cv2
import dlib
import pandas as pd
import datetime

starttime = datetime.datetime.now()

def textual_position(path):
    data = []
    reader = csv.reader(open(path))
    for row in reader:
        data.append(row)
    geo_features_list = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            vec = re.split('\,|\(|\)', data[i][j])
            tuple_new = (int(vec[1]), int(vec[2]))
            data[i][j] = tuple_new

    textual_position_list = []
    for d in data:
        textual_position = []
        for i in range(0,17):
            m1 = d[i]
            m2 = (d[i][0]-2,d[i][1]+2)
            m3 = (d[i][0]-2,d[i][1]+1)
            m4 = (d[i][0]-2,d[i][1])
            m5 = (d[i][0]-1,d[i][1]-2)
            m6 = (d[i][0],d[i][1]-2)
            m7 = (d[i][0]+1,d[i][1]-2)
            m8 = (d[i][0]+2,d[i][1])
            m9 = (d[i][0]+2,d[i][1]+1)
            m10 =(d[i][0]+2,d[i][1]+1)
            textual_position.append(m1)
            textual_position.append(m2)
            textual_position.append(m3)
            textual_position.append(m4)
            textual_position.append(m5)
            textual_position.append(m6)
            textual_position.append(m7)
            textual_position.append(m8)
            textual_position.append(m9)
            textual_position.append(m10)

        for i in range(17,22):
            m1 = d[i]
            m2 = (d[i][0] - 2, d[i][1] -1)
            m3 = (d[i][0] +1, d[i][1])
            m4 = (d[i][0] + 2, d[i][1] -1)

            textual_position.append(m1)
            textual_position.append(m2)
            textual_position.append(m3)
            textual_position.append(m4)

        for i in range(22, 27):
            m1 = d[i]
            m2 = (d[i][0] -2, d[i][1]-1)
            m3 = (d[i][0] - 1, d[i][1])
            m4 = (d[i][0] + 2, d[i][1] -1)

            textual_position.append(m1)
            textual_position.append(m2)
            textual_position.append(m3)
            textual_position.append(m4)


        for i in range(27, 36):
            m1 = d[i]
            m2 = (d[i][0], d[i][1] + 1)
            m3 = (d[i][0] , d[i][1] + 2)
            m4 = (d[i][0] - 2, d[i][1])
            m5 = (d[i][0] - 1, d[i][1] - 1)
            m6 = (d[i][0], d[i][1] - 1)
            m7 = (d[i][0] + 1, d[i][1] - 1)
            m8 = (d[i][0] + 2, d[i][1])

            textual_position.append(m1)
            textual_position.append(m2)
            textual_position.append(m3)
            textual_position.append(m4)
            textual_position.append(m5)
            textual_position.append(m6)
            textual_position.append(m7)
            textual_position.append(m8)

        for i in range(36, 48):
            m1 = d[i]
            m2 = (d[i][0] - 2, d[i][1])
            m3 = (d[i][0] - 2, d[i][1] + 1)
            m4 = (d[i][0] , d[i][1]+1)
            m5 = (d[i][0] + 1, d[i][1] +1)
            m6 = (d[i][0]+2, d[i][1] )
            m7 = (d[i][0] + 1, d[i][1] - 1)
            m8 = (d[i][0] , d[i][1]-1)

            textual_position.append(m1)
            textual_position.append(m2)
            textual_position.append(m3)
            textual_position.append(m4)
            textual_position.append(m5)
            textual_position.append(m6)
            textual_position.append(m7)
            textual_position.append(m8)

        for i in range(48, 68):
            m1 = d[i]
            m2 = (d[i][0] - 2, d[i][1] )
            m3 = (d[i][0] - 1, d[i][1] + 1)
            m4 = (d[i][0] , d[i][1]+1)
            m5 = (d[i][0] + 1, d[i][1] + 1)
            m6 = (d[i][0]+2, d[i][1])
            m7 = (d[i][0] + 1, d[i][1] - 1)
            m8 = (d[i][0], d[i][1]-1)
            m9 = (d[i][0] -1, d[i][1] - 1)
            m10 = (d[i][0] - 1, d[i][1] + 2)
            m11 = (d[i][0] , d[i][1] + 2)
            m12 = (d[i][0] + 1, d[i][1] + 2)
            m13 = (d[i][0] + 1, d[i][1] - 2)
            m14 = (d[i][0] , d[i][1] - 2)
            m15 = (d[i][0] - 1, d[i][1] - 2)



            textual_position.append(m1)
            textual_position.append(m2)
            textual_position.append(m3)
            textual_position.append(m4)
            textual_position.append(m5)
            textual_position.append(m6)
            textual_position.append(m7)
            textual_position.append(m8)
            textual_position.append(m9)
            textual_position.append(m10)
            textual_position.append(m11)
            textual_position.append(m12)
            textual_position.append(m13)
            textual_position.append(m14)
            textual_position.append(m15)
        textual_position_list.append(textual_position)
    for i in range(len(textual_position_list)):
        for j in range(len(textual_position_list[i])):
            if textual_position_list[i][j][0] <0:
                textual_position_list[i][j] = (0,textual_position_list[i][j][1])
            if textual_position_list[i][j][0] >=480:
                textual_position_list[i][j] = (479,textual_position_list[i][j][1])
            if textual_position_list[i][j][1] <0:
                textual_position_list[i][j] = (textual_position_list[i][j][0],0)
            if textual_position_list[i][j][1] >=680:
                textual_position_list[i][j] = (textual_position_list[i][j][0],479)

    return textual_position_list


def get_pixels(path,pos):
    image_path = path
    faceCascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    predictor =  dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    image = cv2.imread(image_path)

    pixels = []
    for p in pos:
        pixel = image[p]
        pixels.append(pixel[0])
        pixels.append(pixel[1])
        pixels.append(pixel[2])
    #print(pixels)
    #endtime = datetime.datetime.now()

    #print(endtime - starttime)

    return pixels

#end def




textual_positions = textual_position('data/landmarks.csv')
csvfile = open('data/data.csv', 'r')
data = []
path = []
pixels_list = []
landmarks_list = []
full_data_list = []
for line in csvfile:
    data.append(list(line.split(',')))
for d in data:
    path.append(d[1].strip())

for i in range(len(path)):

    pixels = get_pixels(path[i],textual_positions[i])

    pixels_list.append(pixels)

#dataframe = pd.DataFrame(pixels_list)
#dataframe.to_csv('data/texualfeatures.csv',header=False,index=False)
position_data = []
for i in range(len(textual_positions)):
    temp = []
    for j in range(len(textual_positions[i])):
        temp.append(textual_positions[i][j][0])
        temp.append(textual_positions[i][j][1])
    position_data.append(temp)




#df = pd.DataFrame(position_data)
#df.to_csv('data/textualpositions.csv',header=False,index=False)
