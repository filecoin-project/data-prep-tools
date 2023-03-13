#!/usr/bin/env bash

# This is an example driver script to generate car files, split them if necessary and
# calculate commp in order to prepare data for filecoin deals.

# Source helper functions
source ../dataprep_tools/file_utils.sh

# Source filecoin related utilities
source ../dataprep_tools/car_generators.sh
source ../dataprep_tools/car_splitters.sh
source ../dataprep_tools/commp_calculators.sh


# Main flow
DATADIR=$1
SIZE=$2
WORKDIR=$(pwd)
METADATA_FILE="__metadata.csv"

# Choose data preparation utilities
CAR_GENERATOR="ipld_go_car"
CAR_SPLITTER="carbites"
COMMP_CALCULATOR="stream_commp"


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
find_all_car_files | xargs -I {} bash -c "${COMMP_CALCULATOR} {}" > "$METADATA_FILE"

echo "Finished processing files"

chdir $WORKDIR
