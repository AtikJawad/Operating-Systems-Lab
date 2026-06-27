#!/bin/bash

echo "Enter password length:"
read len


tr -dc 'A-Za-z0-9' < /dev/urandom | head -c $len

echo
