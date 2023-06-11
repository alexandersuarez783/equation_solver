import tkinter as tk
from tkinter import messagebox, DISABLED

import matplotlib
from business import NumericMethods
from business.controller import Controller
from matplotlib.figure import Figure
from presentation.graph_helper import GraphHelper

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)


class AppFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.controller = Controller()
        self.graph_helper = GraphHelper()
        self.__configure_figure()
        self.__set_widgets()
        for index, widget in enumerate(self.winfo_children(), start=1):
            if widget.widgetName == 'canvas':
                widget.grid(column=2, row=len(self.winfo_children()))
            else:
                widget.grid(column=0, row=index)
        self.pack()

    def __configure_figure(self):
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        self.figure_canvas.get_tk_widget().grid(column=2, row=1)
        self.axes = self.figure.add_axes([0.15, 0.15, 0.7, 0.7])
        self.graph_helper.update_graph('', self.figure)

    def execute_calculate_button(self, equation_text):
        try:
            self.graph_helper.update_graph(equation_text, self.figure)
            self.figure_canvas.get_tk_widget().grid(column=2, row=1)
            equations_result = self.controller.calculate_equations(equation_text)
            for numeric_method in NumericMethods:
                numeric_method_name = numeric_method.value
                result_entry = getattr(self, f'{numeric_method_name}_result')
                iterations_entry = getattr(self, f'{numeric_method_name}_iterations')
                roots = equations_result[numeric_method_name]['roots']
                iterations = equations_result[numeric_method_name]['iterations']
                result_entry.set(str(roots or ''))
                iterations_entry.set(str(iterations))
        except ValueError as e:
            if getattr(e, 'args'):
                message = e.args[0]
            else:
                message = 'Unknown error'
            messagebox.showerror('Something went wrong', message)

    def __set_widgets(self):
        self.bisection_result = tk.StringVar()
        self.bisection_iterations = tk.StringVar()
        bisection_label = tk.Label(self, text="Bisection")
        bisection_result_label = tk.Label(self, text="Result")
        bisection_result_entry = tk.Entry(self, state=DISABLED, textvariable=self.bisection_result)
        bisection_iteration_label = tk.Label(self, text="Iterations")
        bisection_iterations_entry = tk.Entry(self, state=DISABLED, textvariable=self.bisection_iterations)

        self.false_position_result = tk.StringVar()
        self.false_position_iterations = tk.StringVar()
        false_position_label = tk.Label(self, text="False Position")
        false_position_result_label = tk.Label(self, text="Result")
        false_position_result_entry = tk.Entry(self, state=DISABLED, textvariable=self.false_position_result)
        false_position_iteration_label = tk.Label(self, text="Iterations")
        false_position_iterations_entry = tk.Entry(self, state=DISABLED, textvariable=self.false_position_iterations)

        self.secant_result = tk.StringVar()
        self.secant_iterations = tk.StringVar()
        secant_label = tk.Label(self, text="Secant")
        secant_result_label = tk.Label(self, text="Result")
        secant_result_entry = tk.Entry(self, state=DISABLED, textvariable=self.secant_result)
        secant_iteration_label = tk.Label(self, text="Iterations")
        secant_iterations_entry = tk.Entry(self, state=DISABLED, textvariable=self.secant_iterations)

        equation_label = tk.Label(self, text="Enter the equation")
        equation_text_box = tk.Entry(self)

        self.button = tk.Button(self, text='Calculate')
        self.button['command'] = lambda: self.execute_calculate_button(equation_text_box.get())


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Numeric Methods')
        self.geometry('700x900')
