# Data preparation tools for Filecoin

These are a bunch of tools that could be used to prepare data in order to store it on [Filecoin](https://filecoin.io).

These tools are more akin to "orchestrators", i.e., they use other existing tools as
building blocks in order to build a full end-to-end data preparation pipeline.

They are organised according to the implementation language -- shell scripts are in `bash` directory, python scripts in `python` directory etc.

## Tools/Orchestrators in this repository

### Bash

- [car-then-split](https://github.com/anjor/filecoin_data_prep_tools/tree/main/bash/car-then-split)
- :warning: [DO NOT USE, here for legacy reasons] [split-then-car](https://github.com/anjor/filecoin_data_prep_tools/tree/main/bash/split-then-car)

### Python
- [car-then-split](https://github.com/anjor/filecoin_data_prep_tools/tree/main/python/car-then-split)

## Other tools in the ecosystem

There are a few other tools in the ecosystem which may also be used for data preparation
and might be better suited for the specific circumstances.

### Rust
- https://github.com/banyancomputer/dataprep -- this tool handles encryption, compression, deduping and chunking. The output of this tool could then be carred etc and used for deal making.

### Go
- https://github.com/tech-greedy/generate-car -- this tool generates car files and calculates commp at the same time.
- https://github.com/anjor/go-carbites-commp -- this tool splits up an existing car file into smaller car files and calculates commp at the same time.

### Python
- https://github.com/anjor/dataprep_tools -- this is a pypi package that encodes the basic
  steps in a data preparation pipeline. It is heavily used in the orchestrators written in
  python in this repository.

## Performance Benchmarks

Find some performance benchmarks [here](./performance).
