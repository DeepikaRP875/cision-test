#!/bin/bash

# File to be processed
file="test-content.txt"

# Use grep to fetch the string "deepika"
grep_result=$(grep -o "deepika" "$file")

# Check if "deepika" is found
if [ -n "$grep_result" ]; then
  # Use tr to remove "e", "i", "o", and "u" from "deepika"
  tr_result=$(echo "$grep_result" | tr -d 'eiou')

  # Use awk to format the output
  awk_result=$(awk -v original="$grep_result" -v modified="$tr_result" '{gsub(original, original " " modified); print}' "$file")

  # Use sed to append "senior devsecops engineer" to the same line
  sed_result=$(echo "$awk_result" | sed "s/$grep_result.*/& senior devsecops engineer/")

  # Output the result
  echo "$sed_result"
else
  echo "String 'deepika' not found in the file."
fi