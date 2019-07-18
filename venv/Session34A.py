import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

landmarks_frame = pd.read_csv('faces/face_landmarks.csv')

n = 60
img_name = landmarks_frame.iloc[n, 0]
print(">> Image Name:",img_name)

print()

landmarks = landmarks_frame.iloc[n, 1:].as_matrix()
print(">> Landmarks:")
print(landmarks)

print()

landmarks = landmarks.astype('float').reshape(-1, 2)
print(">> LandMarks ReShaped:")
print(landmarks)

def show_landmarks(image, landmarks):
    plt.imshow(image)
    plt.scatter(landmarks[:, 0], landmarks[:, 1], s=100, marker='.', c='r')
    plt.show()

plt.figure()
show_landmarks(io.imread(os.path.join('faces/', img_name)),
               landmarks)

