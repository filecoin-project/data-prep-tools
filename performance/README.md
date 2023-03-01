# Performance Benchmarks

The following benchmarks were done by generating files of varying sizes as follows:
```
dd if=/dev/urandom of=8G-payload.bin bs=1M count=8192
dd if=/dev/urandom of=4G-payload.bin bs=1M count=4096
```
etc.

The scripts in the scripts directory were used to benchmark as follows:
```
find . -name "*.bin" | xargs -I {} bash -c "echo {} && time ./generate-car-prep.sh {} && echo"
```

All of the benchmarks were carried out on a M1 Macbook Pro (8-core, 32G ram).

## Car generation

This benchmark only measured time for car generation.

![Car generation performance](https://user-images.githubusercontent.com/1911631/222182570-dcb926a9-ccad-4656-9e93-592e0c9c0603.png)

## Car generation + commp calculation

This benchmark measured time for car generation + commp calculation. In case of tools like `ipfs-car` and `go-car`, the resulting car file was streamed to [stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash) to calculate commp, whereas [generate-car](https://github.com/tech-greedy/generate-car) does both at once.

![Car generation + commp calculation performance](https://user-images.githubusercontent.com/1911631/222182642-1b6127e3-4420-4692-ae35-48412e7df6ce.png)
