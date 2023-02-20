#!/usr/bin/env python3

from car_generators import IpldGoCar
from car_splitters import Carbites
from commp_calculators import StreamCommP


class CarThenSplit():
    def __init__(self, car_generator, car_splitter, commp_calculator):
        self.car_generator = car_generator
        self.car_splitter = car_splitter
        self.commp_calculator = commp_calculator


if __name__ == '__main__':
    car_then_split = CarThenSplit(IpldGoCar, Carbites, StreamCommP)
