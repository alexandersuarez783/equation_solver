from array import array
from typing import List, Dict, Set, Tuple, Union, Iterable

from business.numeric_methods.base_numeric_method import BaseNumericMethod
from business.numeric_methods.bisection import Bisection
from business.numeric_methods.context import NumericMethodContext
from business.numeric_methods.false_position import FalsePosition
from business.numeric_methods.secant import Secant
from copy import copy


class Service:
    __NUMERIC_METHODS: List[BaseNumericMethod] = [Bisection, FalsePosition, Secant]

    def calculate_roots_by_all_methods(self, equation=array("f", [-30000, 0, 1])):
        numeric_method_results: Dict = dict()
        context = NumericMethodContext(equation)
        for numeric_method in self.__NUMERIC_METHODS:
            numeric_method_results = numeric_method_results | numeric_method(copy(context)).run()

        self.__round_roots(numeric_method_results)
        return numeric_method_results

    def get_function_values_in_range(self, equation: Iterable[float], *, lower:int=-100, upper:int=100) -> Tuple[
        List[int], List[float]]:
        x_values, y_values = list(), list()
        context = NumericMethodContext(equation)
        base_numeric_method = BaseNumericMethod(context)
        for x in range(lower, upper + 1):
            y = base_numeric_method.calculate_equation_value(x)
            x_values.append(x)
            y_values.append(y)
        return x_values, y_values



    def __round_roots(self, numeric_method_results):
        for name in numeric_method_results.keys():
            numeric_method_results[name]['roots'] = {round(root, 2) for root in numeric_method_results[name]['roots']}














