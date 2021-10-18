#!/bin/bash

if lsof -Pi :7998 -sTCP:LISTEN -t >/dev/null ; then
        echo "Stopping Server...."
        kill $(lsof -t -i:7998)
else
        echo "no server found"
fi