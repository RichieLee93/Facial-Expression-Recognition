from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import csv
def generate_data(path):
    csvfile = open(path, 'r')
    data = []
    train = []
    test = []
    reader = csv.reader(csvfile)
    for r in reader:
        data.append(r)
    temp1 = data [0:245]
    temp2 = data[245:327]
    for i in range(len(temp1)):
        t = temp1[i][-1]
        temp1[i].pop()
        for j in range(len(temp1[i])):
            temp1[i][j] = float(temp1[i][j])
        train.append([tuple(temp1[i]),int(t)])

    for i in range(len(temp2)):
        t = temp2[i][-1]
        temp2[i].pop()
        for j in range(len(temp2[i])):
            temp2[i][j] = float(temp2[i][j])
        test.append([tuple(temp2[i]),int(t)])
    return train,test

def cos(vector1,vector2):
    dot_product = 0.0;
    normA = 0.0;
    normB = 0.0;
    for a,b in zip(vector1,vector2):
        dot_product += a*b
        normA += a**2
        normB += b**2
    if normA == 0.0 or normB==0.0:
        return None
    else:
        return dot_product / ((normA*normB)**0.5)



#train_data, test_data = generate_data('data/fulldata.csv')
#train_data, test_data = generate_data('data/geofeatures.csv')
#train_data, test_data = generate_data('data/textualfeatures.csv')
#train_data, test_data = generate_data('data/textualgeofeatures.csv')
#train_data, test_data = generate_data('data/textualpositions.csv')
train_data, test_data = generate_data('data/textualposgeo.csv')




predict_label_list = []
actual_label_list = []
for i in range(len(test_data)):
    actual_label_list.append(test_data[i][1])
    dist = []
    for j in range(len(train_data)):
        cos_dist = cos(test_data[i][0],train_data[j][0])
        dist.append(cos_dist)
    predict_label = train_data[dist.index(max(dist))][1]
    predict_label_list.append(predict_label)


print(classification_report(actual_label_list,predict_label_list))
print(accuracy_score(actual_label_list,predict_label_list))




