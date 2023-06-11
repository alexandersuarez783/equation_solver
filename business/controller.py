from business.sanitizer import Sanitizer
from .service import Service
from .validator import Validator


class Controller:

    def __init__(self):
        self.sanitizer = Sanitizer()
        self.validator = Validator()
        self.service = Service()

    def calculate_equations(self, equation_str):
        if not self.validator.is_equation_valid(equation_str):
            raise ValueError
        equation = self.sanitizer.get_sanitized_equation_array(equation_str)
        return self.service.calculate_roots_by_all_methods(equation)

    def get_function_values(self, equation_str:str):
        if not self.validator.is_equation_valid(equation_str) or not equation_str:
            return list(), list()
        equation = self.sanitizer.get_sanitized_equation_array(equation_str)
        return self.service.get_function_values_in_range(equation)
