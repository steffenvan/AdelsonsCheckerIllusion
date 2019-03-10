import os
from bokeh.plotting import figure

staticRsrcFolder = ""

def init(_staticRsrcFolder):
    """This function will be called before the start of the experiment
    and can be used to initialize variables and generate static resources
    
    :param _staticRsrcFolder: path to a folder where static resources can be stored
    """
    global staticRsrcFolder
    staticRsrcFolder = _staticRsrcFolder

def getName():
    "Returns the name of the illusion"

    return "Adelson's Checker-Shadow Illusion"

def getInstructions():
    "Returns the instructions as a HTML string"
    
    instruction = """
        <p>Still implementing.</p>
    """
    return instruction

def getQuestion():
    "Returns a string with a Yes/No question that checks if the participant sees the illusion inverted"

    return "Does the illusion look inverted?"

def getNumVariations():
    "Returns the number of variations"

    return 3

def draw(variationID, distortion, n=5):
    """This function generates the optical illusion figure.
    The function should return a bokeh figure of size 500x500 pixels.

    :param variationID: select which variation to draw (range: 0 to getNumVariations()-1)
    :param distortion: the selected distortion (range: 0.0 to 1.0)
    :return handle to bokeh figure that contains the optical illusion
    """

    ## Create figure and disable axes and tools
    # p = figure(plot_width=500, plot_height=500, x_range=(0, 1), y_range=(0, 1))
    #p.outline_line_color = None
    p = figure(plot_width=500, plot_height=500, x_range=(0, 10), y_range=(-2, 10))
    p.toolbar.active_drag = None
    p.toolbar.logo = None
    p.toolbar_location = None
    p.xaxis.visible = None
    p.yaxis.visible = None
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    x_coords = [[1, 2, 2, 1], 
                [2, 3, 3, 2],
                [3, 4, 4, 3], 
                [4, 5,5, 4], 
                [5, 6, 6, 5]]

    x2_coords = [[6, 6.5, 6.5, 6],
                 [6.5, 7., 7, 6.5],
                 [7., 7.5, 7.5, 7],
                 [7.5, 8, 8, 7.5],
                 [8, 8.5, 8.5, 8]]

    x_coords.extend(x2_coords)

    y_coords = [[2.0, 1.6, 2.4, 2.8], 
                [1.6, 1.2, 2.0, 2.4],
                [1.2, 0.8, 1.6, 2.0], 
                [0.8, 0.4, 1.2, 1.6], 
                [0.4, 0.0, 0.8, 1.2]]
    
    y2_coords = [[0.0, 1.0, 1.9, 0.8],
                [1.0, 2.0, 2.9, 1.9],
                [2.0, 3.0, 3.9, 2.9],
                [3.0, 4.0, 4.9, 3.9],
                [4.0, 5.0, 5.9, 4.9]]

    y_coords.extend(y2_coords)
    alphas = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    p.patches(x_coords, y_coords,
          color=["darkgray", "gray", "darkgray", "gray", "darkgray", "darkgray", "gray", "darkgray", "gray", "darkgray"], alpha=alphas, line_width=2)
    return p