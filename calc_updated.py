import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("450x750")
        self.root.resizable(0, 0)

        self.expression = ""
        self.result = ""
        self.memory = 0
        self.last_operator = ""
        self.last_number = ""
        self.current_input = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', 'C', '4', '5', '6', '/', 
            '1', '2', '3', '*', '0', '.', '=', '+', 
            '-', '(', ')', 'M+', 'M-', 'MR', 'MC', '√', 
            '^2', '^3', '+/-', '←'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            if col > 3:
                col = 0
                row += 1
            self.create_button(button, row, col)
            col += 1

    def create_button(self, text, row, col):
        if text == '=':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="green", font=("Arial", 18),
                            command=self.calculate_result)
        elif text == 'C':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="red", font=("Arial", 18),
                            command=self.clear)
        elif text == '←':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="blue", font=("Arial", 18),
                            command=self.backspace)
        elif text == '+/-':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="purple", font=("Arial", 18),
                            command=self.change_sign)
        elif text == '^2':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="purple", font=("Arial", 18),
                            command=self.square)
        elif text == '^3':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="purple", font=("Arial", 18),
                            command=self.cube)
        elif text == '√':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="purple", font=("Arial", 18),
                            command=self.sqrt)
        elif text == 'M+':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="brown", font=("Arial", 18),
                            command=self.memory_add)
        elif text == 'M-':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="brown", font=("Arial", 18),
                            command=self.memory_subtract)
        elif text == 'MR':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="brown", font=("Arial", 18),
                            command=self.memory_recall)
        elif text == 'MC':
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="white", bg="brown", font=("Arial", 18),
                            command=self.memory_clear)
        else:
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bd=8, font=("Arial", 18), command=lambda: self.on_click(text))
        btn.grid(row=row, column=col)

    def on_click(self, char):
        if char in "+-*/" and self.expression.endswith(('+', '-', '*', '/')):
            self.expression = self.expression[:-1] + char
        else:
            self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def change_sign(self):
        if self.expression and self.expression[-1].isdigit():
            self.expression = str(-float(self.expression))
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate_result(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result 
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.expression = ""
            self.display.delete(0, tk.END)
        except SyntaxError:
            messagebox.showerror("Error", "Invalid input")
            self.expression = ""
            self.display.delete(0, tk.END)

    def memory_add(self):
        try:
            self.memory += float(self.display.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input in memory add")

    def memory_subtract(self):
        try:
            self.memory -= float(self.display.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input in memory subtract")

    def memory_recall(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(self.memory))
        self.expression = str(self.memory)

    def memory_clear(self):
        self.memory = 0

    def square(self):
        try:
            self.expression = str(float(self.expression) ** 2)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for squaring")

    def cube(self):
        try:
            self.expression = str(float(self.expression) ** 3)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for cubing")

    def sqrt(self):
        try:
            self.expression = str(float(self.expression) ** 0.5)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for square root")

# Main loop
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
