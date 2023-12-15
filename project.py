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
    path, time, visited = dfs.dfs(two_dimensional_array, start_position, end_position)
    print("DFS: ", time)
    time = round(time, 6)
    time = str(time)
    update_text(f"The computing time of DFS was: {time}s")
    process_visited(visited)
    process_path(path)

def BFS_clicked():
    process_input(two_dimensional_array)
    path, time = bfs.bfs(two_dimensional_array, start_position, end_position)
    print("BFS: ", time)
    time = round(time, 6)
    time = str(time)
    update_text(f"The computing time of BFS was: {time}s")
    process_path(path)

def Greedy_clicked():
    process_input(two_dimensional_array)
    path, time = greedy.greedy_search(two_dimensional_array, start_position, end_position)
    print("Greedy: ", time)
    time = round(time, 6)
    time = str(time)
    update_text(f"The computing time of Greedy was: {time}s")
    process_path(path)

def A_clicked():
    process_input(two_dimensional_array)
    path, time = a_search.a_star_search(two_dimensional_array, start_position, end_position)
    print("A: ", time)
    time = round(time, 6)
    time = str(time)
    update_text(f"The computing time of A* search was: {time}s")
    process_path(path)

def clear():
    process_input(two_dimensional_array)
    update_text("Click on any of the search buttons")

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
            y = 50 + i * 20
            
            if two_dimensional_array[i][j] == ' ':
                color = 'white'
            else:
                color = 'black'
            
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=color,outline="")

def process_path(array_of_tuples):
    for tuple_coordinates in array_of_tuples:
        x, y = tuple_coordinates
        canvas.create_rectangle(100 + x*20, 50 + y*20, 100 + x*20 + 20, 50 + y*20 + 20, fill="red",outline="")

def process_visited(array_of_tuples):
    for tuple_coordinates in array_of_tuples:
        y, x = tuple_coordinates
        canvas.create_rectangle(100 + x*20, 50 + y*20, 100 + x*20 + 20, 50 + y*20 + 20, fill="blue",outline="")


def update_text(new_text):
    label.config(text=new_text)

def compare_all():
    process_input(two_dimensional_array)
    path, timedfs, visited = dfs.dfs(two_dimensional_array, start_position, end_position)
    best_time = timedfs
    best_search = "DFS"
    print("DFS: ", timedfs)
    timedfs = round(timedfs, 6)
    timedfs = str(timedfs)
    process_input(two_dimensional_array)
    path, timebfs = bfs.bfs(two_dimensional_array, start_position, end_position)
    if timebfs < best_time:
        best_search = "BFS"
        best_time = timebfs
    print("BFS: ", timebfs)
    timebfs = round(timebfs, 6)
    timebfs = str(timebfs)
    process_input(two_dimensional_array)
    path, timegreedy = greedy.greedy_search(two_dimensional_array, start_position, end_position)
    if timegreedy < best_time:
        best_search = "Greedy"
        best_time = timegreedy
    print("Greedy: ", timegreedy)
    timegreedy = round(timegreedy, 6)
    timegreedy = str(timegreedy)
    process_input(two_dimensional_array)
    path, timea = a_search.a_star_search(two_dimensional_array, start_position, end_position)
    if timea < best_time:
        best_search = "A*"
        best_time = timea
    print("A: ", timea)
    timea = round(timea, 6)
    timea = str(timea)
    update_text(f"The computing time of DFS was: {timedfs}s\nThe computing time of BFS was: {timebfs}s\nThe computing time of Greedy was: {timegreedy}s\nThe computing time of A* search was: {timea}s\nThe quickest algorhytm was {best_search}")

root = tk.Tk()
root.title("Labyrinth")
canvas = Canvas(root, width=800, height=800)
canvas.create_rectangle(100, 50, 700, 650, fill="white", outline="")
label = tk.Label(root, text="Click on any of the search buttons")
label.place(x=400, y=670)

DFS = tk.Button(root, text="DFS", command=DFS_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
BFS = tk.Button(root, text="BFS", command=BFS_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
Greedy = tk.Button(root, text="Greedy", command=Greedy_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
A_search = tk.Button(root, text="A* search", command=A_clicked, bg="white", fg="black", width=15, highlightthickness=0, bd=0)
compare_all = tk.Button(root, text="Compare all", command=compare_all, bg="white", fg="black", width=15, highlightthickness=0, bd=0)

button_width = 100
button_height = 20
DFS.place(x=100, y=670, width=button_width, height=button_height)
BFS.place(x=100, y=695, width=button_width, height=button_height)
Greedy.place(x=100, y=720, width=button_width, height=button_height)
A_search.place(x=100, y=745, width=button_width, height=button_height)
compare_all.place(x=250, y=745, width=button_width, height=button_height)

DFS.config(command=lambda: (DFS_clicked(), DFS.config(bg="grey")))
BFS.config(command=lambda: (BFS_clicked(), BFS.config(bg="grey")))
Greedy.config(command=lambda: (Greedy_clicked(), Greedy.config(bg="grey")))
A_search.config(command=lambda: (A_clicked(), A_search.config(bg="grey")))

title = tk.Label(root, text="Labyrinth", font=("Helvetica", 24), fg="black")
title.place(relx=0.5, rely=0.03, anchor=tk.CENTER)

canvas_width = 800
canvas_height = 800

open_button = tk.Button(root, text="Open File", command=open_file, highlightthickness=0, bd=0)
open_button.pack(pady=10)
open_button.place(x=250, y=670, width=button_width, height=button_height)

clear_button = tk.Button(root, text="Clear", command=clear, highlightthickness=0, bd=0)
clear_button.pack(pady=10)
clear_button.place(x=250, y=695, width=button_width,  height=button_height)

root.geometry(f"{canvas_width}x{canvas_height}")
root.configure(bg='lightgrey')

canvas.pack()
root.mainloop()
