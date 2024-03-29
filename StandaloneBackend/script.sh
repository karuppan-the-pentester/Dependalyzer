#!/bin/sh

if [ -z "$1" ]; then
    echo "No parameters were given"
else
    echo ""
    echo ""
    echo "Project Group    : $1"
    echo "Project Author   : $2"
    echo "Project Name     : $3"
    echo "Project Category : $4"
    echo "Project Source   : $5" 
    echo "Source file Name : $6" 

    # Check if the source is a URL or a zip file
    if echo "$5" | grep -q "^https\?://"; then

        echo "Cloned repository from $5"
        git clone "$5"

        echo "python3 dependalayzer.py $5"
        python3 dependalayzer.py --url="$5"  

    else
        # If it's a zip file, unzip it
        unzip -q "$5" -d "$3"
        echo "Unzipped file: $5"
    fi

    
fi

# Keep the container running
exec /bin/bash
