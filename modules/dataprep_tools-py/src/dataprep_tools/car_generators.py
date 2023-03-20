import subprocess
from abc import ABC, abstractmethod
from os.path import dirname
from subprocess import check_call, check_output
import json


class CarGenerator(ABC):
    """
    A car generator generates a CAR (Content Addressable aRchive) file.
    """

    @abstractmethod
    def generate_car(self, source, output_file):
        """
        Function to generate a car file.
        
        :param source: Path to source data.
        :param output_file: Path where the output car file should be written.
        """
        pass

    @abstractmethod
    def get_root_cid(self, car_file):
        """
        Function to get the root payload cid of the generated car file.

        :param car_file: Input car file from which to get the root cids.
        :return:
        """
        pass


class IpfsCar(CarGenerator):
    """
    ipfs-car is a tool written in JS used to prepare car files.

    Source: https://github.com/web3-storage/ipfs-car
    """
    def __init__(self, generator='ipfs-car'):
        self.generator = generator

    def generate_car(self, source, output_file):
        check_call(
            [self.generator, '--wrapWithDirectory', 'false', '--pack', dirname(source), '--output', output_file])

    def get_root_cid(self, car_file):
        return check_output([self.generator, '--list-roots', car_file]).decode()


class IpldGoCar(CarGenerator):
    """
    ipld/go-car is a tool written in go used to prepare car files.

    Source: https://github.com/ipld/go-car
    """

    def __init__(self, generator='car'):
        self.generator = generator

    def generate_car(self, source, output_file):
        check_call([self.generator, 'create', '--version', '1', '-f', output_file, source])

    def get_root_cid(self, car_file):
        return check_output([self.generator, 'root', car_file]).decode()


class Anelace(CarGenerator):
    """
    Anelace is a tool written in go used to prepare car files, that works well with streaming data.

    Source: https://github.com/anjor/anelace
    """
    def __init__(self, generator='anelace'):
        self.generator = generator
        self.root = None

    def generate_car(self, source, output_file):
        generate_cmd = [
            self.generator,
            '--emit-stderr=roots-jsonl',
            '--emit-stdout=car-v1-stream'
        ]
        with open(source, 'r') as inp:
            with open(output_file, 'w') as car:
                pipe = subprocess.Popen(generate_cmd, stdin=inp, stdout=car, stderr=subprocess.PIPE)

        _, std_err = pipe.communicate()
        self.root = json.loads(std_err)['cid']

    def get_root_cid(self, car_file):
        return self.root
