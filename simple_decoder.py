import numpy as np
import os
from PIL import Image


class SimpleRecognizer:
    def __init__(self):
        self.training_data = []
        self.target_values = []
        self.downscale_res = (16, 16)

    def _load(self, path, target_value):
        training_imgs = os.listdir(path)
        for f in training_imgs:
            img = Image.open(path+'/'+f)
            img = img.resize(self.downscale_res, Image.BILINEAR)
            self.training_data.append(np.array(img.getdata()).flatten())
            self.target_values.append(target_value)

    def load(self):
        self._load('Training_Data/Blue', 0)
        self._load('Training_Data/Green', 1)
        self._load('Training_Data/Orange', 2)
        self._load('Training_Data/Purple', 3)
        self._load('Training_Data/Red', 4)
        self._load('Training_Data/Yellow', 5)
        self._load('Training_Data/Chocolate', 6)

    def predict(self, img):
        resized_img = img.resize(self.downscale_res, Image.BILINEAR)
        np_img = np.array(resized_img).flatten()
        possible_target = -1
        min_diff = 0
        for i, reference in enumerate(self.training_data):
            diff = np.power((np_img - reference), 2).sum()
            if possible_target is -1 or diff < min_diff:
                min_diff = diff
                possible_target = self.target_values[i]

        return possible_target





