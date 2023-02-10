#!/usr/bin/env bash

generate_car() {
  FILE=$1
  echo "Generating car file for $FILE"
  car c  --version 1 -f ${FILE}.car $FILE
  echo "Done generating car file for $FILE"
}

export -f generate_car
