"""
This script consists of FLASK for a simple REST api.

To run this in Linux, enter the following commands in 
the bash while you are in the script folder:
    
    export FLASK_APP=application.py
    flask run

To run this in Windows, enter the following commands in 
the bash while you are in the script folder:
    
    SET FLASK_APP=application.py
    flask run
"""
from flask import Flask
from flask import render_template, request
from PIL import Image
from io import BytesIO
import json
import numpy as np
import nail_defect_detector
import requests

app = Flask(__name__)

#%%
@app.route("/")
def index():
    """main page, prompts the user to enter URL to picture"""
    return render_template("main.html")


#%%
@app.route("/predict", methods=["GET"])
def predict():
    """result page, takes a url of an image and return
    a JSON of defect probabilities"""
    data = dict(request.args)
    resp = requests.get(data["image_url"])
    img = Image.open(BytesIO(resp.content))
    img = np.asarray(img, dtype="uint8")
    img = np.array([nail_defect_detector.image_preprocessing(img)])
    pred = nail_defect_detector.predict_prob(img)
    return json.dumps(pred)
