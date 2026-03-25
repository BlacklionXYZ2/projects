import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Expression string to keep track of the input
        self.expression = ""
        
        # Display screen
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            root, textvariable=self.display_var, font=('Arial', 24), 
            bg="#f4f4f4", bd=10, justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=20, pady=10)

        # Button layout definition
        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('C', 1, 3), ('AC', 1, 4),
            ('log', 2, 0), ('ln', 2, 1), ('(', 2, 2), (')', 2, 3), ('/', 2, 4),
            ('sqrt', 3, 0), ('7', 3, 1), ('8', 3, 2), ('9', 3, 3), ('*', 3, 4),
            ('pi', 4, 0), ('4', 4, 1), ('5', 4, 2), ('6', 4, 3), ('-', 4, 4),
            ('e', 5, 0), ('1', 5, 1), ('2', 5, 2), ('3', 5, 3), ('+', 5, 4),
            ('^', 6, 0), ('0', 6, 1), ('.', 6, 2), ('DEL', 6, 3), ('=', 6, 4)
        ]

        # Create and place buttons
        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        """Creates a button and assigns it to the grid."""
        # Adjust colors based on button type
        if text in ['=', 'C', 'AC', 'DEL']:
            bg_color = "#ff9999" if text != '=' else "#99ff99"
        elif text.isdigit() or text == '.':
            bg_color = "#ffffff"
        else:
            bg_color = "#e6e6e6"

        button = tk.Button(
            self.root, text=text, font=('Arial', 14), bg=bg_color,
            command=lambda t=text: self.on_button_click(t)
        )
        button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10, padx=2, pady=2)
        
        # Configure grid weights to make buttons expand evenly
        self.root.grid_columnconfigure(col, weight=1)
        self.root.grid_rowconfigure(row, weight=1)

    def on_button_click(self, char):
        """Handles the logic when a button is pressed."""
        if char == 'AC':
            # Clear everything
            self.expression = ""
        elif char == 'C' or char == 'DEL':
            # Delete the last character
            self.expression = self.expression[:-1]
        elif char == '=':
            # Evaluate the expression
            try:
                # Replace standard symbols with Python math equivalents
                eval_expr = self.expression
                eval_expr = eval_expr.replace('^', '**')
                eval_expr = eval_expr.replace('sin', 'math.sin')
                eval_expr = eval_expr.replace('cos', 'math.cos')
                eval_expr = eval_expr.replace('tan', 'math.tan')
                eval_expr = eval_expr.replace('log', 'math.log10')
                eval_expr = eval_expr.replace('ln', 'math.log')
                eval_expr = eval_expr.replace('sqrt', 'math.sqrt')
                eval_expr = eval_expr.replace('pi', 'math.pi')
                eval_expr = eval_expr.replace('e', 'math.e')
                
                # Calculate and format the result
                result = str(eval(eval_expr))
                self.expression = result
            except Exception:
                self.expression = "Error"
        else:
            # Append the pressed character to the expression
            # If the screen shows Error, clear it first
            if self.expression == "Error":
                self.expression = ""
            self.expression += str(char)

        # Update the screen
        self.display_var.set(self.expression)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()