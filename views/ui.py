from abc import ABC, abstractmethod

class UI(ABC):
    @abstractmethod
    def write_out(self):
        pass
