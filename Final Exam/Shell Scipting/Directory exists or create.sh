#! /bin/bash

if [ -d "$1" ]
then
    echo "Directory Exists! "
else
    mkdir "$1"
    echo "Directory Created."
fi

