from abc import ABC, abstractmethod


class IOutput(ABC):
    @abstractmethod
    def show(self):
        pass
