#!/usr/bin/env bash

FILE=$1
ipfs-car --pack $FILE --output $FILE.car && cat $FILE.car | stream-commp
