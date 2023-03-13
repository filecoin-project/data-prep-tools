# Data preparation tools for Filecoin

These are a bunch of tools that could be used to prepare data in order to store it on [Filecoin](https://filecoin.io).

These tools are more akin to "orchestrators", i.e., they use other existing tools as
building blocks in order to build a full end-to-end data preparation pipeline.

They are organised according to the implementation language -- shell scripts are in `bash` directory, python scripts in `python` directory etc.

## Tools in the ecosystem

There are a lot of tools in the ecosystem that address different aspects of the data
onboarding pipeline. The following is a non-exhaustive list of these tools.

### Car generators

#### Go
- [ipld/go-car](https://github.com/ipld/go-car)


#### JS
- [ipfs-car](https://github.com/web3-storage/ipfs-car)
- [ipfs-car (streaming)](https://github.com/web3-storage/ipfs-car2)

### Car splitters

#### Go
- [go-carbites](https://github.com/alanshaw/go-carbites)

#### JS
- [carbites](https://github.com/nftstorage/carbites)

### CommP calculators

#### Go
- [stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash)



### Others

#### Go
- [generate-car](https://github.com/tech-greedy/generate-car) -- this tool generates car files and calculates commp at the same time.
- [carbites-commp](https://github.com/anjor/go-carbites-commp) -- this tool splits up an existing car file into smaller car files and calculates commp at the same time.

#### Python
- [dataprep_tools](https://github.com/anjor/dataprep_tools) -- this is a pypi package that encodes the basic
  steps in a data preparation pipeline. It is heavily used in the orchestrators written in
  python in this repository.

#### Rust
- [banyancomputer/dataprep](https://github.com/banyancomputer/dataprep) -- this tool handles encryption, compression, deduping and chunking. The output of this tool could then be carred etc and used for deal making.

## Tools/Orchestrators in this repository

### Bash

- [car-then-split](https://github.com/anjor/filecoin_data_prep_tools/tree/main/bash/car-then-split)
- :warning: [DO NOT USE, here for legacy reasons] [split-then-car](https://github.com/anjor/filecoin_data_prep_tools/tree/main/bash/split-then-car)

### Python
- [car-then-split](https://github.com/anjor/filecoin_data_prep_tools/tree/main/python/car-then-split)


## Performance Benchmarks

Find some performance benchmarks [here](./performance).

## Lead Maintainer

[Anjor](https://github.com/anjor)
