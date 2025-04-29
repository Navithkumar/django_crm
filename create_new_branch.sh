#!/bin/bash

# Ask the user for the new branch name
read -p "Enter the name of the new branch: " branch_name

# Check if branch name is not empty
if [ -z "$branch_name" ]; then
  echo "Branch name cannot be empty."
  exit 1
fi

# Fetch the latest changes
echo "Fetching latest changes..."
git fetch

# Create and switch to the new branch
echo "Creating and switching to new branch '$branch_name'..."
git checkout -b "$branch_name"

# Push the new branch to the remote
echo "Pushing branch to origin..."
git push -u origin "$branch_name"

echo "Branch '$branch_name' created and pushed successfully."
