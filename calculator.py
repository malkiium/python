import tkinter as tk

root = tk.Tk()
root.geometry("400x500")

# Initialize the expression text
expression = ""

def text_stuff():
    global text_result
    text_result = tk.Text(root, height=2, width=21, font=("Arial", 24))
    text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")  # Span across all 4 columns

def on_button_click(button_text, button_widget):
    global expression

    # Temporarily change the button color
    button_widget.config(bg="darkgray")

    # Update the expression and display it
    expression += button_text
    text_result.delete(1.0, tk.END)  # Clear the text area
    text_result.insert(tk.END, expression)  # Insert updated expression

    # After a short delay, revert the button color
    root.after(100, lambda: button_widget.config(bg="lightgray"))

def on_equal_click(button_widget):
    global expression

    # Temporarily change the button color
    button_widget.config(bg="darkgray")

    try:
        # Replace 'x' with '*' to handle multiplication in Python
        expression = expression.replace('x', '*').replace('/', '/')

        # Evaluate the expression when '=' is clicked
        result = str(eval(expression))
        expression = result  # Update the expression with the result
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)  # Show the result
    except Exception as e:
        # If there's an error (like invalid input), display error
        expression = "Error"
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, expression)  # Show the error
    finally:
        # Revert the button color after a short delay
        root.after(100, lambda: button_widget.config(bg="lightgray"))

def on_clear_click(button_widget):
    global expression
    # Clear the expression and the text area only if Clear is pressed
    expression = ""
    text_result.delete(1.0, tk.END)  # Clear the text area
    button_widget.config(bg="darkgray")

    # After a short delay, revert the button color
    root.after(100, lambda: button_widget.config(bg="lightgray"))

def boxes():
    buttons = [
        ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
        ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("x", 3, 3),
        ("(", 4, 0), ("0", 4, 1), (")", 4, 2), ("/", 4, 3),
        ("C", 5, 0), ("=", 5, 2)
    ]

    for button_text, row, col in buttons:
        button = tk.Label(root, text=button_text, font=("Arial", 24), width=5, height=2, bg="lightgray")

        # For the "=" button, make the text be "=" and bind to the on_equal_click function
        if button_text == "=":
            button.config(text="=", bg="lightgray")
            button.grid(row=row, column=col, columnspan=2, padx=10, pady=10, sticky="ew")  # Span across 2 columns
            button.bind("<Button-1>", lambda e, btn=button: on_equal_click(btn))
        elif button_text == "C":
            # For the "Clear" button, bind to on_clear_click function
            button.config(text="Clear")
            button.grid(row=row, column=col, columnspan=2, padx=10, pady=10, sticky="ew")  # Span across 2 columns
            button.bind("<Button-1>", lambda e, btn=button: on_clear_click(btn))
        else:
            # For other buttons, bind to on_button_click
            button.bind("<Button-1>", lambda e, text=button_text, btn=button: on_button_click(text, btn))

        button.grid(row=row, column=col, padx=10, pady=10)

def cells():
    # Configure the grid layout to have 4 columns
    root.grid_rowconfigure(0, weight=0)  # First row doesn't expand
    root.grid_rowconfigure(1, weight=1)  # Second row (for the labels) expands
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)  # For the Clear and Equal buttons row

    root.grid_columnconfigure(0, weight=1)  # First column will expand
    root.grid_columnconfigure(1, weight=1)  # Second column will expand
    root.grid_columnconfigure(2, weight=1)  # Third column will expand
    root.grid_columnconfigure(3, weight=1)  # Fourth column will expand

text_stuff()
boxes()
cells()
root.mainloop()
