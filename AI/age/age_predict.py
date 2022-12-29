#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D,GlobalAveragePooling2D,Dropout, Flatten, Dense
from keras import regularizers
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder # one-hot encoding for age
from keras.utils.np_utils import to_categorical
import keras
import tensorflow.compat.v2 as tf

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
import cv2
import os
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping


# In[7]:


model = tf.keras.models.load_model('age_model.h5')


# In[12]:


X, Y = [], []
width = 180
height = 180

image = Image.open('jy.jpg')
image = image.convert('RGB')
image = image.resize((width, height))
X.append(np.array(image))
Y.append(3)


# In[13]:


X = np.array(X)
X = X.astype('float32')
X /= 255.0
Y = np.array(Y)


# In[14]:


result = model.predict(X)


# In[ ]:




