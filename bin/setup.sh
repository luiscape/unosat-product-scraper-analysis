#!/bin/bash

#
# Setup the virtual environment
# and install dependencies.
#
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
