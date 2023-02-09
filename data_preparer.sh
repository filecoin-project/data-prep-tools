#!/usr/bin/env bash

# Helper functions

chdir() { DIR=$1
  echo "Changing directory to $DIR"
  cd $DIR
}

find_files() {
  SIZE=$1

  find . -type f -size ${SMALL_OR_LARGE}${SIZE}

}

find_small_files() {
  SIZE=$1
  SMALLER_THAN="-"

  find_files ${SMALLER_THAN}${SIZE}
}

find_large_files() {
  SIZE=$1
  LARGER_THAN="+"

  find_files ${LARGER_THAN}${SIZE}
}

split_large_files() {
  SIZE=$1
  echo "Splitting up files larger than $SIZE into smaller chunks"
  find_large_files $SIZE  | xargs -I {} -t split -d -a 5 -b "$SIZE" {} "{}_part__"
  echo "Done splitting files"

}

generate_car() {
  FILE=$1
  echo "Generating car file for $FILE"
  car c  --version 1 -f ${FILE}.car $FILE
  echo "Done generating car file for $FILE"
}


## Main flow

DATADIR=$1
SIZE=$2
WORKDIR=$(pwd)

chdir $DATADIR

echo "Starting processing files"
echo

small_files=$(find_small_files "$SIZE")
large_files=$(find_large_files "$SIZE")

for file in $small_files
do
  generate_car $file
done

# Split large files
split_large_files $SIZE

echo "Done splitting large files"
echo

for file in $large_files
do
  for part_file in $(ls ${file}_part__*)
  do
    generate_car ${part_file}
  done
done


echo "Finished processing files"

chdir $WORKDIR

