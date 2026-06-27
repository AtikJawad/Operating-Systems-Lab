#!/bin/bash

LOGFILE="user_access.log"

echo "===== Login Record =====" >> $LOGFILE
date >> $LOGFILE
who >> $LOGFILE
echo "----------------------" >> $LOGFILE
