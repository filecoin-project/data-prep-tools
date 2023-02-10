#!/usr/bin/env bash

split_large_files() {
  SIZE=$1
  echo "Splitting up files larger than $SIZE into smaller chunks"
  find_large_files $SIZE  | xargs -I {} -t split -d -a 5 -b "$SIZE" {} "{}_part__"
  echo "Done splitting files"
}

find_partial_files() {
  find . -type f -name '*_part__*'
}
