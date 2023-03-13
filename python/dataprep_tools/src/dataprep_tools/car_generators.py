import subprocess
from abc import ABC, abstractmethod
from os.path import dirname
from subprocess import check_call, check_output
import json


class CarGenerator(ABC):

    @abstractmethod
    def generate_car(self, source_file, output_file):
        pass

    @abstractmethod
    def get_root_cid(self, car_file):
        pass


class IpfsCar(CarGenerator):
    def __init__(self, generator='ipfs-car'):
        self.generator = generator

    def generate_car(self, source_file, output_file):
        check_call(
            [self.generator, '--wrapWithDirectory', 'false', '--pack', dirname(source_file), '--output', output_file])

    def get_root_cid(self, car_file):
        return check_output([self.generator, '--list-roots', car_file]).decode()


class IpldGoCar(CarGenerator):
    def __init__(self, generator='car'):
        self.generator = generator

    def generate_car(self, source_file, output_file):
        check_call([self.generator, 'create', '--version', '1', '-f', output_file, source_file])

    def get_root_cid(self, car_file):
        return check_output([self.generator, 'root', car_file]).decode()

class Anelace(CarGenerator):
    def __init__(self, generator='anelace'):
        self.generator = generator
        self.root = None

    def generate_car(self, source_file, output_file):
        generate_cmd = [
            self.generator,
            '--emit-stderr=roots-jsonl',
            '--emit-stdout=car-v1-stream'
        ]
        with open(source_file, 'r') as inp:
            with open(output_file, 'w') as car:
                pipe = subprocess.Popen(generate_cmd, stdin=inp, stdout=car, stderr=subprocess.PIPE)

        _, std_err = pipe.communicate()
        self.root = json.loads(std_err)['cid']

    def get_root_cid(self, car_file):
        return self.root
