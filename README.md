# Data preparation tools for Filecoin

These are a bunch of tools that could be used to prepare data in order to store it on [Filecoin](https://filecoin.io).

They are organised according to the implementation language -- shell scripts are in `bash` directory, python scripts in `python` directory etc.

## Bash

- [split-then-car](https://github.com/anjor/filecoin_data_prep_tools/tree/main/bash/split-then-car)
- [car-then-split](https://github.com/anjor/filecoin_data_prep_tools/tree/main/bash/car-then-split)

## Python
- [car-then-split](https://github.com/anjor/filecoin_data_prep_tools/tree/main/python/car-then-split)

## Other tools in the ecosystem

There are a few other tools in the ecosystem which may also be used for data preparation
and might be better suited for the specific circumstances.

### Rust
- https://github.com/banyancomputer/dataprep -- this tool handles encryption, compression, deduping and chunking. The output of this tool could then be carred etc and used for deal making.

### Go
- https://github.com/tech-greedy/generate-car -- this tool generates car files and calculates commp at the same time.

## Performance Benchmarks

The following benchmarks were done by generating files of varying sizes as follows:
```
dd if=/dev/urandom of=8G-payload.bin bs=1M count=8192
dd if=/dev/urandom of=4G-payload.bin bs=1M count=4096
```
etc.

All of the benchmarks were carried out on a M1 Macbook Pro (8-core, 32G ram).

### Car generation

This benchmark only measured time for car generation.

![Car generation performance](https://user-images.githubusercontent.com/1911631/222182570-dcb926a9-ccad-4656-9e93-592e0c9c0603.png)

### Car generation + commp calculation

This benchmark measured time for car generation + commp calculation. In case of tools like `ipfs-car` and `go-car`, the resulting car file was streamed to [stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash) to calculate commp, whereas [generate-car](https://github.com/tech-greedy/generate-car) does both at once.

![Car generation + commp calculation performance](https://user-images.githubusercontent.com/1911631/222182642-1b6127e3-4420-4692-ae35-48412e7df6ce.png)
