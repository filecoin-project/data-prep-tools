#!/usr/bin/env bash

ipld_go_car() {
  FILE=$1
  echo "Generating car file for $FILE using ipld/go-car"
  car c  --version 1 -f ${FILE}.car $FILE
  echo "Done generating car file for $FILE using ipld/go-car"
}
export -f ipld_go_car

stream_dagger() {
  FILE=$1
  echo "Generating car file for $FILE using stream-dagger" 
  cat $FILE | /Users/anjor/repos/ribasushi/DAGger/bin/stream-dagger --ipfs-add-compatible-command="--cid-version=1" --emit-stdout=car-v0-pinless-stream > ${FILE}.car
  echo "Done generating car file for $FILE using stream-dagger"
}
export -f stream_dagger

