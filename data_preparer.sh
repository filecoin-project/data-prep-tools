#!/usr/bin/env bash

# Source helper functions

source ./utils/file_utils.sh
source ./utils/splitter.sh
source ./utils/car_generators.sh
source ./utils/deal_param_utils.sh

## Main flow

DATADIR=$1
SIZE=$2
WORKDIR=$(pwd)
METADATA_FILE="__metadata.csv"

CAR_GENERATOR="ipld_go_car"

chdir $DATADIR

echo "Starting processing files"
echo

# Split large files
split_large_files $SIZE

echo "Done splitting large files"
echo

# Generate car files for small files
find_small_files $SIZE | xargs -I {} bash -c "${CAR_GENERATOR} {}"
echo

# Generate car files for large files
find_partial_files $SIZE | xargs -I {} bash -c "${CAR_GENERATOR} {}" 
echo

# Calculate commP for all car files
find_car_files | xargs -I {} bash -c "run_stream_commp {}" > "$METADATA_FILE"

echo "Finished processing files"

chdir $WORKDIR

