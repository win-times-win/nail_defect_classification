# Nail defect detection
A docker Image that consists of a REST API running on Flask. API allows the user to use a CNN to identifies the probability of defect nails. CNN accuracy score ~0.95.

![](example.jpg)


## Setup
1. Download release and unrar. 

2. Build docker image.
```shell
$ docker build -t <docker-image-name-of-your-choice> . 
```
    
3. Run docker image.
```shell
$ docker run -d -p 5000:5000 <docker-image-name-of-your-choice>  
```
4. To access the jupyter notebook used for training the model, import environment.yml as a new environment in Anaconda Navigator. 

## Usage

The website can be accessed by one of the following URLs. The results can be assessed by enterring the URL of your image into the input field at the website.
```shell
http://<DOCKER-IP>:5000
http://127.0.0.1:5000
http://localhost:5000
```
or it can be directly assessed from bash.
```shell
$ curl http://<DOCKER-IP>:5000/predict?image_url=<nail-image-of-your-choice>  
```
Currently the API only works with images of size 1936x1216.

## Main Components

- Dockerfile
- requirements.txt
- application.py:
  - Flask main script.
- nail_defect_detector.py:
  - Functions for image preprocessing and model prediction.
  
- EDA_model_training.ipynb:
  - EDA of raw data and training of the model.
- environment.yml:
  - Conda virtual environment configuration for EDA_model_training.ipynb.


