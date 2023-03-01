#!/usr/bin/env bash

# This is an example driver script to split files if necessary, generate car files and
# calculate commp in order to prepare data for filecoin deals.

# Source helper functions
source ../utils/file_utils.sh
source splitter.sh

# Source filecoin related utilities
source ../utils/car_generators.sh
source ../utils/car_splitters.sh
source ../utils/commp_calculators.sh


## Main flow

DATADIR=$1
SIZE=$2
WORKDIR=$(pwd)
METADATA_FILE="__metadata.csv"

CAR_GENERATOR="ipld_go_car"
COMMP_CALCULATOR="stream_commp"

chdir $DATADIR

echo "Starting processing files"
echo

# Split large files
split_large_files $SIZE
echo

# Generate car files for small files
echo "Generating car files for files smaller than "$SIZE
find_small_files $SIZE | xargs -I {} bash -c "${CAR_GENERATOR} {}"
echo

# Generate car files for large files
echo "Generating car files for files larger than "$SIZE
find_partial_files $SIZE | xargs -I {} bash -c "${CAR_GENERATOR} {}" 
echo

# Calculate commP for all car files
echo "Calculating CommP for all files and writing them out to "$METADATA_FILE
find_all_car_files | xargs -I {} bash -c "${COMMP_CALCULATOR} {}" > "$METADATA_FILE"

echo "Finished processing files"

chdir $WORKDIR

