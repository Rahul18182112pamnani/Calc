import tkinter as t
import math

root = t.Tk()
root.title("Basic Calculator")
root.geometry("400x600")

memory = 0

display = t.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=5)

def click_event(key):
    global memory 
    if key == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif key == "CE":
        display.delete(0, tk.END)
    elif key == "C":
        display.delete(0, tk.END)
    elif key == "√":
        try:
            result = str(math.sqrt(float(display.get())))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif key == "%":
        try:
            result = str(float(display.get()) / 100)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif key == "M+":
        try:
            memory += float(display.get())
            display.delete(0, tk.END)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif key == "M-":
        try:
            memory -= float(display.get())
            display.delete(0, tk.END)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif key == "MC":
        memory = 0
    elif key == "MR":
        display.delete(0, tk.END)
        display.insert(tk.END, str(memory))
    else:
        display.insert(tk.END, key)

buttons = [
    'MC', 'MR', 'M+', 'M-', 'C',
    '7', '8', '9', '/', '√',
    '4', '5', '6', '*', '%',
    '1', '2', '3', '-', 'CE',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: click_event(x)
    tk.Button(root, text=button, width=7, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

root.mainloop()
