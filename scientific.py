from tkinter import messagebox

import standard
import math


class ScientificCalculator(standard.StandardCalculator):
    def __init__(self, window, frame, equation_label, first_number_label, operator_label):
        super().__init__(window, frame, equation_label, first_number_label, operator_label)
        self.button_width = 5
        self.operation_functions.update({'n!': lambda: self.factorial(equation_label),
                                        'π': lambda: self.pi(equation_label),
                                         'e': lambda: self.euler(equation_label),
                                         'x^⅓': lambda: self.third_sqr_root(equation_label),
                                         '|x|': lambda: self.absolute(equation_label),
                                         'exp': lambda: self.exponent(equation_label),
                                         'log₁₀': lambda: self.log_ten(equation_label),
                                         '10^x': lambda: self.ten_to_power(equation_label),
                                         'ln': lambda: self.ln(equation_label),
                                         "mod": lambda: self.modulo(equation_label, first_number_label, operator_label),
                                         'x^y': lambda: self.power_of(equation_label, first_number_label, operator_label),
                                         'sin': lambda: self.sinus(equation_label)})
        self.buttons_texts = [
            ['x^⅓', 'π', 'e', 'C', 'X'],
            ['x²', '1/x', '|x|', 'exp', 'mod'],
            ['√', 'log₁₀', 'n!', 'sin', '/'],
            ['x^y', '7', '8', '9', '*'],
            ['10^x', '4', '5', '6', '-'],
            ['+/-', '1', '2', '3', '+'],
            ['ln', '+/1', '0', ',', '=']
        ]
        self.buttons_functions = [
            [self.operation_functions['x^⅓'], self.operation_functions['π'], self.operation_functions['e'],
             self.operation_functions['C'], self.operation_functions['X']],
            [self.operation_functions['x²'], self.operation_functions['1/x'], self.operation_functions['|x|'],
             self.operation_functions['exp'], self.operation_functions['mod']],
            [self.operation_functions['√'], self.operation_functions['log₁₀'], self.operation_functions['n!'],
             self.operation_functions['sin'], self.operation_functions['/']],
            [self.operation_functions['x^y'], self.number_buttons_functions['7'], self.number_buttons_functions['8'],
             self.number_buttons_functions['9'], self.operation_functions['*']],
            [self.operation_functions['10^x'], self.number_buttons_functions['4'], self.number_buttons_functions['5'],
             self.number_buttons_functions['6'], self.operation_functions['-']],
            [self.operation_functions['+/-'], self.number_buttons_functions['1'], self.number_buttons_functions['2'],
             self.number_buttons_functions['3'], self.operation_functions['+']],
            [self.operation_functions['ln'], '+/1', self.number_buttons_functions['0'], self.operation_functions[','],
             self.operation_functions['=']]
        ]

    def third_sqr_root(self, equation_label):
        current_label_value = equation_label.cget('text')
        new_label_value = str(current_label_value ** 1/3)
        equation_label.config(text=new_label_value)

    def pi(self, equation_label):
        current_label_value = equation_label.cget('text')
        if current_label_value == '0':
            new_label_value = str(math.pi)
        else:
            new_label_value = current_label_value + str(math.pi)
        equation_label.config(text=new_label_value)

    def factorial(self, equation_label):
        current_label_value = equation_label.cget('text')
        try:
            current_label_value = int(current_label_value)
        except:
            messagebox.showerror('Error', 'Number is not int number')
        else:
            new_label_value = str(math.factorial(current_label_value))
            equation_label.config(text=new_label_value)

    def euler(self, equation_label):
        equation_label.config(text=math.e)

    def log(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = str(math.log(current_label_value))
        equation_label.config(text=new_label_value)

    def log_ten(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = str(math.log(current_label_value))
        equation_label.config(text=new_label_value)

    def absolute(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = str(math.fabs(current_label_value))
        equation_label.config(text=new_label_value)

    def exponent(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = str(math.exp(current_label_value))
        equation_label.config(text=new_label_value)

    def ten_to_power(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = str(10 ** current_label_value)
        equation_label.config(text=new_label_value)

    def ln(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = str(math.log(current_label_value))
        equation_label.config(text=new_label_value)

    def sinus(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = str(math.sin(current_label_value))
        equation_label.config(text=new_label_value)

    def modulo(self, equation_label, first_number_label, operator_label):
        self.operator = 'mod'
        self.first_number = int(equation_label.cget('text'))
        self.organising_labels(equation_label, first_number_label, operator_label)

    def power_of(self, equation_label, first_number_label, operator_label):
        self.operator = 'x^y'
        self.first_number = int(equation_label.cget('text'))
        self.organising_labels(equation_label, first_number_label, operator_label)

    def calculate(self, equation_label, first_number_label, operator_label):
        self.second_number = float(equation_label.cget('text'))
        if self.operator:
            if self.operator == 'mod':
                result = self.first_number % self.second_number
                equation_label.config(text=str(result))
            elif self.operator == 'x^y':
                result = self.first_number ** self.second_number
                equation_label.config(text=str(result))

        super().calculate(equation_label, first_number_label, operator_label)
