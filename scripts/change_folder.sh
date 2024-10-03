#!/bin/bash

# Define source and destination directories
source_dir=~/Downloads
dest_dir=~/Google\ Drive/My\ Drive/Work/learning/FW24-AICUP/data/auto

# Move files that start with "auto" and do not contain "(1)"
for file in "$source_dir"/auto*; do
  if [[ "$file" != *"(1)"* ]]; then
    unzip "$file" -d "$dest_dir"
  fi
done
