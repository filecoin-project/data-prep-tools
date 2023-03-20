# Data preparation for Filecoin

## Overview of the storage mechanism

Step 1: [Car generation](./car-generators.md)

In order to store data on the filecoin network, the data needs to be
represented[^dataRepresentation] in a specific way. 
The raw data needs to be transformed into what is called a
[Filecoin piece](https://spec.filecoin.io/#section-systems.filecoin_files.piece) -- this
is the main _unit of negotiation_ of data on the filecoin network.


Step 2: [CommP calculation](./commp-calculators.md)
Afer the data has been transformed into the CAR format, the piece cid or the CommP needs to be calculated. The
commP and the piece size is included in the [deal proposal](https://github.com/filecoin-project/go-state-types/blob/master/builtin/v9/market/deal.go#L202)
made by the client. 


At a basic level these two steps are all that's required from the client in order to store
data on the filecoin network. However, as we will find out in the next couple of sections
there are situations that require further transformation steps.

### Large files

In filecoin, files must be smaller than the
[sector](https://spec.filecoin.io/systems/filecoin_mining/sector/)[^sector] in which they
are stored. As a result, any piece that is larger than the sector size needs to be split
into smaller pieces in order to make deals. There are [car splitting
tools](./car-splitters-joiners.md) that can split a large car file into smaller car files.


So now the steps to make a deal are:

1. Car generation
2. Car splitting
3. CommP calculation



## Data preparation best practices

1. [Car first, then split](./car-first-then-split.md)

[^dataRepresentation] [Data representation section from the filecoin spec.](https://spec.filecoin.io/#section-systems.filecoin_files.piece.data-representation)
[^sector] At the time of the writing 32GiB and 64GiB sectors are supported, but 32GiB
sectors are more common.
