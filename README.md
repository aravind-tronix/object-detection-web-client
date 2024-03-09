# Object Detection API using YOLO Darknet and Flask
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Introduction
This API provides a simple way to perform object detection using the YOLO (You Only Look Once) model implemented with Darknet, integrated with a Flask server. It allows users to send images to the server and receive JSON responses containing the result.

## Installation

1. Clone the repository 
2. `git clone https://github.com/aravind-tronix/object-detection-web-client.git`
3. `cd object-detection-web-client`
4. Install required packages by `pip install -r requirements.txt`
5. Start the Flask server `python app.py`

# Architecture Overview
The architecture of this API involves four main components:

## Object Detection Model (YOLO with Darknet):
1. YOLO (You Only Look Once) is a state-of-the-art, real-time object detection system.
2. Darknet is an open-source neural network framework written in C and CUDA.
3. Project uses the YOLO model implemented with Darknet for efficient object detection.

## Flask Server:
1. Flask is a lightweight WSGI web application framework in Python.
2. Have integrated the YOLO model with a Flask server to create a RESTful API.
3. The Flask server listens for incoming HTTPS requests, processes them, and returns JSON responses.

## Apache HTTP Server:
1. Apache HTTP Server is a widely-used open-source web server software.
2. Have deployed the Flask application behind Apache using mod_wsgi module to serve the API.
3. Apache acts as a gateway, routing incoming requests to the Flask application.

## Hetzner Cloud:
1. Hetzner Cloud is a cloud hosting provider offering scalable virtual private servers (VPS) and cloud infrastructure.
2. The deployment of the Apache HTTP Server along with the Flask application is done on Hetzner Cloud infrastructure for reliable and scalable hosting.
