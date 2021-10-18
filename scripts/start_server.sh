#!/bin/bash

echo "Starting Server...."
nohup python3 /var/www/html/pythonwebapp/app.py > /dev/null 2>&1&