import tkinter as tk

def button_clicked():
    label.config(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Simple GUI")
window.geometry("300x200")

# Create a label
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="Click Me", command=button_clicked)
button.pack()

# Run the main loop
window.mainloop()
