from abc import ABC, abstractmethod


class ListStrategy(ABC):
    @abstractmethod
    def generate_list(self, *args):
        pass
