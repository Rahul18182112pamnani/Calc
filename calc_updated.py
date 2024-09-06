import tkinter as tk

# Global memory variable
memory = 0

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def add_memory():
    global memory
    try:
        memory += float(display.get())
    except ValueError:
        pass

def recall_memory():
    display.insert(tk.END, str(memory))

def clear_memory():
    global memory
    memory = 0

def square():
    try:
        result = str(float(display.get()) ** 2)
        display.delete(0, tk.END)
        display.insert(0, result)
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def cube():
    try:
        result = str(float(display.get()) ** 3)
        display.delete(0, tk.END)
        display.insert(0, result)
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def change_sign():
    try:
        current = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(-current))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Main calculator window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#20232A")
window.geometry("550x650")

# Display entry box
display = tk.Entry(window, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button styling
button_font = ("Arial", 14)
button_bg = "#61DAFB"
button_fg = "#20232A"

# Calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, width=10, height=3, font=button_font, bg=button_bg, fg=button_fg,
                       command=lambda t=text: button_click(t) if t != '=' else calculate())
    button.grid(row=row, column=col, padx=5, pady=5)

# Additional functions buttons
tk.Button(window, text="C", width=10, height=3, font=button_font, bg="#61DAFB", fg="#20232A", command=clear_display).grid(row=5, column=0, padx=5, pady=5)
tk.Button(window, text="M+", width=10, height=3, font=button_font, bg="#61DAFB", fg="#20232A", command=add_memory).grid(row=5, column=1, padx=5, pady=5)
tk.Button(window, text="MR", width=10, height=3, font=button_font, bg="#61DAFB", fg="#20232A", command=recall_memory).grid(row=5, column=2, padx=5, pady=5)
tk.Button(window, text="MC", width=10, height=3, font=button_font, bg="#61DAFB", fg="#20232A", command=clear_memory).grid(row=5, column=3, padx=5, pady=5)
tk.Button(window, text="x²", width=10, height=3, font=button_font, bg="#61DAFB", fg="#20232A", command=square).grid(row=6, column=0, padx=5, pady=5)
tk.Button(window, text="x³", width=10, height=3, font=button_font, bg="#61DAFB", fg="#20232A", command=cube).grid(row=6, column=1, padx=5, pady=5)
tk.Button(window, text="+/-", width=10, height=3, font=button_font, bg="#61DAFB", fg="#20232A", command=change_sign).grid(row=6, column=2, padx=5, pady=5)
tk.Button(window, text="←", width=10, height=3, font=button_font, bg="#61DAFB", fg="#20232A", command=backspace).grid(row=6, column=3, padx=5, pady=5)

# Run the main loop
window.mainloop()
