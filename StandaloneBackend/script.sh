#!/bin/sh

if [ -z "$1" ]; then
    echo "No paramters were given"
else
    echo ""
    echo ""
    echo "Project Group    : $1"
    echo "Project Author   : $2"
    echo "Project Name     : $3"
    echo "Project Category : $4"
    echo "Project URL      : $5" 

    git clone $5
    echo "python3 dependalayzer.py $5"
    python3 dependalayzer.py $5 
fi

# Keep the container running
exec /bin/bash
