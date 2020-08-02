from abc import ABC, abstractmethod


class IModerator(ABC):
    @abstractmethod
    def moderate(self):
        pass
