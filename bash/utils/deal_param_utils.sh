#!/usr/bin/env bash

source ./utils/splitter.sh

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
  output=$(cat $FILE | stream-commp 2>&1)

  commp=$(fetch_commp "$output")
  padded_piece_size=$(fetch_padded_piece_size "$output")
  parent_file=$(get_parent_file $FILE)

  echo $(date), $parent_file, $FILE, $commp, $padded_piece_size 
}

export -f run_stream_commp

