import csv
import re
import pandas as pd
import datetime

starttime = datetime.datetime.now()
def euclidean_distance(vector1,vector2):
    dis = 0
    vec1 = re.split('\,|\(|\)',vector1)
    vec2 = re.split('\,|\(|\)',vector2)
    vector1 = (int(vec1[1]),int(vec1[2]))
    vector2 = (int(vec2[1]),int(vec2[2]))
    for v1, v2 in zip(vector1,vector2):
        print(v1,v2)
        dis+= (v1-v2)**2
    eu_dis = dis**0.5
    return eu_dis
#end def
def geo_features(path):
    data = []
    reader = csv.reader(open(path))
    for row in reader:
        data.append(row)
    geo_features_list = []
    for d in data:
        geo_features = []

        for i in range(0,16):
            euclidean_dist = euclidean_distance(d[i],d[i+1])
            geo_features.append(euclidean_dist)
        for i in range(17,21):
            euclidean_dist = euclidean_distance(d[i],d[i+1])
            geo_features.append(euclidean_dist)
        for i in range(22, 26):
            euclidean_dist = euclidean_distance(d[i],d[i+1])
            geo_features.append(euclidean_dist)
        for i in range(27, 35):
            euclidean_dist = euclidean_distance(d[i],d[i+1])
            geo_features.append(euclidean_dist)
        for i in range(36, 41):
            euclidean_dist = euclidean_distance(d[i],d[i+1])
            geo_features.append(euclidean_dist)
        for i in range(42, 47):
            euclidean_dist = euclidean_distance(d[i],d[i+1])
            geo_features.append(euclidean_dist)
        for i in range(48, 67):
            euclidean_dist = euclidean_distance(d[i],d[i+1])
            geo_features.append(euclidean_dist)

        geo_features_list.append(geo_features)

    print(len(geo_features_list),geo_features_list)
    endtime = datetime.datetime.now()
    #print((endtime - starttime)/327)
    return geo_features_list


geometrical_features = geo_features('data/landmarks.csv')
#dataframe = pd.DataFrame(geometrical_features)
#dataframe.to_csv('data/geofeatures.csv',header=False,index=False)

