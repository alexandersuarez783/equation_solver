from typing import Set

from business.numeric_methods.base_numeric_method import BaseNumericMethod
from business.numeric_methods.context import NumericMethodContext
from business import NumericMethods


class Bisection(BaseNumericMethod):
    name = NumericMethods.BISECTION.value

    """
    Evaluates if there is a positive or negative value and then a value of contrary sign
    Then iterates over it until finding the closest value
    """

    def __init__(self, context: NumericMethodContext):
        super().__init__(context)

    def run(self):
        self.find_roots()
        return {
            self.name: {
                'roots': self.roots,
                'iterations': self.iterations
            },
        }

    def find_roots(self, roots=None, lower=None, upper=None):
        """
        :param roots:
        :param lower:
        :param upper:
        :return:
        """
        if self.iterations > self.context.max_iterations:
            return
        lower, roots, upper = self._validate_initial_data(lower, roots, upper)
        if abs(upper - lower) <= self.context.tolerance:
            return
        lower_value = self.calculate_equation_value(lower)
        if abs(lower_value) <= self.context.tolerance:
            self.roots.add(lower)
            return
        upper_value = self.calculate_equation_value(upper)
        if abs(upper_value) <= self.context.tolerance:
            self.roots.add(upper)
            return
        middle_point = (lower + upper) / 2
        if lower_value * upper_value >= 0:
            self.find_roots((middle_point) + self.context.tolerance, upper)
            self.find_roots(lower, (middle_point) - self.context.tolerance)
        self.__find_one_root(lower, upper)

    def __find_one_root(self, lower, upper):
        while lower <= upper:
            self.iterations += 1
            middle_point = (lower + upper) / 2
            middle_value = self.calculate_equation_value(middle_point)
            if abs(middle_value) <= self.context.tolerance:
                self.roots.add(middle_point)
                break
            if self.calculate_equation_value(lower) * middle_value < 0:
                upper = middle_point
            else:
                lower = middle_point
