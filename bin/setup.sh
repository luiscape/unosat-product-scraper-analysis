#!/bin/bash

#
# Setup the virtual environment
# and install dependencies.
#
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

#
# Hack for dealing with missing
# dependencies.
#
sudo pip install termcolor
sudo pip install coverage
sudo pip install nose