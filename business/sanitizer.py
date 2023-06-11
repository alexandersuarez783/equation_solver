from array import array


class Sanitizer:

    def get_sanitized_equation_array(self, equation_str: str) -> array:
        equation_str_list = self.__get_equation_str_list(equation_str)
        equation_hash = self.__get_equation_hash(equation_str_list)
        equation_grade = sorted(equation_hash.keys(), reverse=True)[0]
        equation_array = array('f', [equation_hash.get(i, 0.0) for i in range(0, equation_grade + 1)])
        return equation_array

    def __get_equation_str_list(self, equation_str):
        equation_str = equation_str.replace('-', '+-') \
            .replace(' ', '') \
            .replace('**', '^')
        equation_str_list = equation_str.split('+')
        return equation_str_list

    def __get_equation_hash(self, equation_str_list):
        equation_hash = {}
        for term in equation_str_list:
            if '^' in term:
                alpha_numeric_coefficient, exponent = term.split('^')
                numeric_coefficient = alpha_numeric_coefficient.replace('x', '') or 1
                equation_hash[int(exponent)] = float(numeric_coefficient)
            elif 'x' in term:
                term = term.replace('x', '')
                linear_coefficient_exponent = 1
                equation_hash[linear_coefficient_exponent] = float(term)
            else:
                constant_coefficient_exponent = 0
                equation_hash[constant_coefficient_exponent] = float(term)
        return equation_hash
