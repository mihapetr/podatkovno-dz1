import os
import pickle
from pprint import pprint
from typing import Iterable

from pandas import DataFrame

from processing.calculators import YourCalculator
from processing.models import Event, Results


def get_events(df: DataFrame, file_path: str) -> Iterable[Event]:
    '''
    TODO implementirati logiku za detekciju evenata
    '''


def get_dataframe_from_mf4(file_path: str) -> DataFrame:
    #TODO implementirati logiku za učitavanje mdf datoteka u dataframe koji se zove dataframe
    return None

def processing_flow_logic(filepath: str, result_output_path: str):
    dataframe = get_dataframe_from_mf4(filepath)
    events = get_events(df=dataframe, file_path=filepath)
    calculator = YourCalculator()

    calculated = {}
    for event in events:
        try:
            calculated[hash(event)] = calculator.calculate(dataframe, event)
        except Exception:
            print(f"Could not calculate for event on file {event.file}!")
            pass

    result = Results()
    result.events = events
    result.calculations = calculated

    with open(f'{result_output_path}/{filepath.split("/")[-1]}.pickle', 'wb') as handle:
        pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)
