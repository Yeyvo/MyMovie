import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout, BatchNormalization, Conv2D, MaxPool2D
from os.path import exists
import json

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

img_width = 370
img_height = 556

def createModel(DataShape) :
  model = Sequential()
  model.add(Conv2D(16, (3, 3), activation='relu', input_shape=DataShape, kernel_regularizer='l2'))
  model.add(BatchNormalization())
  model.add(MaxPool2D(2, 2))
  model.add(Dropout(0.3))

  model.add(Conv2D(32, (3, 3), activation='relu', kernel_regularizer='l2'))
  model.add(BatchNormalization())
  model.add(MaxPool2D(2, 2))
  model.add(Dropout(0.3))

  model.add(Conv2D(64, (3, 3), activation='relu', kernel_regularizer='l2'))
  model.add(BatchNormalization())
  model.add(MaxPool2D(2, 2))
  model.add(Dropout(0.4))

  model.add(Conv2D(128, (3, 3), activation='relu', kernel_regularizer='l2'))
  model.add(BatchNormalization())
  model.add(MaxPool2D(2, 2))
  model.add(Dropout(0.5))

  model.add(Flatten())

  model.add(Dense(128, activation='relu', kernel_regularizer='l2'))
  model.add(BatchNormalization())
  model.add(Dropout(0.5))

  model.add(Dense(128, activation='relu', kernel_regularizer='l2'))
  model.add(BatchNormalization())
  model.add(Dropout(0.5))

  model.add(Dense(25, activation='sigmoid', kernel_regularizer='l2'))
  model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3), loss='binary_crossentropy', metrics=['accuracy'])
  return(model)

def plot_learningCurve(history, epoch):
  # Plot training & validation accuracy values
  epoch_range = range(1, epoch+1)
  plt.plot(epoch_range, history.history['accuracy'])
  plt.plot(epoch_range, history.history['val_accuracy'])
  plt.title('Model accuracy')
  plt.ylabel('Accuracy')
  plt.xlabel('Epoch')
  plt.legend(['Train', 'Val'], loc='upper left')
  plt.show()

  # Plot training & validation loss values
  plt.plot(epoch_range, history.history['loss'])
  plt.plot(epoch_range, history.history['val_loss'])
  plt.title('Model loss')
  plt.ylabel('Loss')
  plt.xlabel('Epoch')
  plt.legend(['Train', 'Val'], loc='upper left')
  plt.show()




def getModel() :
  if (exists('./my_model.h5')):
    model = tf.keras.models.load_model('my_model.h5')
    model.summary()
    print("model fully loaded ")
  else :

    print(tf.__version__)

    print("import data\n")
    data = pd.read_csv(
      'Multi_Label_dataset/train.csv')
    print("import done\n")
    data.head()


    X = []

    for i in tqdm(range(data.shape[0])):
      path = 'Multi_Label_dataset/Images/' + \
             data['Id'][i] + '.png'
      img = image.load_img(path, target_size=(img_width, img_height, 3), )
      img = image.img_to_array(img)
      img = img / 255.0
      X.append(img)
    print("image import and prep to show image")
    X = np.array(X)

    print("done with images")
    y = data.drop(['Id', 'Genre'], axis=1)
    y = y.to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.15)
    print("Training set created\n")

    print("model creation")

    model = createModel(X_train[0].shape)

    model.summary()

    history = model.fit(X_train, y_train, epochs=32, validation_data=(X_test, y_test))

    model.save('my_model.h5')

#     plot_learningCurve(history, 10)

    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)

    print('\nTest accuracy:', test_acc)
    print('\nTest loss:', test_loss)

  return model

def evaluatePoster(model,poster):
  img = image.load_img(poster,target_size=(img_width, img_height, 3))
#   plt.imshow(img)
  img = image.img_to_array(img)
  img = img / 255.0
  img = img.reshape(1, img_width, img_height, 3)
  Y_prob = model.predict(img)
  data = ["Action","Adventure","Animation","Biography","Comedy","Crime","Documentary","Drama","Family","Fantasy","History","Horror","Music","Musical","Mystery","N/A","News","Reality-TV","Romance","Sci-Fi","Short","Sport","Thriller","War","Western"]
  print(Y_prob)

  top2 = np.argsort(Y_prob[0])[:-3:-1]
  top2proba = np.sort(Y_prob[0])[:-3:-1]

  res = []
  for i in range(2):
    print(data[top2[i]] , "   :   " , top2proba[i])
    movie = {}
    movie['name'] = data[top2[i]]
    movie['confidence'] = "{:.1f}%".format(top2proba[i]*100)
    movie['id'] = 0
    res.append(movie)
    print("MMMMM : " , movie)

  return res





model = getModel()
# evaluatePoster(model,'sing.jpg')



