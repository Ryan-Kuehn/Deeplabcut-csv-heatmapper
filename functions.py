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
                    low = int(low - 50)
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
                high = int(high + 50)
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
                    low = int(low - 50)
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
                high = int(high + 50)
    return high


# coordinate functions
def x_values(file_input, x):
    values = []
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            values.append(int(float(col[x])))

    return values


def y_values(file_input, y):
    values = []
    with open(file_input, mode='r') as file:
        next(file)
        next(file)
        next(file)
        for col in csv.reader(file, delimiter=','):
            values.append(int(float(col[y])))
    return values
