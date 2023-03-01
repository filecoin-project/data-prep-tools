#!/usr/bin/env bash

FILE=$1
~/repos/tech-greedy/generate-car/generate-car --single -i $FILE -o . -p . | jq
