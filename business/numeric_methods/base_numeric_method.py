from typing import Set, Dict


class BaseNumericMethod:
    name: str
    iterations: int

    def __init__(self, context):
        self.context = context
        self.roots = set()
        self.iterations = 0

    def run(self):
        ...

    def find_roots(self)-> Dict[str, Set]:
        ...

    def calculate_equation_value(self, variable: float) -> float:
        result = 0
        for coefficient, exponent in self.context.equation:
            result += coefficient * pow(variable, exponent)
        return result

    def _validate_initial_data(self, lower, roots, upper):
        if roots is None:
            roots = set()
        if lower is None:
            lower = self.context.lower_boundary
        if upper is None:
            upper = self.context.upper_boundary
        return lower, roots, upper