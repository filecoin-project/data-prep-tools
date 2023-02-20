from abc import ABC, abstractmethod
from subprocess import run
import re


class CommPCalculator(ABC):

    @abstractmethod
    def calculate_commp(self, source_file):
        pass


class StreamCommP(CommPCalculator):

    def __init__(self, calculator='stream-commp'):
        self.calculator = calculator

    def calculate_commp(self, source_file):
        with open(source_file, 'r') as car_file:
            proc = run(['./stream-commp'], stdin=car_file, capture_output=True, check=True, text=True)
            out = proc.stderr.strip()

            # extract commP value, DAG root CID, and CAR file version + corruption status
            commp_re = re.compile('CommPCid: (b[A-Za-z2-7]{58,})')
            root_cid_re = re.compile('Roots:\s+1\n\s+1: (b[A-Za-z2-7]{58,})')
            car_format_version_re = re.compile('(CARv\d+) detected')
            corrupt_re = re.compile('\*CORRUPTED\*')
            padded_piece_re = re.compile('Padded piece:\s+(\d+)\sbytes')
            unpadded_piece_re = re.compile('Unpadded piece:\s+(\d+)\sbytes')
            commp_m = commp_re.findall(out)
            root_cid_m = root_cid_re.findall(out)
            car_format_version_m = car_format_version_re.findall(out)
            corrupt = corrupt_re.match(out)
            padded_piece_m = padded_piece_re.findall(out)
            unpadded_piece_m = unpadded_piece_re.findall(out)

            # this can potentially blow up if output format changes
            assert commp_m and root_cid_m and car_format_version_m and padded_piece_m, proc.stderr

            assert not corrupt, proc.stderr

            commp = commp_m[0]
            root_cid = root_cid_m[0]
            car_format_version = car_format_version_m[0]
            padded_piece = padded_piece_m[0]
            unpadded_piece = unpadded_piece_m[0]
