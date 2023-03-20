from abc import ABC, abstractmethod
from subprocess import run
import re


class CommPCalculator(ABC):
    """
    A CommP Calculator calculates commP aka piece cid in order to make filecoin deals.
    """

    @abstractmethod
    def calculate_commp(self, source_file):
        """
        Main function to calculate commP.

        :param source_file: Source car file to calculate commP for.
        :return: a dict with commp, padded piece size and unpadded piece size. The keys are "commp", "padded_piece" and "unpadded_piece"
        """
        pass


class StreamCommP(CommPCalculator):

    def __init__(self, calculator='stream-commp'):
        self.calculator = calculator

    def calculate_commp(self, source_file):
        with open(source_file, 'r') as car_file:
            proc = run([self.calculator], stdin=car_file, capture_output=True, check=True, text=True)
            out = proc.stderr.strip()

            # extract commP value, DAG root CID, and CAR file version + corruption status
            commp_re = re.compile('CommPCid: (b[A-Za-z2-7]{58,})')
            corrupt_re = re.compile('\*CORRUPTED\*')
            padded_piece_re = re.compile('Padded piece:\s+(\d+)\sbytes')
            unpadded_piece_re = re.compile('Unpadded piece:\s+(\d+)\sbytes')

            commp_m = commp_re.findall(out)
            corrupt = corrupt_re.match(out)
            padded_piece_m = padded_piece_re.findall(out)
            unpadded_piece_m = unpadded_piece_re.findall(out)

            # this can potentially blow up if output format changes
            assert commp_m and padded_piece_m, proc.stderr

            assert not corrupt, proc.stderr

            commp = commp_m[0]
            padded_piece = padded_piece_m[0]
            unpadded_piece = unpadded_piece_m[0]

        return {
            "commp": commp,
            "padded_piece": padded_piece,
            "unpadded_piece": unpadded_piece
        }
