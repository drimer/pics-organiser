#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status


# Ensure test_assets directory is in a clean state before starting
git checkout HEAD -- test_assets


# Tests for command: report no-exif-date command

echo "Test 'pics-org report no-exif-date' happy path"
pics-org report no-exif-date --dir-path ./test_assets


# Tests for command: report no-exif-location command

echo "Test 'pics-org report no-exif-location' happy path"
pics-org report no-exif-location --dir-path ./test_assets


# Tests for command: report exif-date-not-in-path command

echo "Test 'pics-org report exif-date-not-in-path' happy path"
pics-org report exif-date-not-in-path --dir-path ./test_assets


# Tests for command: report all

echo "Test 'pics-org report all' happy path"
pics-org report all --dir-path ./test_assets


# Tests for command: edit set-exif-date command

echo "Test 'pics-org edit set-exif-date' happy path"
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


# Tests for command: edit set-exif-location command

echo "Test 'pics-org edit set-exif-location' happy path"
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


# Tests for command: edit set-exif-date-to-best-guess command

echo "Test 'pics-org edit set-exif-date-to-best-guess' with overwrite happy path"
pics-org edit set-exif-date-to-best-guess --overwrite ./test_assets
changed_files=$(git diff --name-only test_assets)
expected_changed_files="test_assets/2020/5. May/4. birthday/IMG-20161121-WA0001.jpg
test_assets/2020/5. May/4. birthday/IMG-20210920-WA0001.jpg
test_assets/IMG-20161121-WA0001.jpg"
if [ "$changed_files" == "$expected_changed_files" ]; then
    echo "Test passed: Only the expected file was changed."
else
    echo "Test failed: Unexpected files were changed:"
    echo "$changed_files"
    exit 1
fi
git checkout HEAD -- "test_assets/2020/5. May/4. birthday/IMG-20161121-WA0001.jpg"
git checkout HEAD -- "test_assets/2020/5. May/4. birthday/IMG-20210920-WA0001.jpg"
git checkout HEAD -- "test_assets/IMG-20161121-WA0001.jpg"

echo "Test 'pics-org edit set-exif-date-to-best-guess' without overwrite happy path"
pics-org edit set-exif-date-to-best-guess ./test_assets
changed_files=$(git diff --name-only test_assets)
expected_changed_files="test_assets/2020/5. May/4. birthday/IMG-20161121-WA0001.jpg"
if [ "$changed_files" == "$expected_changed_files" ]; then
    echo "Test passed: No files were changed as expected."
else
    echo "Test failed: Unexpected files were changed:"
    echo "$changed_files"
    exit 1
fi

echo "Test 'pics-org edit set-exif-date-to-best-guess' with two images"
pics-org edit set-exif-date-to-best-guess --overwrite \
    "./test_assets/2020/5. May/4. birthday/IMG-20161121-WA0001.jpg" \
    "./test_assets/2020/5. May/4. birthday/IMG-20210920-WA0001.jpg"
changed_files=$(git diff --name-only test_assets)
expected_changed_files="test_assets/2020/5. May/4. birthday/IMG-20161121-WA0001.jpg
test_assets/2020/5. May/4. birthday/IMG-20210920-WA0001.jpg"
if [ "$changed_files" == "$expected_changed_files" ]; then
    echo "Test passed: Only the expected files were changed."
else
    echo "Test failed: Unexpected files were changed:"
    echo "$changed_files"
    exit 1
fi
git checkout HEAD -- "test_assets/2020/5. May/4. birthday/IMG-20161121-WA0001.jpg"
git checkout HEAD -- "test_assets/2020/5. May/4. birthday/IMG-20210920-WA0001.jpg"

# Final cleanup to ensure no files are left changed after the tests
git checkout HEAD -- test_assets

echo "All end-to-end tests passed successfully!"