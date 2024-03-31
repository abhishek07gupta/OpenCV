import cv2 as cv
import os
import numpy as np

people=['hritik','salman','shahrukh']


# one way of getting the names of people
# p=[]
# for i in os.listdir(r'C:\Users\abhis\OneDrive\Desktop\OpenCV\face_recognise\images'):
#     p.append(i)
# print(p)

Dir = r'C:\Users\abhis\OneDrive\Desktop\OpenCV\face_recognise\images'

features = []
labesl = []

def create_train():
    for person in people:
        path = os.path.join(Dir,person)
        label = people.index(person)

