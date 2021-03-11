#!/bin/bash
cd ~/spw
source venv/bin/activate
python webapi.py >> stdout.log 2>> stderr.log &
