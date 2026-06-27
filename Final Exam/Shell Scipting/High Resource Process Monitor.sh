#!/bin/bash

echo "Top CPU Consuming Processes"

ps aux --sort=-%cpu | head -6

echo
echo "Top Memory Consuming Processes"

ps aux --sort=-%mem | head -6
