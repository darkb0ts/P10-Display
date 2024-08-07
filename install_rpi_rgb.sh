#!/bin/bash

echo "Installing Rpi-Rgb-LED-Matrix..."
Makefile build 

echo "Installing Rpi-Rgb-LED-Matrix in Python programming language..."
cd bindings/python

Makefile build 

Makefile build-python