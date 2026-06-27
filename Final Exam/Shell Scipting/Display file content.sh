
#! /bin/bash

if [ -f "$1" ]
then
    echo "Contents of the file: "
    cat "$1"
else
    echo "Not a file"
fi

