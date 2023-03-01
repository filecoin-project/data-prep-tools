#!/usr/bin/env bash

dd if=/dev/urandom of=1G-payload.bin bs=1M count=1024
dd if=/dev/urandom of=2G-payload.bin bs=1M count=2048
dd if=/dev/urandom of=4G-payload.bin bs=1M count=4096
dd if=/dev/urandom of=5G-payload.bin bs=1M count=5200
dd if=/dev/urandom of=8G-payload.bin bs=1M count=8192
