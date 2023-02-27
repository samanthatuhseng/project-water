#!/bin/bash

# Set variables for endpoint URLs
URL="http://localhost:5000/api/timeline_post"

# Generate a random post content
POST_CONTENT=$(openssl rand -hex 16)

curl -X POST "${POST_URL}" -d "name=sam&email=sam@gmail.com&content=${POST_CONTENT}"

echo "Getting all timeline posts..."
TIMELINE_POSTS=$(curl "${GET_URL}")

# Check if the new post is in the list of timeline posts
echo "Checking if the new post was added..."
if echo "${TIMELINE_POSTS}" | grep "${POST_CONTENT}"; then
    echo "success"
else
    echo "fail"
fi
