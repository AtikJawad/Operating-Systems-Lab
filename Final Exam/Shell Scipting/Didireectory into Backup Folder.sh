#! /bin/bash

Source_dir=$1
backup_dir=$2

if [ ! -d "$source_dir" ]
then
    echo " Source Directory doesn't Exist. "
    exit 1
fi

mkdir -p "$backup_dir"

filename="backup_$(date).tar.gz"

tar -czvf "$backup_dir/$filename" "$source_dir"

echo "Backup Complete: $backup_dir/$filename"
