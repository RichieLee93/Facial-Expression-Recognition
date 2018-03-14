from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model.logistic import LogisticRegression
import numpy as np
import pandas as pd




# df = pd.read_csv('data/lbpgeo_train.csv',header=None)
df = pd.read_csv('data/textualgeo_train.csv',header=None)
# df = pd.read_csv('data/textualgeolbp_train.csv',header=None)
# df = pd.read_csv('data/geofeaturesmodel_train.csv',header=None)




X = df.iloc[:,0:-1]
y = df.iloc[:,-1]



# Set the parameters of SVM

'''
tuned_parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svm = svm.SVC()
clf = GridSearchCV(svm,tuned_parameters)
'''

tuned_parameters = {'C':[1, 10]}
svm = svm.LinearSVC(multi_class='ovr')
clf = GridSearchCV(svm,tuned_parameters)

'''
tuned_parameters = {'criterion':('gini', 'entropy'), 'n_estimators':[10, 1000]}
rf = RandomForestClassifier()
clf = GridSearchCV(rf,tuned_parameters)

'''
'''
tuned_parameters = {'n_components':[1,8]}
lda = LinearDiscriminantAnalysis()
clf = GridSearchCV(lda,tuned_parameters)

'''
'''
tuned_parameters = { 'solver' : ('lbfgs', 'sgd', 'adam'), 'alpha':(1e-5,1e-4,1e-3)}
mlp = MLPClassifier()
clf = GridSearchCV(mlp,tuned_parameters)

'''
'''
tuned_parameters = { 'penalty' : ('l1', 'l2'), 'C':[1,10,50,100],'tol':(1e-1,1e-2,1e-3,1e-4,1e-5)}
lr = LogisticRegression()
clf = GridSearchCV(lr,tuned_parameters)
'''
clf.fit(X,y)
print(clf.best_params_)


# database = pd.read_csv('data/lbpgeo_test.csv',header=None)
database = pd.read_csv('data/textualgeo_test.csv',header=None)
#database = pd.read_csv('data/textualgeolbp_test.csv',header=None)
# database = pd.read_csv('data/geofeaturesmodel_test.csv',header=None)



test_X = database.iloc[:,0:-1]
predict_y = clf.predict(test_X)

# database.to_csv('pred_RF.csv')

y_actual = database.iloc[:,-1]
#database['predicted'] = predict_y
#database.to_csv('pred_lda.csv')
print('testing on 25% data samples：')
print(classification_report(y_actual,predict_y, digits=4))
print(confusion_matrix(y_actual,predict_y))
print(accuracy_score(y_actual,predict_y))