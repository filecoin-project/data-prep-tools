# Car generation + commp calculation

This benchmark measured time for car generation + commp calculation. 

For car-generating tools such as [ipfs-car](https://github.com/web3-storage/ipfs-car) and [go-car](https://github.com/ipld/go-car), the resulting car file was streamed to [stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash) to calculate commp.


Whereas, [generate-car](https://github.com/tech-greedy/generate-car) does both -- generating car and calculating commP at once. 

[delta](https://github.com/application-research/delta) calculates commp but does not generate car file.

![Car generation + commp calculation performance_ 20230311 (2)](https://user-images.githubusercontent.com/1911631/224515505-81ebc68b-1f95-429e-90dd-57e5fb49858e.png)

The following graph is same as above, but excluding delta to make the graph easier to read beyond 8G.

![Car generation + commp calculation performance_ 20230311 (excluding delta)](https://user-images.githubusercontent.com/1911631/224515506-dd5ab62b-a672-4452-b481-24ba167cf1f5.png)


Raw data
| Payload size (GB)	| ipfs-car + stream-commp |	ipfs-car-streaming + stream-commp |	go-car + stream-commp	| streaming (wip) |	generate-car |	delta |
| ------------------|-------------------------|-----------------------------------|-----------------------|-----------------|--------------|--------|
| 1	                | 4.102	                  | 3.1835                            |	2.772                 |	1.818           |	3.5095       |	1.771 |
| 2	                | 11.0375                 |	6.206                             |	5.5045                |	3.7365          |	7.2055       |	3.3805|
| 4	                | 19.7685	                | 12.2275                           |	10.885                |	7.236           |	14.31        |	6.742 |
| 5	                | 27.441                  |	15.449                            |	13.886                |	9.519           |	18.0255      |	8.293 |
| 8	                | 48.2735                 |	24.782                            |	22.447                |	14.3815         |	28.6355      |	33.393 |
| 16                |	93.608                  |	49.347                            |	43.0295               |	27.942          |	57.7495      |	458.383 |
