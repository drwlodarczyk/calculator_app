from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

import scientific
import standard

bg_color = 'lightgrey'
equal_button_color = 'lightblue'


def clear_frame(frame):
    for child in frame.winfo_children():
        child.destroy()


def add_buttons(buttons, button_width, buttons_functions):
    buttons_list = []
    clear_frame(frame_buttons)
    for row_texts, row_functions in zip(buttons, buttons_functions):
        buttons_frame = Frame(frame_buttons)
        buttons_frame.pack(side='top', fill='both', expand=True)
        row_buttons = []
        for text, function in zip(row_texts, row_functions):
            button = Button(buttons_frame, text=text, width=button_width, command=function)
            button.pack(side='left', fill='both', expand=True)
            row_buttons.append(button)
        buttons_list.append(row_buttons)
    buttons_list[-1][-1].config(bg=equal_button_color)


def selection_changed(event):
    selection = combo.get()
    if selection == 'Standardowy':
        equation_label.config(text='0')
        add_buttons(standard_calculator.buttons_texts, standard_calculator.button_width,
                    standard_calculator.buttons_functions)
    else:
        equation_label.config(text='0')
        add_buttons(scientific_calculator.buttons_texts, scientific_calculator.button_width,
                    scientific_calculator.buttons_functions)


window = Tk()
window.title("Calculator")
window.geometry("320x510")
window.config(bg="lightgrey")

style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground=bg_color, background=bg_color)

TopFrame = Frame(window, bg='lightgrey')
TopFrame.pack(side='top', fill='x')

combo = Combobox(TopFrame,
                 state='readonly',
                 values=('Standardowy', 'Naukowy'))
combo.pack(side='left', pady=10)

combo.current(0)
combo.bind('<<ComboboxSelected>>', selection_changed)

operator_label = Label(TopFrame, text='', font=5, bg=bg_color, padx=5)
operator_label.pack(side='right')
first_number_label = Label(TopFrame, text='', font=5, bg=bg_color, padx=5)
first_number_label.pack(side='right')


equation_frame = Frame(window, bg=bg_color)
equation_frame.pack(side='top', fill='both')
equation_label = Label(equation_frame, text='0', bg=bg_color, font=("Helvetica", 20, 'bold'), pady=10)
equation_label.pack(side='right')

# creating memory buttons
memory_frame = Frame(window, bg=bg_color)
memory_frame.pack(side='top', fill='both')

button_MC = Button(memory_frame, text='MC')
button_MC.pack(side='left', fill='both', expand=True)
button_MR = Button(memory_frame, text='MR')
button_MR.pack(side='left', fill='both', expand=True)
button_Mplus = Button(memory_frame, text="M+")
button_Mplus.pack(side='left', fill='both', expand=True)
button_Mminus = Button(memory_frame, text='M-')
button_Mminus.pack(side='left', fill='both', expand=True)
button_MS = Button(memory_frame, text='MS')
button_MS.pack(side='left', fill='both', expand=True)

frame_buttons = Frame(window)
frame_buttons.pack(side='top', fill='both', expand=True)

standard_calculator = standard.StandardCalculator(window, frame_buttons, equation_label,
                                                  first_number_label, operator_label)
scientific_calculator = scientific.ScientificCalculator(window, frame_buttons, equation_label,
                                                        first_number_label, operator_label)

# calling function on app opening
selection_changed(None)

window.mainloop()
