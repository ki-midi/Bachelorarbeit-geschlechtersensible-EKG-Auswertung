# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 09:17:43 2025

@author: micha
"""

import numpy as np
import pandas as pd
import wfdb
import matplotlib.pyplot as plt
from tensorflow.keras import models, layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers.schedules import ExponentialDecay
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import shap

pfad = r"C:/Users/micha/OneDrive/Desktop/ekg/ekgdaten/"
pfad_mi_alle = r"C:/Users/micha/OneDrive/Desktop/ekg/ekgdaten/alle_werte_nn.csv"
pfad_mi_m = r"C:/Users/micha/OneDrive/Desktop/ekg/ekgdaten/y_sex_0.csv"
# pfad_mi_w = r"C:/Users/micha/OneDrive/Desktop/ekg/ekgdaten/y_sex_1.csv"
pfad_mi_w = r"G:\Meine Ablage\EKG\ekglisten\frauen01.csv"

n = 5000
Ya = pd.read_csv(pfad_mi_w, index_col='ecg_id')
Ya = Ya.iloc[:n]

print(Ya)

Yami = Ya.iloc[:n, 3].values

print(len(Yami))
print(Yami)

label_encoder = LabelEncoder()
Yami_encoded = label_encoder.fit_transform(Yami)  
Yami_categorical = to_categorical(Yami_encoded) 

print("Klassen:", label_encoder.classes_)

sampling_rate = 100

def ekg_daten_laden(Ya, sampling_rate, path):
    data = [wfdb.rdsamp(pfad + f) for f in Ya.filename_lr]
    data = np.array([signal for signal, meta in data])
    return data

X = ekg_daten_laden(Ya, sampling_rate, pfad)

def build_ekg_model(input_shape=(1000, 12)):
    model = models.Sequential()

    model.add(layers.Conv1D(filters=32, kernel_size=3, activation=None, input_shape=input_shape))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.AveragePooling1D(pool_size=2))

    model.add(layers.Conv1D(filters=64, kernel_size=3, activation=None))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.2))

    model.add(layers.Conv1D(filters=128, kernel_size=3, activation=None))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.3))
    model.add(layers.GlobalAveragePooling1D())

    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.6))
    model.add(layers.Dense(1, activation='linear'))

    model.add(layers.Dense(2, activation='softmax'))

    model.compile( loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

model = build_ekg_model(input_shape=(1000, 12))

history = model.fit(X, Yami_categorical, 
                    epochs=50, 
                    batch_size=32, 
                    validation_split=0.2)

model.save(r"C:/Users/micha/OneDrive/Desktop/ekg/nn/nn_w_01.keras")


plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.show()