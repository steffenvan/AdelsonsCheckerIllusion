import os
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.glyphs import ImageURL
import numpy as np


colors = ["Black", "Blue", "Green", "Red", "Yellow", "Purple"]

staticRsrcFolder = "illusionApp/static"


def init(_staticRsrcFolder):
    """This function will be called before the start of the experiment
    and can be used to initialize variables and generate static resources
    
    :param _staticRsrcFolder: path to a folder where static resources can be stored
    """
    global staticRsrcFolder
    staticRsrcFolder = _staticRsrcFolder
    
    ## Create figure as global variable and disable axes and tools
    global p
    p = figure(plot_width=500, plot_height=500, x_range=(0, 1), y_range=(0, 1))
    #p.outline_line_color = None
    p.toolbar.active_drag = None
    p.toolbar.logo = None
    p.toolbar_location = None
    p.xaxis.visible = None
    p.yaxis.visible = None
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # here in this template we just draw a circle with 'distorted' radius
    # this time we draw the circle with a dynamic data source
    global source
    source = ColumnDataSource(data=dict(radius=[0.5], color=[colors[3]]))
    p.circle(0.5,0.5, radius='radius', fill_color='color', line_color=None, source=source)
    

def getName():
    "Returns the name of the illusion"

    return "Template Illusion"

def getInstructions():
    "Returns the instructions as a HTML string"
    
    instruction = """
        <p>blah <b style=\"color:red\">the red cross</b> in the centre of the image.
        Your task is to change the distort slider until all the polygons appear square. When ... or when
        you can not find a slider position where ... answer the question and press the \"Submit\" button
        below. Complete this task for each of the variations of this illusion listed below and then press \"Save Data\".</p>
    """
    return instruction

def getQuestion():
    "Returns a string with a Yes/No question that checks if the participant sees the illusion inverted"

    return "Does the illusion look inverted?"

def getNumVariations():
    "Returns the number of variations"

    return 3

def draw(variationID, distortion):
    """This function generates the optical illusion figure.
    The function should return a bokeh figure of size 500x500 pixels.

    :param variationID: select which variation to draw (range: 0 to getNumVariations()-1)
    :param distortion: the selected distortion (range: 0.0 to 1.0)
    :return handle to bokeh figure that contains the optical illusion
    """
    # global p
    # global source

    #here we only change the content of the data source and the circle updates automatically

    # display the illusion from image. 
    imgString = staticRsrcFolder + 'standard.png'
    # N = 5
    # source = ColumnDataSource(dict(
    # imgString = [imgString]*N,
    # x1  = np.linspace(  0, 150, N),
    # y1  = np.linspace(  0, 150, N),
    # w1  = np.linspace( 10,  50, N),
    # h1  = np.linspace( 10,  50, N),
    # x2  = np.linspace(-50, 150, N),
    # y2  = np.linspace(  0, 200, N),
    # ))

    # image3 = ImageURL(url=dict(value=url), x=200, y=-100, anchor="bottom_right")

    p = ImageURL(url=imgString, x=100, y=100)
    # p = figure(x_range=(0,1), y_range=(0,1))
    # p.image_url(url=['pngs/standard.png'], x=0, y=1, w=500, h=500)
    # source.data = dict(radius=[distortion/2], color=[colors[variationID]])

    
    return p