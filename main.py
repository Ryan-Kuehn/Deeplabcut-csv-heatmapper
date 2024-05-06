import matplotlib.pyplot as plt
from matplotlib import collections
import functions as funct

file_path = funct.file_get()
# x-axis setup functions see functions.py
x_low = funct.graph_minsize_x(file_path)
x_high = funct.graph_maxsize_x(file_path)
print(f"x lowest value = {x_low} , x highest value = {x_high}")

# y-axis setup functions see functions.py
y_low = funct.graph_minsize_y(file_path)
y_high = funct.graph_maxsize_y(file_path)
print(f"y lowest value = {y_low} , y highest value = {y_high}")

plt.style.use('_mpl-gallery-nogrid')
# data import from csv
x = funct.x_values(file_path)
y = funct.y_values(file_path)

# plot:
fig, ax = plt.subplots()
# args for .hexbin can be found at
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin
graph = ax.hexbin(x, y, C=None, bins='log', gridsize=50, cmap='jet', edgecolors='grey', marginals=False)
ax.set(xlim=(x_low, x_high), ylim=(y_high, y_low))

array = collections.PolyCollection.get_array(graph)
print(collections.PolyCollection.get_sizes(graph))
print(array)

plt.show()