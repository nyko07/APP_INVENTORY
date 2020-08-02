from abc import ABC, abstractmethod


class IRuler(ABC):
    @abstractmethod
    def verify_rulers(self):
        pass
