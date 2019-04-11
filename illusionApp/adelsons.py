import os
import numpy as np

# Weird macOS fix for displaying screen-shots. 
import matplotlib
matplotlib.use('Agg')

from bokeh.plotting import figure, curdoc


# Folder where background images are stored
staticRsrcFolder = ""

def return_files(vID):
    """Combine striped patterns to get our illusion background

    :param angle: the angle of the lines
    :param size: the size of the figure
    :param offsets: the space between the lines for each pattern (manually determined, depend on the image scale)
    :param linewidth: the thickness of the line
    :param linewidth_step: increase the line thickness by this amount for every smaller pattern
    :param dpi: the dpi of the output image
    :param force_replot: if true, will redraw the pattern every time, otherwise load from disc

    :return: list of filenames that contain the patterns"""

    staticFolder = os.path.abspath(staticRsrcFolder)
    variations_list_path = os.path.join(staticFolder, "variation"+str(vID))

    dir_as_list = os.listdir(variations_list_path)
    filenames = []
    for i in range(len(dir_as_list)):
        filename = dir_as_list[i]
        filenames.append(filename)
    return filenames


def init(_staticRsrcFolder):
    """This function will be called before the start of the experiment
    and can be used to initialize variables and generate static resources
    
    :param _staticRsrcFolder: path to a folder where static resources can be stored
    """
    global staticRsrcFolder
    staticRsrcFolder = _staticRsrcFolder

def getName():
    "Returns the name of the illusion"
    return "Adelson's Checker-Shadow illusion"

def getInstructions():
    "Returns the instructions as a HTML string"
    
    instruction = """
        <p>Compare tile A and tile B. Click on the different variations to change the intensity of the colours of some of the tiles. Modify the shadow strength by using the slider".</p>
    """
    return instruction

def getQuestion():
    "Returns a string with a Yes/No question that checks if the participant sees the illusion inverted"

    return "Do the squares appear similar?"

def getNumVariations():
    "Returns the number of variations"
    return 10

def draw(variationID, distortion):
    """This function generates the optical illusion figure.
    The function should return a bokeh figure of size 500x500 pixels.
    :param variationID: select which variation to draw (changes the path to the folder in which the distortions are stored)
    :param distortion: the selected distorion (rounded to be an integer from which we choose the shadow intensity)
    :return handle to bokeh figure that contains the optical illusion
    """
    bokehFig = figure(plot_width=500, plot_height=500, x_range=(0, 1), y_range=(0, 1))

    bokehFig.toolbar.active_drag = None
    bokehFig.toolbar.logo = None
    bokehFig.toolbar_location = None
    bokehFig.xaxis.visible = None
    bokehFig.yaxis.visible = None
    bokehFig.xgrid.grid_line_color = None
    bokehFig.ygrid.grid_line_color = None

    variationsFolder = os.path.join(staticRsrcFolder, "variations")


    # Rounding the distortion value to nearest integer
    shadowDistortion = round(distortion)

    # Absolute path to the different variation. Indexed by variationID 
    # The distortion changes the shadow intensity.
    filename = "variation_" + str(variationID) + "_" + str(shadowDistortion) + ".png"
    file = os.path.join(variationsFolder, filename)
    print("Distortion: ", shadowDistortion)
    print("File: ", file)

    bokehFig.image_url(url=[file], x=0, y=1, w=None, h=None)

    return bokehFig