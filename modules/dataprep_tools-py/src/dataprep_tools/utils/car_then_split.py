import glob
import os


class CarThenSplit:

    def __init__(self, data, chunk_size, car_generator,
                 car_splitter, commp_calculator):
        self.data_dir = data
        self.chunk_size = chunk_size
        self.car_generator = car_generator
        self.car_splitter = car_splitter
        self.commp_calculator = commp_calculator

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
