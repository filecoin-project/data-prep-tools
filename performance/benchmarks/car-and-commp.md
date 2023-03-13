# Car generation + commp calculation

This benchmark measured time for car generation + commp calculation. 

For car-generating tools such as [ipfs-car](https://github.com/web3-storage/ipfs-car) and [go-car](https://github.com/ipld/go-car), the resulting car file was streamed to [stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash) to calculate commp.


Whereas, [generate-car](https://github.com/tech-greedy/generate-car) does both -- generating car and calculating commP at once. 

[delta](https://github.com/application-research/delta) calculates commp but does not generate car file.

![Car generation + commp calculation performance_ 20230311 (2)](https://user-images.githubusercontent.com/1911631/224515505-81ebc68b-1f95-429e-90dd-57e5fb49858e.png)

The following graph is same as above, but excluding delta to make the graph easier to read beyond 8G.

![Car generation + commp calculation performance_ 20230311 (excluding delta)](https://user-images.githubusercontent.com/1911631/224515506-dd5ab62b-a672-4452-b481-24ba167cf1f5.png)


