# import os
from typing import Set, Iterable
from os import walk

from prefect_implementation.detection.IDetectionAPI import IDetectionAPI


class FileDetector(IDetectionAPI):

    projectRoot = "../"

    def __init__(self, files_sources: Iterable[str]):
        self.files_sources = files_sources

    def detect_files(self) -> Iterable[str]:
        '''
        TODO napisati metodu za detekciju datoteka iz direktorija.
        Ocekivano ponašanje: u konstruktoru je specificirana lista direktorija iz kojih se učitavaju sve datoteke koje će se procesirati
        Datoteke se učitaju te metoda vraća listu ili set kao rezultat
        Bonus: može se dodatno ubaciti filtriranje gdje će se vraćati samo određeni tip datoteka (npr. .mf4 u ovom slučaju)
        '''

        res = list()
        visited_files = list()

        for target in self.files_sources :

            for (dirpath, dirnames, filenames) in walk(target) :
                for name in filenames :
                    if name[-4:] == ".mf4" and name not in visited_files :
                        res.append( dirpath + "/" + name)
                        visited_files.append(name)

        return res