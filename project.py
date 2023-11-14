import tkinter as tk
from tkinter import filedialog
from tkinter import *

def DFS_clicked():
    # Add functionality for DFS button click here
    pass

def BFS_clicked():
    # Add functionality for BFS button click here
    pass

def Greedy_clicked():
    # Add functionality for Greedy button click here
    pass

def open_file():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            lines = content.split('\n')

            # Create a two-dimensional array
            two_dimensional_array = [list(line) for line in lines]

            process_input(two_dimensional_array)

def process_input(two_dimensional_array):
    rows = len(two_dimensional_array)
    cols = len(two_dimensional_array[0])
    
    for i in range(rows):
        for j in range(cols):
            x = 100 + j * 20
            y = 100 + i * 20
            
            if two_dimensional_array[i][j] == ' ':
                color = 'white'
            else:
                color = 'black'
            
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=color,outline="")


root = tk.Tk()
root.title("Labyrinth")
canvas = Canvas(root, width=800, height=800)
canvas.create_rectangle(100, 100, 700, 700, fill="white", outline="")

# Create buttons
DFS = tk.Button(root, text="DFS", command=DFS_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
BFS = tk.Button(root, text="BFS", command=BFS_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
Greedy = tk.Button(root, text="Greedy", command=Greedy_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)

# Place buttons with equal width and white background
button_width = 100
button_padding = 125
DFS.place(x=button_padding, y=750, width=button_width)
BFS.place(x=button_padding * 2 + button_width, y=750, width=button_width)
Greedy.place(x=button_padding * 3 + button_width * 2, y=750, width=button_width)

# Change background to grey on button click
DFS.config(command=lambda: (DFS_clicked(), DFS.config(bg="grey")))
BFS.config(command=lambda: (BFS_clicked(), BFS.config(bg="grey")))
Greedy.config(command=lambda: (Greedy_clicked(), Greedy.config(bg="grey")))

# Add title
title = tk.Label(root, text="Labyrinth", font=("Helvetica", 24), fg="black")
title.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Set canvas size
canvas_width = 800
canvas_height = 800

# Create a button to open the file
open_button = tk.Button(root, text="Open File", command=open_file, highlightthickness=0, bd=0)
open_button.pack(pady=10)
open_button.place(x=button_padding * 2 + button_width, y=720, width=button_width)

root.geometry(f"{canvas_width}x{canvas_height}")
root.configure(bg='lightgrey')

canvas.pack()
root.mainloop()
