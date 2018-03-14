from skimage.feature import local_binary_pattern
from scipy.stats import itemfreq
import cv2
from Generate_texual_features import textual_position
import numpy as np
import pandas as pd
import datetime

starttime = datetime.datetime.now()



def get_hist(path):
    image_path = path
    # Create the haar cascade
    faceCascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    image = cv2.imread(image_path)
    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    radius = 3  # （这是lbp用的参数 radius窗口大小 通常是3，5,7.）
    # Number of points to be considered as neighbourers
    no_points = 8 * radius
    # Uniform LBP is used
    lbp = local_binary_pattern(image, no_points, radius, method='uniform')
    # （先整个图im_gray算出lbp编码。然后从lbp里面把我们用到的点的位置保留，没有用到的删除,lbp是与im_gray相同维数的矩阵，值是一个lbp代码，类似颜色）
    # Calculate the histogram
    pos = textual_position('data/landmarks.csv')
    lbp_used = []
    for i in pos:
        temp = []
        for j in i:
            temp.append(lbp[j[0]][j[1]])
        lbp_used.append(temp)
    lbp_used = np.array(lbp_used)

    x = itemfreq(lbp_used.ravel())
    # Normalize the histogram
    hist = x[:, 1] / sum(x[:, 1])

    return lbp_used,hist





csvfile = open('data/data.csv', 'r')
data = []
landmarks_list = []
full_data_list = []
for line in csvfile:
    data.append(list(line.split(',')))
lbp_hist = []
for d in data:
    full = []
    lbp,hist = get_hist(d[1].strip())
    print('222222222',hist)
    endtime = datetime.datetime.now()

    print(endtime - starttime)
    lbp_hist.append(hist)

#df = pd.DataFrame(lbp_hist)
#df.to_csv('data/lbpfeatures.csv',header=False,index=False)






