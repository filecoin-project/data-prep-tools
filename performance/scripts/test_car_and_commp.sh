#!/usr/bin/env bash

TIMEFORMAT=%R
TOOL=$1
FILE=$2

go-car() {
  FILE=$1
  echo -ne "go-car, ${FILE}, $(ls -lh $FILE | awk '{print $5}'), "
  time bash -c "car c --version 1 -f $FILE.car $FILE && cat $FILE.car | stream-commp" 2>&1 | grep real
}

ipfs-car() {
  FILE=$1
  echo -ne "ipfs-car, ${FILE}, $(ls -lh $FILE | awk '{print $5}'), "
  time bash -c "ipfs-car --pack $FILE --output $FILE.car && cat $FILE.car | stream-commp" 2>&1 | grep real
}

ipfs-car-streaming() {
  FILE=$1
  echo -ne "ipfs-car2, ${FILE}, $(ls -lh $FILE | awk '{print $5}'), "
  time bash -c "ipfs-car2 pack $FILE -o $FILE.car && cat $FILE.car | stream-commp" 2>&1 | grep real
}

streaming-wip() {
  FILE=$1
  echo -ne "streaming-wip, ${FILE}, $(ls -lh $FILE | awk '{print $5}'), "
  time bash -c "cat $FILE | ~/repos/anjor/anelace/cmd/anelace/anelace --ipfs-add-compatible-command="--cid-version=1"  --emit-stdout=car-v1-stream | tee $FILE.car | stream-commp" 2>&1 | grep real
}

generate-car() {
  FILE=$1
  echo -ne "generate-car, ${FILE}, $(ls -lh $FILE | awk '{print $5}'), "
  time bash -c "~/repos/tech-greedy/generate-car/generate-car --single -i $FILE -o . -p ." | grep real
}

delta() {
  FILE=$1
  echo -ne "delta, ${FILE}, $(ls -lh $FILE | awk '{print $5}'), "
  time bash -c "~/repos/application-research/delta/delta commp --file $FILE" | grep real
}


case $TOOL in

  go-car)
    go-car $FILE
    ;;

  ipfs-car)
    ipfs-car $FILE
    ;;

  ipfs-car-streaming)
    ipfs-car-streaming $FILE
    ;;

  streaming-wip)
    streaming-wip $FILE
    ;;

  generate-car)
    generate-car $FILE
    ;;

  delta)
    delta $FILE
    ;;

  *)
    echo "Unknown tool"
    exit 1
  ;;
esac
  
