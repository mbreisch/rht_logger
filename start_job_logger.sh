#!/bin/bash
# Start screen session
sleep 10
/usr/bin/screen -dmS log /home/pi/log_pyenv/bin/python3 /home/pi/logger/db_logger.py
