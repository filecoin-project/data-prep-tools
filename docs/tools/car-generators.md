# Car generators

These tools generate [car files](https://ipld.io/specs/transport/car/). Generating a car file involves constructing an [IPLD dag](https://ipld.io/docs/data-model/)
from raw data and then serialising it into a car file.

Except for [anelace](https://github.com/anjor/anelace), all the tools listed below use
unixfs libraries - [golang](https://github.com/ipfs/go-unixfs) or
[js](https://github.com/ipfs/js-ipfs-unixfs) to generate the IPLD dag, which is
subsequently serialised into a car file.

Anelace has its own custom implementation for the dag generation.

## Go
- [ipld/go-car](https://github.com/ipld/go-car)
- [generate-car](https://github.com/tech-greedy/generate-car) -- this tool generates car files and calculates commp at the same time.
- [anelace](https://github.com/anjor/anelace)


## JS
- [ipfs-car](https://github.com/web3-storage/ipfs-car)
- [ipfs-car (streaming)](https://github.com/web3-storage/ipfs-car2)

