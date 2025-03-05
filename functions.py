import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import pandas as pd

"""
                                                   DEVELOPMENT NOTES                                                   
Finish flip_check function
    needs x flip logic
    needs y flip logic

GUI for whole process?

Upload to SUN lab github
"""


"""
                                                Function Table of Contents
flip_check: Prompts user if they want to mirror points over x or y axis. useful for reorienting graphs
file_get: GUI prompt for the path of users CSV
what_is_graphed: Reads in the users CSV and pulls what to graph, user then selects from options
frames_to_sec: Converts FPS into seconds
x_locator: finds column of x values within CSV
graph_minsize_x: Determines the minimum X value for our graph, used for auto scaling graph size, buffer of 100 pixels
graph_maxsize_x: Determines the maximum X value for our graph, used for auto scaling graph size, buffer of 100 pixels
y_locator: finds column of y values within CSV
graph_minsize_y: Determines the minimum Y value for our graph, used for auto scaling graph size, buffer of 100 pixels
graph_maxsize_y: Determines the maximum Y value for our graph, used for auto scaling graph size, buffer of 100 pixels
x_values: Compiles our x values into a list
y_values: Compiles our Y values into a list
"""


def flip_check():
    prompt = input("Would you like to mirror over x-axis or y-axis? enter 'x', 'y', or hit 'enter' to skip: ")

    if prompt == 'x':
        return 'x'
    if prompt == 'y':
        return 'y'
    else:
        return False


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
        options = {}
        val_loop = 0
        for val in line:
            parser = val_loop % 3
            if parser == 0:
                valid = True
            else:
                valid = False

            if val_loop != 0 and valid:
                options[val] = str(int(val_loop / 3))
            val_loop = val_loop + 1
        print(options)

        master = Tk()
        master.geometry("175x175")

        # Tkinter string variable
        v = StringVar(master, '1')

        # Tracing variable change state
        def callback(var):
            print(f"Value changed to {var.get()}")
        v.trace("w", lambda name, index, mode, var=v: callback(v))

        # Loop is used to create multiple Radio buttons
        for (text, value) in options.items():
            Radiobutton(master, text=text, variable=v,
                        value=value).pack(side=TOP, ipady=5)

        # Infinite loop can be terminated by
        # keyboard or mouse interrupt
        # or by any predefined function (destroy())
        btn1 = Button(master, text="Finish", command=master.quit)
        btn1.pack(pady=10)
        master.mainloop()
        master.destroy()
        return v.get()


def frames_to_sec():
    convert = input("Convert Output from frame count ot seconds? y/n: ")
    frame_conv = 0
    if convert == "y":
        frame_conv = int(input("Input Frame count: "))
        return frame_conv
    else:
        return frame_conv


# x-value functions
def x_locator(var_to_graph):
    var_to_graph = 3 * int(var_to_graph)
    var_to_graph = var_to_graph - 1
    return var_to_graph


def graph_minsize_x(file_input, x):
    low = 99999999
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            if float(col[x]) < low:
                low = float(col[x])
                if low - 50 > 0:
                    low = int(low - 100)
                else:
                    low = 0
    print(low)
    return low


def graph_maxsize_x(file_input, x):
    high = 0
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            if float(col[x]) > high:
                high = float(col[x])
                high = int(high + 100)
    return high


# y-value functions
def y_locator(var_to_graph):
    var_to_graph = 3 * int(var_to_graph)
    var_to_graph = var_to_graph - 2
    return var_to_graph


def graph_minsize_y(file_input, y):
    low = 99999999
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            if float(col[y]) < low:
                low = float(col[y])
                if low - 50 > 0:
                    low = int(low - 100)
                else:
                    low = 0
    return low


def graph_maxsize_y(file_input, y):
    high = 0
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            if float(col[y]) > high:
                high = float(col[y])
                high = int(high + 100)
    return high


# coordinate functions
def x_values(file_input, x, frame_conv):
    values = []
    with open(file_input, mode='r') as file:
        # Skip the first three header rows
        next(file)
        next(file)
        next(file)

        reader = csv.reader(file, delimiter=',')
        for i, col in enumerate(reader):
            # Check if the column index is within bounds for the current row
            if len(col) > x:
                # Take the value if row index satisfies the skipping logic
                if i % (frame_conv + 1) == 0:
                    try:
                        values.append(int(float(col[x])))
                    except ValueError:
                        print(f"Warning: Non-numeric value at row {i + 1}, column {x}. Skipping...")
            else:
                print(f"Warning: Row {i + 1} does not have column {x}. Skipping...")

    return values


def y_values(file_input, y, frame_conv):
    values = []
    with open(file_input, mode='r') as file:
        # Skip the first three header rows
        next(file)
        next(file)
        next(file)

        reader = csv.reader(file, delimiter=',')
        for i, col in enumerate(reader):
            # Check if the column index is within bounds for the current row
            if len(col) > y:
                # Take the value if row index satisfies the skipping logic
                if i % (frame_conv + 1) == 0:
                    try:
                        values.append(int(float(col[y])))
                    except ValueError:
                        print(f"Warning: Non-numeric value at row {i + 1}, column {y}. Skipping...")
            else:
                print(f"Warning: Row {i + 1} does not have column {y}. Skipping...")

    return values
