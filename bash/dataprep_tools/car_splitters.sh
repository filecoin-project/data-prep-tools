#!/usr/bin/env bash
carbites() {
  FILE=$1
  SIZE=$2
  echo "Splitting car file for $FILE using carbites"
  /Users/anjor/repos/alanshaw/go-carbites/cmd/carbites split --size $SIZE $FILE
}
export -f carbites
