from enum import Enum

class Type(Enum):
    Normal = 1
    Major = 2
    EndOfRoute = 3
    Interchange = 4

class Stop:
    def __init__(self, name, line, stop_type):
        self.name = name
        self.line = line
        self.stop_type = stop_type # major, end of route, or rail interchange
    

