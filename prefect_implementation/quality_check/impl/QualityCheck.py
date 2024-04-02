from typing import List, Tuple, Iterable

from asammdf import MDF

from prefect_implementation.quality_check.IQualityCheck import IQualityCheck


class QualityCheck(IQualityCheck):
    def check_quality(self, paths: Iterable[str]) -> Tuple[List[str], List[str]]:

        good = []
        bad = []

        '''
        TODO napisati metodu za filtriranje fajlova.
        Ocekivano ponašanje: u konstruktoru je specificirana lista putanja do datoteka
        Datoteke koje se ne ponašaju u skladu sa očekivanim ponašanjem se vraćaju u listi loših datoteka
        Očekivani rezultat se treba vratiti kao tuple lista, lista, npr. ["a.txt", "b.txt"], ["c.txt"]
        '''
        for path in paths :

            try :
                temp = MDF(path)
                good.append(path)

            except:
                bad.append(path)

        return good, bad