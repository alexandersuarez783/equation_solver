from typing import Set

from business.numeric_methods.base_numeric_method import BaseNumericMethod
from business.numeric_methods.context import NumericMethodContext
from business import NumericMethods


class Secant(BaseNumericMethod):
    name = NumericMethods.SECANT.value

    """
    Gets the secant point between two random points
    See where it intercepts
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
        if lower_value * upper_value >= 0:
            self.find_roots(((lower + upper) / 2) + self.context.tolerance, upper)
            self.find_roots(lower, ((lower + upper) / 2) - self.context.tolerance)
        self.__find_one_root(lower, upper)

    def __find_one_root(self, lower, upper):
        while lower <= upper and self.iterations < self.context.max_iterations:
            self.iterations += 1
            secant_point = self.__find_secant_point(lower, upper)
            if secant_point is None:
                break
            secant_value = self.calculate_equation_value(secant_point)
            if abs(secant_value) <= self.context.tolerance:
                self.roots.add(secant_point)
                break
            lower = secant_point

    def __find_secant_point(self, lower, upper):
        lower_value, upper_value = self.calculate_equation_value(lower), self.calculate_equation_value(upper)
        if abs(upper_value - lower_value) <= 0:
            return
        return lower - (lower_value * ((upper - lower) / (upper_value - lower_value)))
