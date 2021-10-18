#!/bin/bash

echo "Stop Server...."
kill $(lsof -t -i:7998)