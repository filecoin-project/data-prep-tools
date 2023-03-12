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

## Benchmarks

- [Car generation](./benchmarks/car-generation.md)
- [Car generation + CommP calculation](./benchmarks/car-and-commp.md)

