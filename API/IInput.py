from abc import ABC, abstractmethod


class IInput(ABC):
    @abstractmethod
    def get_data(self):
        pass
