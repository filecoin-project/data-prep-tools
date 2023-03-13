#!/usr/bin/env bash

ipld_go_car() {
  FILE=$1
  echo "Generating car file for $FILE using ipld/go-car"
  car c  --version 1 -f ${FILE}.car $FILE
  echo "Done generating car file for $FILE using ipld/go-car"
}
export -f ipld_go_car

ipfs_car() {
  FILE=$1
  echo "Generating car file for $FILE using ipfs-car"
  ipfs-car --wrapWithDirectory false --pack $FILE --output ${FILE}.car
}
export -f ipfs_car


