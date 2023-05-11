# Data preparation for Filecoin

## Overview of the storage mechanism

*Step 1: [Car generation](./tools/car-generators.md)*

In order to store data on the filecoin network, the data needs to be
represented[^dataRepresentation] in a specific way. 
Namely, the raw data needs to be transformed into what is called a
[Filecoin piece](https://spec.filecoin.io/#section-systems.filecoin_files.piece) -- this
is the main _unit of negotiation_ of data on the filecoin network.

![onboarding-pipeline](./images/onboarding-pipeline.png)

*Step 2: [CommP calculation](./tools/commp-calculators.md)*

Afer the data has been transformed into an IPLD dag and serialised into the CAR format, the piece cid or the CommP needs to be calculated. The
commP and the piece size is included in the [deal proposal](https://github.com/filecoin-project/go-state-types/blob/master/builtin/v9/market/deal.go#L202)
made by the client. 


At a basic level these two steps are all that's required from the client in order to store
data on the filecoin network. However, depending on the size of the data to be onboarded
additional transformations could be required. In the next two sections we discuss how to
handle large files[^largeFiles] and small files[^smallFiles].

### Large files

In filecoin, files must be smaller than the
[sector](https://spec.filecoin.io/systems/filecoin_mining/sector/)[^sector] in which they
are stored. As a result, any piece that is larger than the sector size needs to be split
into smaller pieces in order to make deals. There are [car splitting
tools](./tools/car-splitters-joiners.md) that can split a large car file into smaller car files.


So now the steps to make a deal are:

1. Car generation
2. Car splitting
3. CommP calculation

### Small files

Even though the storage protocol does not prevent a deal for a very small file, it is not
economically feasible for a storage provider to accept such a deal. Therefore in case the
client has a lot of small files it would be beneficial for them to aggregate these files
into a larger file before making a filecoin deal. There are [car joining
tools](./tools/car-splitters-joiners.md) that can combine multiple small car files into a large
car file.

So now the steps to make a deal are:

1. Car generation
2. Car joining
3. CommP calculation

## FAQs
1. [Payload cid vs Piece cid](./payload-piece-cid.md)

## Data preparation best practices

1. [Data preparation and retrieval patterns](./best-practices/data-preparation-and-retrieval.md)
2. [Car first, then split](./best-practices/car-first-then-split.md)

[^dataRepresentation]: [Data representation section from the filecoin spec.](https://spec.filecoin.io/#section-systems.filecoin_files.piece.data-representation)
[^largeFiles]: Files larger than the sector size.
[^sector]: At the time of the writing 32GiB and 64GiB sectors are supported, but 32GiB
sectors are more common.
[^smallFiles]: From a storage provider standpoint, a deal becomes economically viable only
for data scales above a certain threshold. As a result if the files to be stored are too
small, they need special handling.
