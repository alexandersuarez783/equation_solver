from array import array
from typing import List, NamedTuple


class Term(NamedTuple):
    coefficient: float
    exponent: float


class NumericMethodContext:
    lower_boundary: float
    upper_boundary: float
    equation: List[Term] = list()
    tolerance: float
    max_iterations: int

    def __init__(self, terms: array):
        for index, term in enumerate(terms):
            self.equation.append(Term(coefficient=term, exponent=index))
            self.lower_boundary = -1000
            self.upper_boundary = 1000
            self.tolerance = 0.1
            self.roots = set()
            self.max_iterations = 10000

