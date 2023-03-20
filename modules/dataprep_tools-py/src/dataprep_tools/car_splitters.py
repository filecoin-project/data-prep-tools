from abc import ABC, abstractmethod
from subprocess import check_call


class CarSplitter(ABC):
    """
    A car splitter splits a CAR (Content Addressable aRchive) file into multiple small car files.
    """

    @abstractmethod
    def split_car(self, source_file, size):
        """
        Main function to split a car file.
        :param source_file: The car file to be split.
        :param size: Target size in bytes to chunk CARs to.
        """
        pass


class Carbites(CarSplitter):
    """"
    Carbites is a car splitter implemented in go.

    Source: https://github.com/alanshaw/go-carbites
    """

    def __init__(self, splitter='carbites'):
        self.splitter = splitter

    def split_car(self, source_file, size):
        check_call([self.splitter, 'split', '--size', str(size), source_file])
