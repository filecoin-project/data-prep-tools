#!/usr/bin/env bash

# Source helper functions

source ../utils/file_utils.sh
source ../utils/car_utils.sh
source ../utils/deal_param_utils.sh


# Main flow
DATADIR=$1
SIZE=$2
WORKDIR=$(pwd)
METADATA_FILE="__metadata.csv"

CAR_GENERATOR="ipld_go_car"
CAR_SPLITTER="carbites"

TMP="./.tmp"


chdir $DATADIR

echo "Starting processing files"
echo

# Find all files to be processed and write them out to be used later
mkdir -p $TMP
find . -type f ! -path "${TMP}/*" > ${TMP}"/all_files"


# Generate car files
echo "Generating car files"
cat ${TMP}"/all_files" | xargs -I {} bash -c "${CAR_GENERATOR} {}"
echo

# Split car files
echo "Splitting car files"
cat ${TMP}"/all_files" | xargs -I {} bash -c "${CAR_SPLITTER} {}.car $SIZE"
echo

# Calculate commP for all car files
echo "Calculating CommP for all files and writing them out to "$METADATA_FILE
find_small_car_files $SIZE | xargs 
#find_small_car_files $SIZE | xargs -I {} bash -c "run_stream_commp {}" > "$METADATA_FILE"

echo "Finished processing files"

chdir $WORKDIR
