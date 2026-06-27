#!/bin/bash

CPU_LIMIT=80
DISK_LIMIT=90

CPU=$(top -bn1 | grep "Cpu" | awk '{print $2}')
DISK=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

if [ ${CPU%.*} -gt $CPU_LIMIT ]
then
    echo "WARNING: High CPU Usage!"
fi

if [ $DISK -gt $DISK_LIMIT ]
then
    echo "WARNING: Disk Space Running Low!"
fi
