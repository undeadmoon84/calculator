from tkinter import *
from math import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=40, borderwidth=5, relief="ridge",)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def buttonClick(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonClear():
    e.delete(0, END)

def addition():
    firstNumber = e.get()
    global fNum
    global math
    math = "addition"
    fNum = int(firstNumber)
    e.delete(0, END)
    

def sub():
    firstNumber = e.get()
    global fNum
    global math
    math = "subtraction"
    fNum = int(firstNumber)
    e.delete(0, END)

def mul():
    firstNumber = e.get()
    global fNum
    global math
    math = "multiplication"
    fNum = int(firstNumber)
    e.delete(0, END)

def division():
    firstNumber = e.get()
    global fNum
    global math
    math = "division"
    fNum = int(firstNumber)
    e.delete(0, END)

def sqrt():
    firstNumber = e.get()
    global fNum
    global math
    math = "sqrt"
    fNum = int(firstNumber)
    e.delete(0, END)

def power():
    firstNumber = e.get()
    global fNum
    global math
    math = "power"
    fNum = int(firstNumber)
    e.delete(0, END)

def equal():
    secondNumber = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, fNum + int(secondNumber))
    if math == "subtraction":
        e.insert(0, fNum - int(secondNumber))
    if math == "multiplication":
        e.insert(0, fNum * int(secondNumber))
    if math == "division":
        e.insert(0, fNum / int(secondNumber))
    if math == "sqrt":
        e.insert(0, sqrt(fNum))
    if math == "power":
        e.insert(0, fNum ** int(secondNumber))



#define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1), bg="white")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2), bg="white")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3), bg="white")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4), bg="white")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5), bg="white")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6), bg="white")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7), bg="white")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8), bg="white")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9), bg="white")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0), bg="white")

sum_Button = Button(root, text="+", padx=40, pady=20, command= sum)
sub_Button = Button(root, text="-", padx=40, pady=20, command= sub)
mul_Button = Button(root, text="X", padx=40, pady=20, command= mul)
div_Button = Button(root, text="÷", padx=40, pady=20, command= division)
sqrt_Button = Button(root, text="√", padx=40, pady=20, command= sqrt)
power_Button = Button(root, text="^", padx=40, pady=20, command= power)

equalButton = Button(root, text="=", padx=88, pady=20, command= equal, bg="#383838", fg="white")
clearButton = Button(root, text="Clear", padx=30, pady=20, command= buttonClear)


# Put the buttons on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)

div_Button.grid(row=1,column=4)
sum_Button.grid(row=4,column=4)
sub_Button.grid(row=3,column=4)
mul_Button.grid(row=2,column=4)
sqrt_Button.grid(row=1,column=2)
power_Button.grid(row=1,column=1)

equalButton.grid(row=5, column=2,columnspan=10)
clearButton.grid(row=5, column=0)

def buttonKeyPress(event):
    key = event.char
    if key.isdigit():
        buttonClick(int(key))
    elif key == "+":
        addition()
    elif key == "-":
        sub()
    elif key == "*":
        mul()
    elif key == "/":
        division()
    elif key == "^":
        power()
    elif key == "=" or key == "\r":
        equal()
    elif key == "\x08":  # Backspace key
        e.delete(len(e.get()) - 1, END)
    elif key == "\x1B":  # ESC key
        buttonClear()

# Bind numeric keyboard events
for i in range(10):
    root.bind(str(i), buttonKeyPress)

# Bind operator keyboard events
root.bind('+', buttonKeyPress)
root.bind('-', buttonKeyPress)
root.bind('*', buttonKeyPress)
root.bind('/', buttonKeyPress)
root.bind('^', buttonKeyPress)

# Bind Enter key
root.bind('<Return>', buttonKeyPress)

# Bind Backspace key
root.bind('<BackSpace>', buttonKeyPress)
root.bind('<Escape>', buttonKeyPress)

root.mainloop()