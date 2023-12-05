import tkinter as tk
from tkinter import filedialog
from tkinter import *
import bfs
import dfs
import greedy
import a_search

two_dimensional_array = None
start_position = (1, 0)  
end_position = (28,29)

def DFS_clicked():
    process_input(two_dimensional_array)
    path = dfs.dfs(two_dimensional_array, start_position, end_position)
    process_path(path)

def BFS_clicked():
    process_input(two_dimensional_array)
    path = bfs.bfs(two_dimensional_array, start_position, end_position)
    process_path(path)

def Greedy_clicked():
    process_input(two_dimensional_array)
    path = greedy.greedy_search(two_dimensional_array, start_position, end_position)
    process_path(path)

def A_clicked():
    process_input(two_dimensional_array)
    path = a_search.a_star_search(two_dimensional_array, start_position, end_position)
    process_path(path)

def clear():
    process_input(two_dimensional_array)

def open_file():
    global two_dimensional_array 
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            lines = content.split('\n')

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

def process_path(array_of_tuples):
    for tuple_coordinates in array_of_tuples:
        x, y = tuple_coordinates
        canvas.create_rectangle(100 + x*20, 100 + y*20, 100 + x*20 + 20, 100 + y*20 + 20, fill="red",outline="")


root = tk.Tk()
root.title("Labyrinth")
canvas = Canvas(root, width=800, height=800)
canvas.create_rectangle(100, 100, 700, 700, fill="white", outline="")

DFS = tk.Button(root, text="DFS", command=DFS_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
BFS = tk.Button(root, text="BFS", command=BFS_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
Greedy = tk.Button(root, text="Greedy", command=Greedy_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
A_search = tk.Button(root, text="A* search", command=A_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)

button_width = 100
button_padding = 125
DFS.place(x=button_padding, y=750, width=button_width)
BFS.place(x=button_padding * 2 + button_width, y=750, width=button_width)
Greedy.place(x=button_padding * 3 + button_width * 2, y=750, width=button_width)
A_search.place(x=button_padding * 4 + button_width * 2, y=750, width=button_width)

DFS.config(command=lambda: (DFS_clicked(), DFS.config(bg="grey")))
BFS.config(command=lambda: (BFS_clicked(), BFS.config(bg="grey")))
Greedy.config(command=lambda: (Greedy_clicked(), Greedy.config(bg="grey")))
A_search.config(command=lambda: (A_clicked(), A_search.config(bg="grey")))

title = tk.Label(root, text="Labyrinth", font=("Helvetica", 24), fg="black")
title.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

canvas_width = 800
canvas_height = 800

open_button = tk.Button(root, text="Open File", command=open_file, highlightthickness=0, bd=0)
open_button.pack(pady=10)
open_button.place(x=button_padding * 2 + button_width, y=720, width=button_width)

clear_button = tk.Button(root, text="Clear", command=clear, highlightthickness=0, bd=0)
clear_button.pack(pady=10)
clear_button.place(x=button_padding * 2 + button_width + 200, y=720, width=button_width)

root.geometry(f"{canvas_width}x{canvas_height}")
root.configure(bg='lightgrey')

canvas.pack()
root.mainloop()
