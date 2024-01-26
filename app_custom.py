from flask import Flask
import torch
import pandas as pd
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route("/")
def yolo():
    
    PATH_MODEL = 'model_CUSTOM.pt'
    PATH_IMG = 'image.jpg'
    
    model_yolo = torch.hub.load('ultralytics/yolov5', 'custom', path=PATH_MODEL)
    
    img = PATH_IMG
    
    predict = model_yolo(img)
    
    df = predict.pandas().xyxy[0]
    
    df.to_csv('predict.csv')
    
    return 'ok!!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
