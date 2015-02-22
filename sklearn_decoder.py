from sklearn import svm
from sklearn import cross_validation
from sklearn.externals import joblib
from PIL import Image
import os
import numpy as np

'''
 candy values:
- 0 blue
- 1 green
- 2 orange
- 3 purple
- 4 yellow'''


class ImgRecognizer:
    def __init__(self):
        self.training_data = []
        self.target_values = []
        self.svc = svm.SVC(gamma=0.001, kernel='linear', C=100)
        self.downscale_res = (32, 32)

    def _load(self, path, target_value):
        training_imgs = os.listdir(path)
        for f in training_imgs:
            img = Image.open(path+'/'+f)
            img = img.resize(self.downscale_res, Image.BILINEAR)
            self.training_data.append(np.array(img.getdata()).flatten())
            self.target_values.append(target_value)

    def load(self):
        self._load('Training_Data/Blue', 0)
        self._load('Training_Data/Blue_Striped_H', 1)
        self._load('Training_Data/Blue_Striped_V', 13)
        self._load('Training_Data/Blue_Wrapped', 19)
        self._load('Training_Data/Green', 2)
        self._load('Training_Data/Green_Striped_H', 3)
        self._load('Training_Data/Green_Striped_V', 14)
        self._load('Training_Data/Green_Wrapped', 20)
        self._load('Training_Data/Orange', 4)
        self._load('Training_Data/Orange_Striped_H', 5)
        self._load('Training_Data/Orange_Striped_V', 15)
        self._load('Training_Data/Orange_Wrapped', 21)
        self._load('Training_Data/Purple', 6)
        self._load('Training_Data/Purple_Striped_H', 7)
        self._load('Training_Data/Purple_Striped_V', 18)
        self._load('Training_Data/Purple_Wrapped', 22)
        self._load('Training_Data/Red', 8)
        self._load('Training_Data/Red_Striped_H', 9)
        self._load('Training_Data/Red_Striped_V', 16)
        self._load('Training_Data/Red_Wrapped', 23)
        self._load('Training_Data/Yellow', 10)
        self._load('Training_Data/Yellow_Striped_H', 11)
        self._load('Training_Data/Yellow_Striped_V', 17)
        self._load('Training_Data/Yellow_Wrapped', 24)
        self._load('Training_Data/Chocolate', 12)

    def train(self):
        if os.path.isfile('svc.dat'):
            self.svc = joblib.load('svc.dat')
        else:
            self.load()
            np_data = np.array(self.training_data)
            np_values = np.array(self.target_values)
            self.svc.fit(np_data, np_values)
            joblib.dump(self.svc, 'svc.dat', compress=9)

    def test(self):
        np_train_data = np.array(self.training_data)
        np_values = np.array(self.target_values)
        data, test_data, train_target, test_target = cross_validation.train_test_split(np_train_data, np_values,
                                                                                       test_size=0.4, random_state=0)
        self.svc.fit(data, train_target)
        print self.svc.score(test_data, test_target)

    def predict(self, img):
        resized_img = img.resize(self.downscale_res, Image.BILINEAR)
        np_img = np.array(resized_img.getdata()).flatten()
        return int(self.svc.predict(np_img))








