#!/bin/bash

echo "Starting Pokémon Collector App..."
python3 /home/ubuntu/pokemon-collector/app.py >> /home/ubuntu/pokemon-app.log 2>&1
echo "App execution finished with exit code $?"
