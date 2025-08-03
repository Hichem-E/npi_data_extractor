#!/bin/bash

URL="https://download.cms.gov/nppes/NPPES_Data_Dissemination_July_2025_V2.zip"
OUTPUT_FILENAME="NPPES_Data_Dissemination_July_2025_V2.zip"

# Attempt to download using curl
if command -v curl &>/dev/null; then
  echo "Using curl to download..."
  if [ -n "$OUTPUT_FILENAME" ]; then
    curl -L -o "$OUTPUT_FILENAME" "$URL"
  else
    curl -L -O "$URL"
  fi
  if [ $? -eq 0 ]; then
    echo "Download successful using curl."
    exit 0
  else
    echo "Curl download failed. Trying wget..."
  fi
elif command -v wget &>/dev/null; then
  echo "Using wget to download..."
  if [ -n "$OUTPUT_FILENAME" ]; then
    wget -O "$OUTPUT_FILENAME" "$URL"
  else
    wget "$URL"
  fi
  if [ $? -eq 0 ]; then
    echo "Download successful using wget."
    exit 0
  else
    echo "Wget download failed."
    exit 1
  fi
else
  echo "Neither curl nor wget found. Please install one of them."
  exit 1
fi