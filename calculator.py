import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("300x400")
        self.result_var = tk.StringVar()

        # Entry widget to display the result
        entry_frame = ttk.Frame(self.master, padding="10")
        entry_frame.grid(row=0, column=0, columnspan=4)
        entry = ttk.Entry(entry_frame, textvariable=self.result_var, font=('Arial', 18), justify="right")
        entry.grid(row=0, column=0, sticky="nsew")

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, column) in buttons:
            ttk.Button(self.master, text=text, command=lambda t=text: self.button_click(t)).grid(row=row, column=column, sticky="nsew")

        # Configure row and column weights so that they expand proportionally
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == "=":
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            new_text = current_text + button_text
            self.result_var.set(new_text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
