from flask import Flask
import torch
import pandas as pd
import numpy as np
from PIL import Image

PATH_MODEL = 'yolov3.weights'
PATH_IMG = 'dog.jpeg'

model_yolo = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img = PATH_IMG

predict = model_yolo(img)

df = predict.pandas().xyxy[0]

df.to_csv('predict.csv')