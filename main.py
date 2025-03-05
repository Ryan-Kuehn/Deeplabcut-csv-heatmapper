import matplotlib.pyplot as plt
from matplotlib import collections
import functions as funct

print("\033[31mWARNING, This code uses several input prompts, meaning YOU will have to type using the keyboard in order"
      " to answer the prompts, ensure to read all prompts carefully.\n if the code seems like it's frozen, it probably"
      " requires an input, or the graph is displayed, which will require you to close the graph in order to re-run"
      " the code.\n If you want to create multiple graphs, run the code multiple times.\n Please ensure that your "
      "graph is rotated properly I can not do this for you.\033[0m")


file_path = funct.file_get()
var = funct.what_is_graphed(file_path)

# x-axis setup functions see functions.py
x = funct.x_locator(var)
x_low = funct.graph_minsize_x(file_path, x)
x_high = funct.graph_maxsize_x(file_path, x)
print(f"x lowest value = {x_low} , x highest value = {x_high}")

# y-axis setup functions see functions.py
y = funct.y_locator(var)
y_low = funct.graph_minsize_y(file_path, y)
y_high = funct.graph_maxsize_y(file_path, y)
print(f"y lowest value = {y_low} , y highest value = {y_high}")

plt.style.use('_mpl-gallery-nogrid')
frame_conv = funct.frames_to_sec()
# data import from csv
x = funct.x_values(file_path, x, frame_conv)
y = funct.y_values(file_path, y, frame_conv)

# plot:
fig, ax = plt.subplots()

# args for .hexbin can be found at
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin
graph = ax.hexbin(x, y, C=None, bins='log', gridsize=23, cmap='jet', edgecolors='grey', marginals=False)
ax.set(xlim=(x_low, x_high), ylim=(y_high, y_low))

# sets colorbar settings
cb = fig.colorbar(graph, ax=ax, label='counts')

# displays an array of values for the hexagons
array = collections.PolyCollection.get_array(graph)
print(array)

plt.show()
