"""
This script consists of the nail defect detector model. 
Functions available are image_preprocessing(img) and
predict_prob(img).
"""

import requests
import numpy as np
from skimage.morphology import remove_small_objects
from skimage.transform import resize
from tensorflow.keras.models import Model, load_model
import tensorflow as tf

m = load_model("200306_model.h5")


def image_preprocessing(img):
    """Preprocesses a numpy array image for input into model."""
    # pre-crop the image to avoid misleading bright pixels.
    img = img[125:1100, 500:1500]
    # find the average location of the top 20 brightest pixels.
    sort_image = np.dstack(np.unravel_index(np.argsort(img[:, :].ravel()), (975, 1000)))
    sort_x_avg = int(np.around(np.average(sort_image[:, -20:-1, 0])))
    sort_y_avg = int(np.around(np.average(sort_image[:, -20:-1, 1])))

    if sort_x_avg < 200:
        sort_x_avg = 200
    elif sort_x_avg + 200 > 975:
        sort_x_avg = 975 - 200
    if sort_y_avg < 200:
        sort_y_avg = 200
    elif sort_y_avg + 200 > 1000:
        sort_y_avg = 1000 - 200

    img = img[sort_x_avg - 200 : sort_x_avg + 200, sort_y_avg - 200 : sort_y_avg + 200]
    # resize image, note that skimage normalizes the array
    img = resize(img, (224, 224))
    # thresholding and removing small objects to minimize noise.
    threshold = np.average(img) + np.std(img) * 0.75
    pred_temp = img.copy()
    cnd = img[:] >= threshold
    pred_temp[cnd] = 1
    cnd = img[:] < threshold
    pred_temp[cnd] = 0
    pred_temp = pred_temp.astype("bool")
    pred_temp = remove_small_objects(pred_temp, 30, connectivity=2, in_place=True)
    img = np.multiply(img, pred_temp)
    # create a 3 channel image duplicate for feeding into model.
    img = np.array(img, dtype=np.float32)
    img = np.expand_dims(img, 2)
    img = img * np.ones((1, 1, 3))
    return img


def predict_prob(img):
    """Takes a numpy array of images and returns a dictionary of probabilities."""
    pred = m.predict(img)
    out = {"good": pred.tolist(), "bad": (1 - pred).tolist()}
    return out
