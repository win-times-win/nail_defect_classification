# Nail defect detection
A docker Image that consists of a REST API running on Flask. API allows the user to use a CNN to identifies defect nails. CNN accuracy score ~0.95.

![](example.jpg)

## Setup
1. Download release and unrar. 

2. Build docker image.

    docker build -t <docker-image-name-of-your-choice> . 

    
3. Run docker image.

    docker run -d -p 5000:5000 <docker-image-name-of-your-choice>  

    
## Usage
The website can be assessed by one of the following URLs. 
- http://<DOCKER-IP>:5000
- http://192.0.0.1:5000
- http://127.0.0.1:5000
- http://localhost:5000
or it can be directly assessed from bash.
'''shell
$ curl http://<DOCKER-IP>:5000/predict?image_url=<nail-image-of-your-choice>  
'''
    
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


