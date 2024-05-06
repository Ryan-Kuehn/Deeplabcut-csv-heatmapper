import csv
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
import pandas as pd


def file_get():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    return file_path


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
                high = int(high+50)
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
                high = int(high+50)
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
