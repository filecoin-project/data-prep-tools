#!/usr/bin/env bash

for tool in go-car ipfs-car streaming-wip generate-car delta
do
  find . -name "*.bin" | xargs -I {} ./test_car_and_commp.sh $tool {}
done
