# car-then-split

The script `car-then-split.sh`, generates CAR files, then splits large car files into smaller car files, generates CAR files, calculates commP and then persists metadata into a csv.  

It does so in the following order:

  1. Generates [CAR files](https://ipld.io/specs/transport/car/) for each of those smaller chunks.
  2. Splits large car files into smaller car files using [carbites](https://github.com/alanshaw/go-carbites).
  3. Calculates [CommP (piece cid)](https://spec.filecoin.io/systems/filecoin_files/piece/) for each of the generated car files.
  4. Persists metadata about original file, partial file (if split), CommP and padded piece size to a csv file, which can then be used to make storage deals on filecoin.

## Using the tool

The data preparation tool may be used either as a standalone tool or using docker. 

### Running the script directly

This method requires your preferred car generator, for example
[ipld/go-car](https://github.com/ipld/go-car) to be installed and in path. It also requires
[stream-commp](https://github.com/filecoin-project/go-fil-commp-hashhash/tree/master/cmd/stream-commp)
and [carbites](https://github.com/alanshaw/go-carbites)
to be installed and in path.

The `car-then-split.sh` script is the main driver script. It takes two arguments -- the
directory where the raw data is hosted, and the preferred size of chunks (in bytes). 

You can run the script using the command below.

```shell
/path/to/car-then-split.sh <data folder> <size, for example 1000000000>
```
### Using docker 

This method of using the tool requires [Docker](https://docs.docker.com/get-docker/) to be
installed. To build the image, from the project directory, run the docker build command
below.

```shell
docker build -t car-then-split .
```
Once completed, you should see a new image created named car-then-split.
```shell
docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
car-then-split       latest    84812c960e53   8 seconds ago   1.06GB
```

To prepare data, run the following command.
```shell
docker run -v /Users/anjor/repos/anjor/data_preparation_tool/data:/data car-then-split /bin/car-then-split.sh /data 2000000000
```

this mounts the local directory `/Users/anjor/repos/data_preparation_tool/data` to `/data`
on the container. Then it runs the `car-then-split.sh` script as outlined in the previous section.

