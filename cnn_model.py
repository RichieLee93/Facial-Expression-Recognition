from __future__ import print_function

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer, one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Input, Dense, Flatten, Dropout
from keras.layers import Embedding, Conv1D, MaxPooling1D,concatenate
from keras.models import Model, load_model
from keras.callbacks import ModelCheckpoint
from keras.utils import to_categorical

import win_unicode_console
win_unicode_console.enable()



data_train =  pd.read_csv('data/textualgeo_train.csv',header=0)
data_test = pd.read_csv('data/textualgeo_test.csv',header=0)
# data_train = data_train+5

data_train = np.array(data_train)
data_test =  np.array(data_test)

# print(data_train,data_test.shape)

x_train = data_train[:,0:-1] # training set
for i in range(len(x_train)):
    for j in range(len(x_train[i])):
        x_train[i][j] = x_train[i][j]+4

y_train = data_train[:,-1]  # training label
y_train = to_categorical(y_train)
y_train = np.delete(y_train, 0, axis=1)
print('aaaaa',y_train.shape)

x_test = data_test[:,0:-1]  # validation set

for i in range(len(x_test)):
    for j in range(len(x_test[i])):
        x_test[i][j] = x_test[i][j]+4

y_test = data_test[:,-1]  # validation label
y_test = to_categorical(y_test)
y_test = np.delete(y_test, 0, axis=1)


print(y_test.shape)
#train a 1D convnet with global maxpoolinnb_wordsg

embedding_layer = Embedding(10000 + 1,
                            300,
                            input_length=1417,
                            trainable=True)


input = Input(shape=(1417,), dtype='float64')
print('input.shape',input.shape)
embedded_sequences = embedding_layer(input)
x = Conv1D(128, 5, activation='relu')(embedded_sequences)
print('1',x.shape)
x = MaxPooling1D(3)(x)
print('2',x.shape)
x = Conv1D(128, 5, activation='relu')(x)
print('3',x.shape)
x = MaxPooling1D(3)(x)
print('4',x.shape)
x = Dropout(1)(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
preds = Dense(7, activation='softmax')(x)
 # softmax

# optimization
model = Model(inputs=input, outputs=preds)
model.compile(loss='categorical_crossentropy',
              optimizer='Adadelta',
              metrics=['acc'],
              )

#RMSprop

filepath='C:/Users/NLP/PycharmProjects/Facial_Emotion_AR/facial_best.hdf5'

checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=0, save_best_only=True,mode='max')
callbacks_list = [checkpoint]
model.fit(x_train, y_train, epochs=50,batch_size=32, validation_split=0.15, callbacks=callbacks_list)

# checkpoint = ModelCheckpoint(filepath='facial_best1.hdf5',monitor='val_acc',verbose=0,save_best_only='True',mode='auto')

#model = load_model(filepath)
loss,acc = model.evaluate(x_test,y_test)

print('test_loss',loss,'test_accuracy',acc)


#score = model.evaluate(x_train, y_train, verbose=0)
#print('train score:', score[0])
#print('train accuracy:', score[1])
#score = model.evaluate(x_test, y_test, verbose=0)
#print('Test score:', score[0])
#print('Test accuracy:', score[1])