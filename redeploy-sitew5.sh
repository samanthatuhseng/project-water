#!/bin/bash

# Step: Kill all existing tmux sessions
tmux kill-server

# Step: cd into project folder
cd project-water

# Step: Get latest changes from main branch on GitHub
git fetch && git reset origin/main --hard

# Step: Activate python virtual environment and install dependencies
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Step: Start Flask server in a new detached Tmux session
cd ..
tmux new -s myflasksession 'cd project-water && flask run --host=0.0.0.0'
echo "Reached"
