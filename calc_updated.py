import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("450x750")
        self.root.resizable(False, False)

        self.expression = ""
        self.result_shown = False
        self.last_result = None

        self.text_input = tk.StringVar()

        self.display = tk.Entry(self.root, textvariable=self.text_input, font=('arial', 28, 'bold'), bd=20, insertwidth=4, width=14, borderwidth=4, justify='right', bg="#f5f5f5")
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=10, pady=20)

        self.create_buttons()

        self.bind_keys()

    def create_buttons(self):
        button_texts = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('Back', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col) in button_texts:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), bg="#e0e0e0", fg="black", command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)

    def on_button_click(self, char):
        if char == 'C':
            self.clear()
        elif char == 'Back':
            self.backspace()
        elif char == '=':
            self.calculate()
        else:
            if self.result_shown and char.isdigit():
                self.expression = ""
                self.result_shown = False

            if self.result_shown and not char.isdigit():
                self.expression = self.last_result
                self.result_shown = False

            self.expression += str(char)
            self.text_input.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.text_input.set(result)
            self.last_result = result
            self.result_shown = True
        except:
            self.text_input.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.text_input.set("")
        self.result_shown = False
        self.last_result = None

    def backspace(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("<Escape>", lambda event: self.clear())
        for key in '1234567890+-*/().':
            self.root.bind(key, lambda event, char=key: self.on_button_click(char))

root = tk.Tk()
app = Calculator(root)
root.mainloop()
