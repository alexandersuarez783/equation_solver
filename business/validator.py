import re


class Validator:

    def __init__(self):
        self.pattern = re.compile('([+-]?[^-+]+)')

    def is_equation_valid(self, equation_str):
        try:
            return re.search(self.pattern, equation_str)
        except Exception as e:
            return False
