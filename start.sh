#!/bin/bash
pip install https://github.com/RPi-Distro/python-dlib/releases/download/v19.24.0/dlib-19.24.0-cp311-cp311-manylinux_2_17_x86_64.whl
pip install face_recognition opencv-python reportlab
pip install -r requirements.txt
python app.py
