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


chdir $DATADIR

echo "Starting processing files"
echo

# Generate car files for small files
echo "Generating car files for files smaller than "$SIZE
find_small_files ${SIZE}"c" | xargs -I {} bash -c "${CAR_GENERATOR} {}"
echo

# Generate car files for large files + split them + delete original file
echo "Generating car files for files larger than "$SIZE
find_large_files ${SIZE}"c" | xargs -I {} bash -c "${CAR_GENERATOR} {}"
find_large_car_files ${SIZE}"c" | xargs -I {} bash -c "${CAR_SPLITTER} {} $SIZE && rm {}"

# Calculate commP for all car files
echo "Calculating CommP for all files and writing them out to "$METADATA_FILE
find_all_car_files | xargs -I {} bash -c "run_stream_commp {}" > "$METADATA_FILE"

echo "Finished processing files"

chdir $WORKDIR
