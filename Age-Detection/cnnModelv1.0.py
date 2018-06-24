from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import Flatten
from keras.layers import MaxPooling2D 
from keras.layers import Dropout 

#Initializing the CNN
classifier=Sequential()

#S1 Convolution + Pooling
classifier.add(Conv2D(32, (3, 3), padding='same', input_shape=(150,150,3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))


#S2 Flattening
classifier.add(Flatten())

#S3 Fully connected 
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=64, activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=3, activation='softmax'))

#Compiling the CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#P2 Fitting the images to the CNN
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (150, 150),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (150, 150),
                                            batch_size = 32,
                                            class_mode = 'categorical')

classifier.fit_generator(training_set,
                         steps_per_epoch = 8000,
                         epochs = 3,
                         validation_data = test_set,
                         validation_steps = 2000)


#Loading the testset
import pandas as pd
test=pd.read_csv('test.csv')
sample=pd.read_csv('Sample.csv')

import numpy as np
from keras.preprocessing import image
training_set.class_indices
for i in range(len(test)):
    my_img=test.get_value(index=i,col='ID')
    src='Test/'+my_img
    test_image = image.load_img(src, target_size = (150, 150))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    if result[0][0] > 0.5:
        prediction = 'MIDDLE'
    if result[0][1] > 0.5:
        prediction = 'OLD'
    if result[0][2] > 0.5:
        prediction = 'YOUNG'
    sample=sample.append({'Class':prediction,'ID':my_img},ignore_index=True)
    

sample.to_csv('result.csv', sep='\t',index=False)


#Making Single Prediction
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('y.jpg', target_size = (150, 150))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] > 0.5:
        prediction = 'MIDDLE'
if result[0][1] > 0.5:
        prediction = 'OLD'
if result[0][2] > 0.5:
        prediction = 'YOUNG'
sample=sample.append({'Class':prediction,'ID':my_img},ignore_index=True)
