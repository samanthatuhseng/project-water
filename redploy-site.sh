#!/bin/bash
chmod +x redploy-site.sh
# Step: cd into project folder
cd /path/to/your/project-folder

# Step: Get latest changes from main branch on GitHub
git fetch && git reset origin/main --hard

# Step: Spin containers down to prevent out of memory issues on the VPS instance
docker-compose -f docker-compose.prod.yml down

# Step: Build and start containers in detached mode
docker-compose -f docker-compose.prod.yml up -d --build