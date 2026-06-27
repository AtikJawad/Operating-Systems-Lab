#!/bin/bash

echo "===== SYSTEM INFORMATION ====="

echo "Date & Time:"
date

echo
echo "CPU Usage:"
top -bn1 | grep "Cpu"

echo
echo "Memory Usage:"
free -h

echo
echo "Disk Usage:"
df -h

echo
echo "Network Statistics:"
netstat -i
