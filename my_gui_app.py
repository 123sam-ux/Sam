import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

root = tk.Tk()
root.title("Simple GUI App")

label = tk.Label(root, text="Welcome!", font=("Arial", 18))
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

root.mainloop()
