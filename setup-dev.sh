#!/bin/bash
# Script to setup the dependencies for the sample app. Designed to work with
# Debian based systems only (Ubuntu, Mint, etc).

# Make sure Python PIP is available on the system.
sudo apt-get install build-essential python-dev python-pip

# Install the AWS command line tools and Tornado.
sudo pip install aws tornado
