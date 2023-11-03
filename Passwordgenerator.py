import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1 character.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
label = tk.Label(root, text="Password Length:")
label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()