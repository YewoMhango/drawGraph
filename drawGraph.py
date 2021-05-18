import matplotlib.pyplot as plt  # for plotting graphs
import numpy as np               # for arrays

# DrawCartesianGraph plots the graph of the function you pass to it.
# lower_limit and upper_limit specify the region over which to draw
# the graph. The function assumes a cartesian coordinate function

def drawCartesianGraph(function, lower_limit = -1, upper_limit = 1):
    if lower_limit >= upper_limit:
        return None

    # generate a range of values corresponding to the specified range
    x = np.arange(lower_limit, upper_limit, (upper_limit - lower_limit)/ 10000)

    # use the given function to evaluate y = f(x)
    y = function(x)

    # plot and show the graph
    plt.plot(x, y)
    plt.show()


# DrawPolarGraph plots the graph of the function you pass to it.
# lower_limit and upper_limit specify the region over which to draw
# the graph. The function assumes a polar coordinate function

def drawPolarGraph(function, lower_limit = -1, upper_limit = 1):
    if lower_limit >= upper_limit:
        return None

    # generate a range of values corresponding to the specified range
    theta = np.arange(lower_limit, upper_limit, (upper_limit - lower_limit)/10000)

    # use the given function to evaluate r = f(theta)
    r = function(theta)

    # convert polar coordinates to cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # plot and show the graph
    plt.plot(x, y)
    plt.show()

squared = lambda x: x**2
drawCartesianGraph(squared, 0, 10)
drawPolarGraph(squared, 0, 10)

polarArchimedeanSpiral = lambda x: x
drawPolarGraph(polarArchimedeanSpiral, 0, 20)
