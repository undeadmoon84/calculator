from tkinter import *
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.f_num = 0
        self.math_operation = ""
        self.result_displayed = False

        self.e = Entry(master, width=35, borderwidth=5, relief="ridge", font=('Arial', 16), justify='right')
        self.e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        self.create_buttons()
        self.bind_keys()

    def button_click(self, value):
        if self.result_displayed:
            self.e.delete(0, END)
            self.result_displayed = False

        current = self.e.get()

        if value == '.':
            if '.' in current:
                return
            if not current:
                current = '0'

        self.e.delete(0, END)
        self.e.insert(0, current + str(value))

    def button_clear(self):
        self.e.delete(0, END)
        self.f_num = 0
        self.math_operation = ""

    def perform_operation(self, operation):
        current_val = self.e.get()
        if not current_val:
            return

        try:
            self.f_num = float(current_val)
            self.math_operation = operation
            self.e.delete(0, END)
        except ValueError:
            self.display_error()

    def sqrt(self):
        current_val = self.e.get()
        if not current_val:
            return
        try:
            num = float(current_val)
            if num < 0:
                self.display_error("Invalid input")
                return
            result = math.sqrt(num)
            self.e.delete(0, END)
            self.e.insert(0, self.format_result(result))
            self.result_displayed = True
        except ValueError:
            self.display_error()

    def backspace(self):
        if self.result_displayed:
            self.button_clear()
        else:
            self.e.delete(len(self.e.get())-1, END)

    def equal(self):
        second_number_str = self.e.get()
        if not second_number_str or not self.math_operation:
            return

        try:
            second_number = float(second_number_str)

            operations = {
                "addition": lambda a, b: a + b,
                "subtraction": lambda a, b: a - b,
                "multiplication": lambda a, b: a * b,
                "division": lambda a, b: a / b if b != 0 else "error",
                "power": lambda a, b: a ** b
            }

            result = operations[self.math_operation](self.f_num, second_number)

            if result == "error":
                self.display_error("Division by zero")
            else:
                self.e.delete(0, END)
                self.e.insert(0, self.format_result(result))
                self.result_displayed = True

        except (ValueError, KeyError):
            self.display_error()

    def format_result(self, result):
        if result == int(result):
            return str(int(result))
        else:
            return str(round(result, 8))

    def display_error(self, message="Error"):
        self.e.delete(0, END)
        self.e.insert(0, message)
        self.result_displayed = True

    def create_buttons(self):
        buttons = [
            ('C', 1, 0, self.button_clear), ('<-', 1, 1, self.backspace), ('√', 1, 2, self.sqrt), ('/', 1, 3, lambda: self.perform_operation('division')),
            ('7', 2, 0, lambda: self.button_click('7')), ('8', 2, 1, lambda: self.button_click('8')), ('9', 2, 2, lambda: self.button_click('9')), ('*', 2, 3, lambda: self.perform_operation('multiplication')),
            ('4', 3, 0, lambda: self.button_click('4')), ('5', 3, 1, lambda: self.button_click('5')), ('6', 3, 2, lambda: self.button_click('6')), ('-', 3, 3, lambda: self.perform_operation('subtraction')),
            ('1', 4, 0, lambda: self.button_click('1')), ('2', 4, 1, lambda: self.button_click('2')), ('3', 4, 2, lambda: self.button_click('3')), ('+', 4, 3, lambda: self.perform_operation('addition')),
            ('^', 5, 0, lambda: self.perform_operation('power')), ('0', 5, 1, lambda: self.button_click('0')), ('.', 5, 2, lambda: self.button_click('.')), ('=', 5, 3, self.equal)
        ]

        for (text, row, col, cmd) in buttons:
            btn = Button(self.master, text=text, padx=20, pady=20, font=('Arial', 14), command=cmd, relief="groove")
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            if text in "/*-+=":
                btn.configure(bg='#ff9f0a')
            elif text in "C<-√^":
                btn.configure(bg='#f0f0f0')
            else:
                btn.configure(bg='white')

        for i in range(1, 6):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def key_press(self, event):
        key = event.char

        if key.isdigit() or key == '.':
            self.button_click(key)
        elif key in ['+', '-', '*', '/', '^']:
            op_map = {'+': 'addition', '-': 'subtraction', '*': 'multiplication', '/': 'division', '^': 'power'}
            self.perform_operation(op_map[key])
        elif event.keysym == 'Return' or key == '=':
            self.equal()
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Escape' or key.lower() == 'c':
            self.button_clear()

    def bind_keys(self):
        self.master.bind('<Key>', self.key_press)
        self.master.bind('<Return>', lambda event: self.equal())
        self.master.bind('<BackSpace>', lambda event: self.backspace())
        self.master.bind('<Escape>', lambda event: self.button_clear())

if __name__ == '__main__':
    root = Tk()
    app = Calculator(root)
    root.mainloop()
