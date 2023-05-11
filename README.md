# Data preparation for Filecoin

This repository contains information about everything related to data preparation that is
required before onboarding data to [Filecoin](https://filecoin.io). This includes tooling,
documentation, and performance benchmarks.

The repository is split into 4 main sections:

1. [Docs](./docs): this section includes documentation explaining how data onboarding to
filecoin works, best practices and common pitfalls. It also contains links to available
tools in the ecosystem.
2. [Modules](./modules): the different data onboarding steps are encoded as modules
(written in python and bash) which could be easily imported and used in any data
onboarding pipeline.
3. [Orchestrators](./orchestrators): these are example scripts demonstrating how to import
and use the modules from the [modules section](./modules) to orchestrate data onboarding.
4. [Performance benchmarks](./performance): these include performance benchmarks for
different available tools.


## Other tools in the ecosystem

- [banyancomputer/dataprep](https://github.com/banyancomputer/dataprep) -- this tool handles encryption, compression, deduping and chunking. The output of this tool could then be carred etc and used for deal making.


## Lead Maintainer

[Anjor](https://github.com/anjor)
