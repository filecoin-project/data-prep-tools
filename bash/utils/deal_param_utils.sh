#!/usr/bin/env bash

fetch_commp() {
  OUTPUT=$1
  echo $OUTPUT | grep -o "CommPCid.*" | tr -s ' ' | cut -d: -f2 | cut -d ' ' -f2
}

export -f fetch_commp

fetch_padded_piece_size() {
  OUTPUT=$1
  echo $OUTPUT | grep -o "Padded piece.*" | tr -s ' ' | cut -d: -f 2 | cut -d ' ' -f2
}

export -f fetch_padded_piece_size

run_stream_commp() {
  FILE=$1
  output=$(cat $FILE | stream-commp -d 2>&1)

  commp=$(fetch_commp "$output")
  padded_piece_size=$(fetch_padded_piece_size "$output")
  car_file_size=$(ls -l $FILE | awk '{print $5}')

  echo $(date), $FILE, $commp, $padded_piece_size, $car_file_size
}

export -f run_stream_commp

