from abc import ABC, abstractmethod
from subprocess import check_call


class CarSplitter(ABC):

    @abstractmethod
    def split_car(self, source_file, size):
        pass


class Carbites(CarSplitter):

    def __init__(self, splitter='carbites'):
        self.splitter = splitter

    def split_car(self, source_file, size):
        check_call([self.splitter, 'split', '--size', str(size), source_file])
