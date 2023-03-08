# Performance Benchmarks

The following benchmarks were done by generating files of varying sizes as follows:
```
dd if=/dev/urandom of=8G-payload.bin bs=1M count=8192
dd if=/dev/urandom of=4G-payload.bin bs=1M count=4096
```
etc.

There is a handy script [generate_data.sh](./scripts/generate_data.sh) to generate data.

To test an individual tool, you can use the [test_tool.sh](./scripts/test_tool.sh) script:
```
./test_tool.sh go-car 1G-payload.bin
```

To test all the tools at once, you can use the [run_load_test.sh](./scripts/run_load_test.sh) script which tests all the tools for all the generated files at once.

All of the benchmarks were carried out on a M1 Macbook Pro (8-core, 32G ram).

## Car generation

This benchmark only measured time for car generation.

![Car generation performance](https://user-images.githubusercontent.com/1911631/222182570-dcb926a9-ccad-4656-9e93-592e0c9c0603.png)

## Car generation + commp calculation

This benchmark measured time for car generation + commp calculation. In case of tools like [ipfs-car](https://github.com/web3-storage/ipfs-car) and [go-car](https://github.com/ipld/go-car), the resulting car file was streamed to [stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash) to calculate commp, whereas [generate-car](https://github.com/tech-greedy/generate-car) does both at once. [delta](https://github.com/application-research/delta) calculates commp but does not generate car file.


![Car generation + commp calculation performance (2)](https://user-images.githubusercontent.com/1911631/222276892-187d6e2f-985f-4878-be3d-50ac14050e79.png)
