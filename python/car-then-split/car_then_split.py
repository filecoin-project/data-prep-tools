#!/usr/bin/env python3

import csv
import glob
import os.path
import shutil
from datetime import datetime

from dataprep_tools.car_generators import IpfsCar
from dataprep_tools.car_splitters import Carbites
from dataprep_tools.commp_calculators import StreamCommP


class CarThenSplit:

    def __init__(self, data, chunk_size, car_generator,
                 car_splitter, commp_calculator):
        self.data_dir = data
        self.chunk_size = chunk_size
        self.car_generator = car_generator
        self.car_splitter = car_splitter
        self.commp_calculator = commp_calculator

    def find_small_files(self):
        for file in glob.glob(self.data_dir + "**/**", recursive=True):
            if os.path.isfile(file) and os.path.getsize(file) <= self.chunk_size:
                yield file

    def find_large_files(self):
        for file in glob.glob(self.data_dir + "**/**", recursive=True):
            if os.path.isfile(file) and os.path.getsize(file) > self.chunk_size:
                yield file

    def find_car_files(self):
        for file in glob.glob(self.data_dir + "**/*.car", recursive=True):
            if os.path.isfile(file):
                yield file

    def generate_car(self, file, output=None):
        if not output:
            output = file + ".car"
        self.car_generator.generate_car(file, output)

    def split_car(self, file):
        self.car_splitter.split_car(file, self.chunk_size)

    def calculate_deal_params(self, file):
        return self.commp_calculator.calculate_commp(file)


if __name__ == '__main__':
    data_dir = "/Users/anjor/repos/anjor/filecoin_data_prep_tools/data"
    metadata_file = os.path.join(data_dir, "__metadata.csv")
    car_then_split = CarThenSplit(
        data=data_dir,
        chunk_size=1000000000,
        car_generator=IpfsCar(),
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
