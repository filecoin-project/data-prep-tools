from abc import ABC, abstractmethod
from os.path import dirname
from subprocess import check_call


class CarGenerator(ABC):

    @abstractmethod
    def generate_car(self, source_file, output_file):
        pass


class IpfsCar(CarGenerator):
    def __init__(self, generator='ipfs-car'):
        self.generator = generator

    def generate_car(self, source_file, output_file):
        check_call([self.generator, '--wrapWithDirectory', 'false', '--pack', dirname(source_file), '--output', output_file])


class IpldGoCar(CarGenerator):
    def __init__(self, generator='car'):
        self.generator = generator

    def generate_car(self, source_file, output_file):
        check_call([self.generator, 'create', '--version', '1', '-f', output_file, source_file])
