# Data preparation tools for Filecoin

These are a bunch of tools that could be used to prepare data in order to store it on [Filecoin](https://filecoin.io).

These tools are more akin to "orchestrators", i.e., they use other existing tools as
building blocks in order to build a full end-to-end data preparation pipeline.

They are organised according to the implementation language -- shell scripts are in `bash` directory, python scripts in `python` directory etc.



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


## Other tools in the ecosystem

- [banyancomputer/dataprep](https://github.com/banyancomputer/dataprep) -- this tool handles encryption, compression, deduping and chunking. The output of this tool could then be carred etc and used for deal making.


## Performance Benchmarks

Find some performance benchmarks [here](./performance).

## Lead Maintainer

[Anjor](https://github.com/anjor)
