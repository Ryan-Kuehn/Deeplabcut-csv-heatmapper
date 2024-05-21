import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import *

"""
file_get: GUI prompt for the path of users CSV
what_is_graphed: Reads in the users CSV and pulls what to graph
graph_minsize_x: Determines the minimum X value for our graph
graph_maxsize_x: Determines the maximum X value for our graph
graph_minsize_y: Determines the minimum Y value for our graph
graph_maxsize_y: Determines the maximum Y value for our graph
x_values: Compiles our x values into a list
y_values: Compiles our Y values into a list

"""


def file_get():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    return file_path


def what_is_graphed(file_input):
    with open(file_input, mode='r') as file:

        # Initial loop to isolate the variables row
        loop = 0
        for col in csv.reader(file, delimiter=','):
            if loop == 1:
                line = col
            elif loop == 2:
                break
            loop = loop + 1

        # Loop to parse the variables row into options for the GUI
        options = []
        val_loop = 0
        for val in line:
            parser = val_loop % 3
            if parser == 0:
                valid = True
            else:
                valid = False

            if val_loop != 0 and valid:
                options.append(val)
            val_loop = val_loop + 1

            # Nested function to check when an item in the GUI is selected

            def check_list():
                try:
                    selected = lb.selection_get()
                    print('selected:', selected)
                    top.destroy()
                    return selected
                except:
                    print('no selection')

        # Loop to display the variables row in the GUI
        print(options)
        top = Tk()
        lb = Listbox(top)

        lb_loop = 1
        for val in options:
            lb.insert(lb_loop, val)
            lb_loop = lb_loop + 1
        lb.pack()

        # Button to finish and return selection
        but = Button(top, text="Finish", command=check_list)
        but.pack()
        top.mainloop()
        selected = check_list()
        print(selected)


# x-value functions
def graph_minsize_x(file_input):
    low = 99999999
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            if float(col[1]) < low:
                low = float(col[1])
                if low - 50 > 0:
                    low = int(low - 50)
                else:
                    low = 0
    return low


def graph_maxsize_x(file_input):
    high = 0
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            if float(col[1]) > high:
                high = float(col[1])
                high = int(high + 50)
    return high


# y-value functions
def graph_minsize_y(file_input):
    low = 99999999
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            if float(col[2]) < low:
                low = float(col[2])
                if low - 50 > 0:
                    low = int(low - 50)
                else:
                    low = 0
    return low


def graph_maxsize_y(file_input):
    high = 0
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            if float(col[2]) > high:
                high = float(col[2])
                high = int(high + 50)
    return high


# coordinate functions
def x_values(file_input):
    values = []
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            values.append(int(float(col[1])))

    return values


def y_values(file_input):
    values = []
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            values.append(int(float(col[2])))
    return values
