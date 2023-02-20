#!/usr/bin/env python3

from car_generators import IpldGoCar
from car_splitters import Carbites
from commp_calculators import StreamCommP


if __name__ == '__main__':
    car_generator = IpldGoCar()
    car_splitter = Carbites()
    commp_calculator = StreamCommP()

    # Get all files to be processed using derivermodule

    # Generate car files for all the items

    # Split all car files that are larger than a given size

    # Calculate commP for all files

    # Persist source_file -> (list of car files, corresponding commP) locally