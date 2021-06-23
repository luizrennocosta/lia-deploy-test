from abc import ABC, abstractmethod
from unicodedata import normalize


class BaseRule(ABC):
    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def refactor(self):
        pass

    def pt_normalize(self, word):
        return normalize("NFKD", word).encode("ASCII", "ignore").decode("ASCII")