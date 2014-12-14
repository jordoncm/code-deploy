#!/bin/bash
# Script to setup the dependencies for the sample app. Designed to work with
# Amazon Linux.

# Make sure Python PIP is available on the system.
yum update -y
yum install gcc python-devel python-pip -y

# Install Tornado.
pip install tornado
