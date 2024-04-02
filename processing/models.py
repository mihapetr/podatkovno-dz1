from typing import List, Dict
import hashlib


class Event:
    start: float
    end: float
    file: str

    def __str__(self):
        return f"event of start: {self.start}, and end: {self.end} on file: {self.file}"

    def __hash__(self):
        m = hashlib.md5()
        m.update(repr(self.start).encode())
        m.update(repr(self.end).encode())
        m.update(self.file.encode())
        return int(m.hexdigest(), 16)


class Results:
    events: List[Event]
    calculations: Dict[int, Dict[str, Dict[str, float]]]
