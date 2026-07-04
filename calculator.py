import tkinter as tk
from tkinter import messagebox

# Function to update expression in the entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    global expression
    try:
        # Securely evaluate the mathematical string expression
        total = str(eval(expression))
        equation.set(total)
        expression = total # Allow continuous calculation on the result
    except Exception as e:
        equation.set("Error")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window setup
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("350x450")
root.configure(bg="#2c3e50")

expression = ""
equation = tk.StringVar()

# Display screen entry grid
display = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, 
                   insertwidth=4, width=14, borderwidth=0, justify="right", fg="#ffffff", bg="#34495e")
display.grid(columnspan=4, ipady=15, padx=10, pady=20)

# Button layout configuration (text, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), fg="#ffffff", bg="#27ae60",
                        command=equalpress, height=2, width=5, bd=0)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), fg="#ffffff", bg="#e74c3c",
                        command=clear, height=2, width=5, bd=0)
    elif text in ['/', '*', '-', '+']:
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), fg="#ffffff", bg="#3498db",
                        command=lambda t=text: press(t), height=2, width=5, bd=0)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14), fg="#ffffff", bg="#7f8c8d",
                        command=lambda t=text: press(t), height=2, width=5, bd=0)
    
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Configure grid row and column weights for responsiveness
for i in range(5):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()

