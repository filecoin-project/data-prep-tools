# Data preparation tools for Filecoin

These are a bunch of tools that could be used to prepare data in order to store it on [Filecoin](https://filecoin.io).

These tools are more akin to "orchestrators", i.e., they use other existing tools as
building blocks in order to build a full end-to-end data preparation pipeline.

They are organised according to the implementation language -- shell scripts are in `bash` directory, python scripts in `python` directory etc.

## Tools in the ecosystem

There are a lot of tools in the ecosystem that address different aspects of the data
onboarding pipeline. The following is a non-exhaustive list of these tools.

### Car generators

> These tools generate car files.

#### Go
- [ipld/go-car](https://github.com/ipld/go-car)
- [generate-car](https://github.com/tech-greedy/generate-car) -- this tool generates car files and calculates commp at the same time.


#### JS
- [ipfs-car](https://github.com/web3-storage/ipfs-car)
- [ipfs-car (streaming)](https://github.com/web3-storage/ipfs-car2)

---

### Car splitters/joiners

> These tools split large car files into smaller car files, or combine small large car files into a large car file.

#### Go
- [go-carbites](https://github.com/alanshaw/go-carbites)
- [carbites-commp](https://github.com/anjor/go-carbites-commp) -- this tool splits up an existing car file into smaller car files and calculates commp at the same time.


#### JS
- [carbites](https://github.com/nftstorage/carbites)

---

### CommP calculators

> These tools calculate commP.

#### Go
- [stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash)
- [carbites-commp](https://github.com/anjor/go-carbites-commp) -- this tool splits up an existing car file into smaller car files and calculates commp at the same time.
- [generate-car](https://github.com/tech-greedy/generate-car) -- this tool generates car files and calculates commp at the same time.


### Others

- [banyancomputer/dataprep](https://github.com/banyancomputer/dataprep) -- this tool handles encryption, compression, deduping and chunking. The output of this tool could then be carred etc and used for deal making.

## Tools/Orchestrators in this repository

### Modules
- [dataprep_tools-bash](./modules/dataprep_tools-bash) -- shell scripts that encode basic steps in a data prepration pipeline.
- [dataprep_tools-py](./modules/dataprep_tools-py) -- this is a pypi package that encodes the basic steps in a data preparation pipeline. 

### Orchestrators

#### Bash

- [car-then-split](./orchestrators/bash/car-then-split) -- this tool first generates a car file, then splits it into smaller car files.
- :warning: [DO NOT USE, here for legacy reasons]
  [split-then-car](./orchestrators/bash/split-then-car) -- this tool first splits a large file into smaller files, then generates car files for each of the split files.

#### Python

- [car-then-split](./orchestrators/python/car-then-split) -- this tool first generates a car file, then splits it into smaller car files. 



## Performance Benchmarks

Find some performance benchmarks [here](./performance).

## Lead Maintainer

[Anjor](https://github.com/anjor)
