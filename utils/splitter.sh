#!/usr/bin/env bash

export PARTIAL_FILE_SUFFIX="_part__"

split_large_files() {
  SIZE=$1
  echo "Splitting up files larger than $SIZE into smaller chunks"
  find_large_files $SIZE  | xargs -I {} -t split -d -a 5 -b "$SIZE" {} "{}${PARTIAL_FILE_SUFFIX}"
  echo "Done splitting files"
}

find_partial_files() {
  SIZE=$1
  find . -type f -size ${SIZE} -name "*${PARTIAL_FILE_SUFFIX}*"
}

get_parent_file() {
  FILE=$1
  echo $FILE | sed "s/.car$//" | sed "s/$PARTIAL_FILE_SUFFIX[0-9]\{5\}$//"
}

export -f get_parent_file

