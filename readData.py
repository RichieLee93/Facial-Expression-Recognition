import os
import pandas as pd

def file_path (file_dir):
    temp = []
    file_path = []
    for files in os.walk(file_dir):
        temp.append(files)
    for i in temp:
        if i[1] == []:
            path = i[0]+'\\'+i[2][-1]
            file_path.append(path)
    return file_path

#end def


def label_path(label_dir):
    temp = []
    label_path = []
    for labels in os.walk(label_dir):
        temp.append(labels)
    for t in temp:
        if t[1] == [] and t[2] != []:
            path = t[0]+'\\'+t[2][0]
            label_path.append(path)
    return label_path

#end def


def get_label_list(label_paths):
    label_list = []
    for l in label_paths:
        f = open(l)
        label_list.append(f.read().strip()[0])
    for i in range(len(label_list)):
        label_list[i] = int(label_list[i])
    return label_list

#end def


def label_generate(file_paths,label_paths,label_list):
    fm_list = []
    lm_list = []
    labels = []
    for f in file_paths:
        fs = os.path.split(f)
        fn = os.path.splitext(fs[1])
        fm = fn[0].split('_')
        fm_list.append(fm)
    for l in label_paths:
        ls = os.path.split(l)
        ln = os.path.splitext(ls[1])
        print(ln)
        lm = ln[0].split('_')
        lm_list.append(lm)
    # print(len(fm_list))
    # print(len(lm_list))
    # print(len(label_list))
    for fml in fm_list:
        label = 8
        for i in range(len(lm_list)):
            if fml[0] == lm_list[i][0] and fml[1] == lm_list[i][1] and fml[2] == lm_list[i][2]:
                label = label_list[i]
        labels.append(label)
    return labels

#end def




file_paths = file_path('data/cohn-kanade-images')
label_paths = label_path('data/Emotion')
label_list = get_label_list(label_paths)
labels = label_generate(file_paths,label_paths,label_list)


dataframe = pd.DataFrame(file_paths,labels)
dataframe.to_csv('data/data.csv',header=False)