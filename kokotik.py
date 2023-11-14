import tkinter as tk

def create_grid(root, array):
    rows = len(array)
    cols = len(array[0])
    
    for i in range(rows):
        for j in range(cols):
            x = j * 20
            y = i * 20
            
            if array[i][j] == ' ':
                color = 'white'
            else:
                color = 'black'
            
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=color)

# Example two-dimensional array
my_array = [
    ['#', ' ', '#', ' '],
    [' ', '#', ' ', '#'],
    ['#', ' ', '#', ' '],
    [' ', '#', ' ', '#']
]






