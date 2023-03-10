#!/usr/bin/env python3

import csv
import os.path
import shutil
from datetime import datetime

from dataprep_tools.car_generators import IpldGoCar
from dataprep_tools.car_splitters import Carbites
from dataprep_tools.commp_calculators import StreamCommP
from dataprep_tools.utils.car_then_split import CarThenSplit

if __name__ == '__main__':
    data_dir = "/Users/anjor/repos/anjor/filecoin_data_prep_tools/data"
    metadata_file = os.path.join(data_dir, "__metadata.csv")
    car_then_split = CarThenSplit(
        data=data_dir,
        chunk_size=1000000000,
        car_generator=IpldGoCar(),  # IpldGoCar's generate_car function can take in a glob as data_dir
        car_splitter=Carbites("/Users/anjor/repos/alanshaw/go-carbites/cmd/carbites"),
        commp_calculator=StreamCommP()
    )

    car_file = "data.car"

    car_then_split.generate_car(data_dir, car_file)
    shutil.move(car_file, data_dir)
    os.chdir(data_dir)

    car_then_split.split_car(car_file)
    os.unlink(car_file)

    f = open(metadata_file, 'w')
    writer = csv.writer(f)
    writer.writerow(["timestamp", "original data", "car file", "piece cid", "padded piece size"])
    car_files = car_then_split.find_car_files()
    for car_file in car_files:
        deal_params = car_then_split.calculate_deal_params(car_file)
        row = [datetime.now(), data_dir, car_file, deal_params['commp'], deal_params['padded_piece']]

        writer.writerow(row)

    f.close()
