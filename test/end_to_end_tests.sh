#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status

echo "Running pics-org report no-exif-date..."
pics-org report no-exif-date --dir-path ./test_assets

echo "Running pics-org report no-exif-location..."
pics-org report no-exif-location --dir-path ./test_assets

echo "Running pics-org report exif-date-not-in-path..."
pics-org report exif-date-not-in-path --dir-path ./test_assets

echo "Running pics-org edit set-exif-date..."
pics-org edit set-exif-date --date "2024:09:25 12:34:57" ./test_assets/DSC00316.JPG

echo "Running pics-org edit set-exif-location..."
pics-org edit set-exif-location -- 54.991008 -2.574939 ./test_assets/DSC00316.JPG