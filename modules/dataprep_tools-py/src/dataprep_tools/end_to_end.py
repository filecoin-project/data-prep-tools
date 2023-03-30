import glob
import json
import os
import re
from subprocess import check_output
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

    def prepare_data(self, data_dir, size, output, metadata):
        generate_cmd = [self.bin, 'dp', '--size', str(size), '--output', output, '--metadata', metadata, data_dir]
        out = check_output(generate_cmd)
        out = out.decode().strip()

        rcid_re = re.compile(r'root cid = (\S+)')

        rcid = rcid_re.findall(out)

        self.root = rcid[0]

    def get_root_cid(self):
        return self.root
