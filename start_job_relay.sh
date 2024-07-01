#!/bin/bash
# Start screen session
/usr/bin/screen -dmS relay /home/logger/logenv/bin/python3 /home/logger/logger/relay.py
