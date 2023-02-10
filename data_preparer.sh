#!/usr/bin/env bash

# Source helper functions

source ./utils/file_utils.sh
source ./utils/splitter.sh
source ./utils/car_generators.sh

## Main flow

DATADIR=$1
SIZE=$2
WORKDIR=$(pwd)

chdir $DATADIR

echo "Starting processing files"
echo

# Split large files
split_large_files $SIZE

echo "Done splitting large files"
echo

# Generate car files for small files
find_small_files $SIZE | xargs -I {} bash -c "generate_car {}"

# Generate car files for large files
find_partial_files $SIZE | xargs -I {} bash -c "generate_car {}" 

echo "Finished processing files"

chdir $WORKDIR

