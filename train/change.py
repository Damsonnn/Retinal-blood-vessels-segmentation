import cv2
import os

folders = ["./image", './label']

for folder in folders:
    ids = os.listdir(folder)
    for image_id in self.ids:
        image = cv2.imread(image_id)
        cv2.imshow('image', image)
