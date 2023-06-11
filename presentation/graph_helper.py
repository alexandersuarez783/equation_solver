from business.controller import Controller
from matplotlib.figure import Figure


class GraphHelper:


    def __init__(self):
        self.__controller = Controller()


    def update_graph(self, equation_str, figure):
        figure.clf()
        axes = figure.add_axes([0.15, 0.15, 0.7, 0.7])
        x_values, y_values = self.__controller.get_function_values(equation_str)
        axes.plot(x_values, y_values)
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        axes.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')
        axes.spines['left'].set_position('zero')
        axes.spines['right'].set_color('none')
        axes.spines['bottom'].set_position('zero')
        axes.spines['top'].set_color('none')
        axes.spines['top'].set_visible(False)
        axes.spines['right'].set_visible(False)
        axes.set_title('Function Graph')
