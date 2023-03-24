import glob
import json
import os
import subprocess
from abc import ABC, abstractmethod


class E2EDataPrep(ABC):

    @abstractmethod
    def prepare_data(self, data_dir, size, output, metadata):
        pass

    @abstractmethod
    def get_root_cid(self):
        pass


class FilDataPrep(E2EDataPrep):
    """
    FilDataPrep does full end to end data preparation for filecoin in a streaming fashion.

    Source: https://github.com/anjor/go-fil-dataprep
    """

    def __init__(self, bin='data-prep'):
        self.bin = bin
        self.root = None

    @staticmethod
    def _get_files(data_dir):
        for file in glob.glob(data_dir + "**/*r", recursive=True):
            if os.path.isfile(file):
                yield file

    def prepare_data(self, data_dir, size, output, metadata):
        files = self._get_files(data_dir)
        for file in files:
            generate_cmd = [self.bin, 'fil-data-prep', '--size', str(size), '--output', output, '--metadata', metadata]
            with open(file, 'r') as inp:
                pipe = subprocess.Popen(generate_cmd, stdin=inp, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

        _, std_err = pipe.communicate()
        self.root = json.loads(std_err)['cid']

    def get_root_cid(self):
        return self.root
