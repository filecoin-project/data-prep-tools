#!/usr/bin/env bash

FILE=$1
car c --version 1 -f $FILE.car $FILE && cat $FILE.car | stream-commp
