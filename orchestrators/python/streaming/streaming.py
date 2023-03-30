from dataprep_tools.end_to_end import FilDataPrep

if __name__ == '__main__':
    # The data directory to be transformed into car files
    data_dir = '/Users/anjor/repos/filecoin-project/data-prep-tools/data/subdir2'
    # Target size for car files
    size = 100000
    # Car files will have names of the format <output>-<number>.car
    output = '/Users/anjor/repos/filecoin-project/data-prep-tools/data/out'
    # Path to metadata file where metadata is persists
    meta = '/Users/anjor/repos/filecoin-project/data-prep-tools/data/metadata.csv'

    # Instantiate the FilDataPrep class with the go-fil-dataprep binary
    f = FilDataPrep('/Users/anjor/repos/anjor/go-fil-dataprep/cmd/data-prep/data-prep')

    f.prepare_data(data_dir=data_dir, size=size, output=output, metadata=meta)

    root_cid = f.get_root_cid()

    print(root_cid)
