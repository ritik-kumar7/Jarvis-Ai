# utils/base_solver.py
from abc import ABC, abstractmethod

class BaseSolver(ABC):
    @abstractmethod
    def handle(self, query: str, context: str = "") -> str:
        """Main method to handle the query"""
        pass