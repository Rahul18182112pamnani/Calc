import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")
        master.geometry("450x750")
        
        self.expression = ""
        self.result = 0
        self.current_input = ""
        self.last_operation = ""
        self.memory = 0
        self.memory_history = []
        self.last_expression = ""
        self.operator = ""
        master.bind("<Key>", self.on_keypress)
        # Display Frame
        self.display_frame = tk.Frame(self.master)
        self.display_frame.pack(expand=True, fill="both")

        # Expression Label
        self.expression_var = tk.StringVar()
        self.expression_label = tk.Label(self.display_frame, textvariable=self.expression_var, font=("Arial", 18), anchor="e", bg="white", fg="grey")
        self.expression_label.pack(expand=True, fill="both", padx=10, pady=10)

        # Result Label
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_label = tk.Label(self.display_frame, textvariable=self.result_var, font=("Arial", 24), anchor="e", bg="white", fg="black")
        self.result_label.pack(expand=True, fill="both", padx=10, pady=10)


        # Button Layout
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(expand=True, fill="both")

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            ['MC', 'MR', 'M+', 'M-', 'C'],
            ['(', ')', '1/x', 'x³', '←'],
            ['7', '8', '9', '/', 'x²'],
            ['4', '5', '6', '*', '±'],
            ['1', '2', '3', '-', '√'],
            ['0', '.', '=', '+', 'CE']
        ]

        for row in button_texts:
            button_row = tk.Frame(self.buttons_frame)
            button_row.pack(expand=True, fill="both")
            for button_text in row:
                button = tk.Button(button_row, text=button_text, font=("Arial", 18), command=lambda x=button_text: self.on_button_click(x))
                button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def on_button_click(self, button_text):
        
        # Check if last operation was '=' and a digit or '.' is pressed
        if self.last_operation and (button_text.isdigit() or button_text == "."):
            # Reset for new calculation
            self.current_input = button_text  # Start fresh with new input
            self.result = 0
            self.expression = ""
            self.result_var.set(self.current_input)
            self.expression_var.set("")
            self.last_operation = False  # Reset the equals flag
            return
        # else:
        #     # Normal input processing
        #     if button_text.isdigit() or button_text == ".":
        #         self.current_input += button_text
        #         self.result_var.set(self.current_input)

        if self.current_input.startswith("."):
            self.current_input = "0" + self.current_input
        if button_text.isdigit() or button_text == ".":
            if button_text == '.' and '.' in self.current_input:
                return  # Prevent multiple decimals in a single number
            if self.last_operation:
                self.current_input = button_text
                self.last_operation = False
            else:
                self.current_input += button_text
            self.result_var.set(self.current_input)
        elif button_text in ['+', '-', '*', '/', 'x²', 'x³', '√', '1/x']:
            if self.current_input != "":
                self.expression += self.current_input
            if button_text == 'x²':
                self.expression += '**2'
            elif button_text == 'x³':
                self.expression += '**3'
            elif button_text == '√':
                self.expression += '**0.5'
            elif button_text == '1/x':
                self.expression += '**-1'
            else:
                self.expression += button_text
            self.operator = button_text  # Track operator
            self.last_expression = self.expression
            self.expression_var.set(self.expression)
            self.current_input = ""
        elif button_text == "=":
            try:
                if self.current_input != "":
                    self.expression += self.current_input
                if self.last_operation:
                    self.expression = str(self.result) + self.operator + str(self.current_input or self.result)
                self.result = eval(self.expression)
                self.result = round(self.result, 2)
                # self.result_var.set(round(result, 10))
                self.result_var.set(str(self.result))
                self.last_operation = True  # Indicates that an equals operation was made
                self.expression_var.set(self.expression)
                self.current_input = str(self.current_input)
                self.expression = ""
            except Exception as e:
                self.result_var.set("Error")
                self.expression = ""
                self.current_input = ""
        elif button_text == "C":
            self.expression = ""
            self.current_input = ""
            self.result = 0
            self.memory = 0
            self.result_var.set("0")
            self.expression_var.set("")
        elif button_text == "CE":
            self.current_input = ""
            self.result = 0
            self.result_var.set("0")
        elif button_text == "←":
            self.current_input = self.current_input[:-1]
            self.result_var.set(self.current_input)
        elif button_text == "±":
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.result_var.set(self.current_input)
        elif button_text == "MC":
            self.memory = 0
            self.memory_history.clear()
        elif button_text == "MR":
            self.result_var.set(str(self.memory))
            self.current_input = str(self.memory)
        elif button_text == "M+":
            self.memory += float(self.result_var.get())
            self.memory_history.append(self.result_var.get())
        elif button_text == "M-":
            self.memory -= float(self.result_var.get())
            self.memory_history.append('-' + self.result_var.get())
    
    def on_keypress(self, event):
        if event.char.isdigit() or event.char in ['+', '-', '*', '/', '.', '=']:
            self.on_button_click(event.char)
        elif event.keysym == 'Return':
            self.on_button_click('=')
        elif event.keysym == 'BackSpace':
            current_text = self.result_var.get()
            self.result_var.set(current_text[:-1])

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
