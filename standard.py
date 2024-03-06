from tkinter import messagebox


class StandardCalculator:
    def __init__(self, window, frame, equation_label, first_number_label, operator_label):
        self.second_number = None
        self.first_number = None
        self.operator = None
        self.window = window
        self.frame = frame
        self.equation_label = equation_label
        self.first_number_label = first_number_label
        self.operator_label = operator_label
        self.button_width = 10
        self.number_buttons_functions = {}
        self.operation_functions = {
            '%': lambda: self.percentage_button(equation_label, first_number_label, operator_label),
            'CE': lambda: self.clear_entry(equation_label),
            'C': lambda: self.clear(equation_label, first_number_label, operator_label),
            '1/x': lambda: self.reverse(equation_label),
            'x²': lambda: self.square(equation_label),
            '√': lambda: self.square_root(equation_label),
            '/': lambda: self.divide_button(equation_label, first_number_label, operator_label),
            '+': lambda: self.add_button(equation_label, first_number_label, operator_label),
            '-': lambda: self.subtract_button(equation_label, first_number_label, operator_label),
            '*': lambda: self.multiply_button(equation_label, first_number_label, operator_label),
            'X': lambda: self.delete_button(equation_label),
            '+/-': lambda: self.negate(equation_label),
            ',': lambda: self.comma(equation_label),
            '=': lambda: self.calculate(equation_label, first_number_label, operator_label)
        }
        self.create_number_buttons(equation_label)
        self.buttons_texts = [
            ['%', 'CE', 'C', 'X'],
            ['1/x', 'x²', '√', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', ',', '=']
        ]
        self.buttons_functions = [
            [self.operation_functions['%'], self.operation_functions['CE'], self.operation_functions['C'],
             self.operation_functions['X']],
            [self.operation_functions['1/x'], self.operation_functions['x²'], self.operation_functions['√'],
             self.operation_functions['/']],
            [self.number_buttons_functions['7'], self.number_buttons_functions['8'], self.number_buttons_functions['9'],
             self.operation_functions['*']],
            [self.number_buttons_functions['4'], self.number_buttons_functions['5'], self.number_buttons_functions['6'],
             self.operation_functions['-']],
            [self.number_buttons_functions['1'], self.number_buttons_functions['2'], self.number_buttons_functions['3'],
             self.operation_functions['+']],
            [self.operation_functions['+/-'], self.number_buttons_functions['0'], self.operation_functions[','],
             self.operation_functions['=']]
        ]

    def create_add_number_to_label(self, value, equation_label):
        def inner():
            current_label_value = equation_label.cget('text')
            if current_label_value == '0':
                new_text = value
            else:
                new_text = current_label_value + value
            equation_label.config(text=new_text)
        return inner

    def create_number_buttons(self, equation_label):
        for i in range(10):
            button_text = str(i)
            button_function = self.create_add_number_to_label(button_text, equation_label)
            self.number_buttons_functions[button_text] = button_function

    def delete_button(self, equation_label):
        current_label_value = equation_label.cget('text')
        if current_label_value:  # Check if the label is not empty
            new_label_value = current_label_value[:-1]
            equation_label.config(text=new_label_value)
            if new_label_value == '':
                equation_label.config(text='0')

    def square(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = current_label_value**2
        equation_label.config(text=new_label_value)

    def square_root(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        new_label_value = current_label_value**0.5
        equation_label.config(text=new_label_value)

    def reverse(self, equation_label):
        current_label_value = float(equation_label.cget('text'))
        if current_label_value != 0:
            new_label_value = 1/current_label_value
            equation_label.config(text=new_label_value)
        else:
            messagebox.showerror('Error', 'Zero cannot be reversed')

    def organising_labels(self, equation_label, first_number_label, operator_label):
        equation_label.config(text='0')
        first_number_label.config(text=self.first_number)
        operator_label.config(text=self.operator)

    def divide_button(self, equation_label, first_number_label, operator_label):
        self.operator = '/'
        self.first_number = int(equation_label.cget('text'))
        self.organising_labels(equation_label, first_number_label, operator_label)

    def add_button(self, equation_label, first_number_label, operator_label):
        self.operator = '+'
        self.first_number = int(equation_label.cget('text'))
        self.organising_labels(equation_label, first_number_label, operator_label)

    def subtract_button(self, equation_label, first_number_label, operator_label):
        self.operator = '-'
        self.first_number = int(equation_label.cget('text'))
        self.organising_labels(equation_label, first_number_label, operator_label)

    def multiply_button(self, equation_label, first_number_label, operator_label):
        self.operator = '*'
        self.first_number = int(equation_label.cget('text'))
        self.organising_labels(equation_label, first_number_label, operator_label)

    def percentage_button(self, equation_label, first_number_label, operator_label):
        self.operator = '%'
        self.first_number = int(equation_label.cget('text'))
        self.organising_labels(equation_label, first_number_label, operator_label)

    def negate(self, equation_label):
        current_label_value = int(equation_label.cget('text'))
        new_label_value = -current_label_value
        equation_label.config(text=str(new_label_value))

    def comma(self, equation_label):
        current_label_value = equation_label.cget('text')
        new_label_value = current_label_value + '.'
        equation_label.config(text=str(new_label_value))

    def clear_entry(self, equation_label):
        equation_label.config(text='0')

    def clear(self, equation_label, first_number_label, operator_label):
        equation_label.config(text='0')
        first_number_label.config(text='')
        operator_label.config(text='')

    def calculate(self, equation_label, first_number_label, operator_label):
        self.second_number = float(equation_label.cget('text'))
        if self.operator:
            if self.operator == '/':
                if self.second_number != 0:
                    result = self.first_number / self.second_number
                    equation_label.config(text=str(result))
                else:
                    messagebox.showerror('Error', 'Cannot divide by zero')
            elif self.operator == '+':
                result = self.first_number + self.second_number
                equation_label.config(text=str(result))
            elif self.operator == '-':
                result = self.first_number - self.second_number
                equation_label.config(text=str(result))
            elif self.operator == '*':
                result = self.first_number * self.second_number
                equation_label.config(text=str(result))
            elif self.operator == '%':
                result = round((self.second_number / self.first_number) * 100, 2)
                equation_label.config(text=str(result) + '%')
        self.operator = None
        self.first_number = None
        self.second_number = None
        first_number_label.config(text='')
        operator_label.config(text='')
