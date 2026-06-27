#! /bin/bash

echo -e "Enter directory name: \c"
read name 
if [ -d "$name" ]
then
    count=$(ls "$name" | wc -l)
    echo "Number of files: $count "
else

    echo "Not a directory"
fi

