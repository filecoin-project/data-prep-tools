#!/usr/bin/env bash


# Utility function to change directories + log
chdir() { 
  DIR=$1
  echo "Changing directory to $DIR"
  cd $DIR
}

# Private function to find files
find_files() {
  SIZE=$1
  find . -type f -size ${SMALL_OR_LARGE}${SIZE}
}

# Public functions to find small/large files
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

find_all_car_files() {
  find . -type f -name "*.car" 
}

find_large_car_files() {
  SIZE=$1
  find . -type f -size "+"${SIZE} -name "*.car"
}

