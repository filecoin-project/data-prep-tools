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

Find some performance benchmarks [here](./performance).
