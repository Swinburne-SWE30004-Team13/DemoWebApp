#!/bin/bash

echo "Installing python dependencies..."
pip3 install --trusted-host pypi.python.org -r /var/www/html/pythonwebapp/requirements.txt
echo "completed Install"