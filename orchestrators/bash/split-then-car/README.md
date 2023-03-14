# :warning: Do not use this method to prepare data if you don't know what you are doing.

# split-then-car

The script `split-then-car.sh`, splits large files into smaller chunks, generates CAR files, calculates commP and then persists metadata into a csv.
It does so in the following order:

  1. Splits large files into smaller chunks.
  2. Generates [CAR files](https://ipld.io/specs/transport/car/) for each of those smaller chunks.
  3. Calculates [CommP (piece cid)](https://spec.filecoin.io/systems/filecoin_files/piece/) for each of the generated car files.
  4. Persists metadata about original file, partial file (if split), CommP and padded piece size to a csv file, which can then be used to make storage deals on filecoin.

## Using the tool

The data preparation tool may be used either as a standalone tool or using docker. 

### Running the script directly

This method requires your preferred car generator, for example
[ipld/go-car](https://github.com/ipld/go-car) to be installed and in path. It also requires
[stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash/tree/master/cmd/stream-commp)
to be installed and in path.

The `split-then-car.sh` script is the main driver script. It takes two arguments -- the
directory where the raw data is hosted, and the preferred size of chunks. 

You can run the script using the command below.

```shell
/path/to/split-then-car.sh <data folder> <size, for example 1G>
```
### Using docker 

This method of using the tool requires [Docker](https://docs.docker.com/get-docker/) to be
installed. To build the image, from the project directory, run the docker build command
below.

```shell
docker build -t split-then-car .
```
Once completed, you should see a new image created named split-then-car.
```shell
docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
split-then-car       latest    84812c960e53   8 seconds ago   1.06GB
```

To prepare data, run the following command.
```shell
docker run -v /Users/anjor/repos/anjor/data_preparation_tool/data:/data split-then-car /bin/split-then-car.sh /data 2G
```

this mounts the local directory `/Users/anjor/repos/data_preparation_tool/data` to `/data`
on the container. Then it runs the `split-then-car.sh` script as outlined in the previous section.

