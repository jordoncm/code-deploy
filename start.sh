#!/bin/bash
# Start up the web server.

cd /root/
nohup python app.py > /dev/null 2>&1 &
