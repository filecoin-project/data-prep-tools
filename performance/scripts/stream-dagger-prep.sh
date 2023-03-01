#!/usr/bin/env bash

FILE=$1
cat $FILE | ~/repos/ribasushi/DAGger/bin/stream-dagger --ipfs-add-compatible-command="--cid-version=1"  --emit-stdout=car-v0-pinless-stream | tee $FILE.car | stream-commp
