#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status

# Ensure test_assets directory is in a clean state before starting
git checkout HEAD -- test_assets

# Test the report no-exif-date command

echo "Running pics-org report no-exif-date..."
pics-org report no-exif-date --dir-path ./test_assets

# Test the report no-exif-location command

echo "Running pics-org report no-exif-location..."
pics-org report no-exif-location --dir-path ./test_assets

# Test the report exif-date-not-in-path command

echo "Running pics-org report exif-date-not-in-path..."
pics-org report exif-date-not-in-path --dir-path ./test_assets

# Test the edit set-exif-date command

echo "Running pics-org edit set-exif-date..."
pics-org edit set-exif-date --date "2024:09:25 12:34:57" ./test_assets/DSC00316.JPG
changed_files=$(git diff --name-only test_assets)
if [ "$changed_files" == "test_assets/DSC00316.JPG" ]; then
    echo "Test passed: Only the expected file was changed."
else
    echo "Test failed: Unexpected files were changed:"
    echo "$changed_files"
    exit 1
fi
git checkout HEAD -- test_assets/DSC00316.JPG

# Test the edit set-exif-location command

echo "Running pics-org edit set-exif-location..."
pics-org edit set-exif-location -- 54.991008 -2.574939 ./test_assets/DSC00316.JPG
changed_files=$(git diff --name-only test_assets)
if [ "$changed_files" == "test_assets/DSC00316.JPG" ]; then
    echo "Test passed: Only the expected file was changed."
else
    echo "Test failed: Unexpected files were changed:"
    echo "$changed_files"
    exit 1
fi
git checkout HEAD -- test_assets/DSC00316.JPG

# Test the edit set-exif-date-to-best-guess command

echo "Running pics-org edit set-exif-date-to-best-guess..."
pics-org edit set-exif-date-to-best-guess --dir-path ./test_assets
changed_files=$(git diff --name-only test_assets)
if [ "$changed_files" == "test_assets/2020/5. May/4. birthday/IMG-20161121-WA0001.jpg" ]; then
    echo "Test passed: Only the expected file was changed."
else
    echo "Test failed: Unexpected files were changed:"
    echo "$changed_files"
    exit 1
fi
git checkout HEAD -- "test_assets/2020/5. May/4. birthday/IMG-20161121-WA0001.jpg"