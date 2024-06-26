#!/bin/bash

# Configuration
REMOTE_USER="pi"
REMOTE_HOST="raspberrypisipm.am14.uni-tuebingen.de"
REMOTE_DIR="/home/pi/SSoft_exp/app/ambient/static/"
REMOTE_PASSWORD="pipc"
LOCAL_DIR="/home/pi/logger/logs/"

# Files to copy from local to remote
FILES_TO_COPY=(
    "cooler.txt"
    "darkbox.txt"
    "outside.txt"
)

# ANSI color codes
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;36m'
NC='\033[0m' # No Color

# Function to handle Ctrl+C
trap "echo 'Script terminated by user'; exit" SIGINT

# Counter for checking new files
CHECK_COUNTER=0

# Main loop to run every 1100 seconds
while true; do
    echo "Checking for new files (Check #$CHECK_COUNTER)..."
    echo ""
    # Loop through each file in FILES_TO_COPY array
    ((CHECK_COUNTER++))
    for FILE in "${FILES_TO_COPY[@]}"; do
        # Copy the file to the remote directory
        sshpass -p "$REMOTE_PASSWORD" scp -o StrictHostKeyChecking=no "$LOCAL_DIR$FILE" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR"
        
        # Check if the copy was successful
        if [ $? -eq 0 ]; then
            echo -e "Copied ${BLUE}$FILE${NC} to ${GREEN}$REMOTE_HOST${NC}"
        else
            echo -e "${RED}Failed${NC} to copy $FILE to $REMOTE_HOST"
        fi
    done
    # Wait for 1100 seconds before the next iteration
    echo ""
    echo "Waiting..."
    echo ""
    sleep 10
done
