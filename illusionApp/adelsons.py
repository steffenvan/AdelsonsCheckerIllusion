import os
import numpy as np


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator
from PIL import Image
from matplotlib.backends.backend_agg import FigureCanvasAgg

from bokeh.io import show
from bokeh.layouts import widgetbox, column, row, layout
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, TextInput, RadioGroup, Toggle, Div
from bokeh.plotting import figure, curdoc
from bokeh.models.plots import Plot
from bokeh.models import ColumnDataSource, Range1d
from itertools import islice
from bokeh.models.callbacks import CustomJS
from bokeh.models.sources import ColumnDataSource


# Folder where background images are stored
staticRsrcFolder = ""
# variations_folder = "illusionApp/variations"
# if not os.path.exists(variations_folder):
#     os.makedirs(variations_folder)
# path_name = os.path.join(os.path.basename(os.path.dirname(__file__)), "", "variation")
# print(path_name)
default_parameters = {
    "shade_id": None,
    "originalID": None # Represents the actual ID of our illusion. 
}

## This variable specifies the parameter variations we will apply 
illusion_variations = {
    1: {"originalID": 1}, 
    2: {"shade_id": 2, "originalID": 2}, 
    3: {"shade_id": 3, "originalID": 3}, 
    4: {"shade_id": 4, "originalID": 4}    
}


remaining_indices = range(max(illusion_variations.keys()) + 1, max(illusion_variations.keys()) + 1)
# for i, shade in zip(remaining_indices, shade): 
#     illusion_variations[i] = {"shade_id": shade, "originalID": i}
    
llusion_count = len(illusion_variations)

## This dictionary contains the final illusion parameters for each illusion variation we will 
illusion_variation_dict = {}
illusions_to_modify = list(illusion_variations.keys())

# Create a dictionary with default parameters
for i in illusions_to_modify: 
    illusion_variation_dict[i] = default_parameters.copy()

# Modify the parameters according to our illusion variations 
for variationId, variation in illusion_variations.items(): 

    # print("Variation id: ", variationId)
    for key, value in variation.items(): 
        # print("key: {0}, value: {1} ".format(key, value))
        illusion_variation_dict[variationId][key] = value
        print("Assigned value: ", value)
        print("dictionary: ", illusion_variation_dict[variationId][key])


# Make sure number of illusions adds up
#assert not illusions_to_modify
def fig2data ( fig ):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()
 
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = np.fromstring ( fig.canvas.tostring_argb(), dtype=np.uint8 )
    buf.shape = ( w, h, 4)
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll ( buf, 3, axis = 2 )
    return buf

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

    variations_folder = os.path.abspath(staticRsrcFolder)
    variations_list_path = os.path.join(variations_folder, "variation"+str(vID))
    dir_as_list = os.listdir(variations_list_path)
    variation_length = len(os.listdir(variations_list_path))
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
    return "Adelsons Checker illusion"

def getInstructions():
    "Returns the instructions as a HTML string"
    
    instruction = """
        <p>Look at tile A and B - notice that they seem disimilar? They are not".</p>
    """
    return instruction

def getQuestion():
    "Returns a string with a Yes/No question that checks if the participant sees the illusion inverted"

    return "Do the squares appear similar?"


def getNumVariations():
    "Returns the number of variations"
    return 4


def draw(variationID, distortion):
    """This function generates the optical illusion figure.
    The function should return a bokeh figure of size 500x500 pixels.
    :param variationID: select which variation to draw (range: 0 to getNumVariations()-1)
    :param distortion: the selected distorion (range: 0.0 to 1.0)
    :return handle to bokeh figure that contains the optical illusion
    """

    bokehFig = figure(plot_width=500, plot_height=500, x_range=(0, 1), y_range=(0, 1))
    #p.outline_line_color = None
    bokehFig.toolbar.active_drag = None
    bokehFig.toolbar.logo = None
    bokehFig.toolbar_location = None
    bokehFig.xaxis.visible = None
    bokehFig.yaxis.visible = None
    bokehFig.xgrid.grid_line_color = None
    bokehFig.ygrid.grid_line_color = None

    filenames = return_files(variationID)
    variationsFolder = os.path.join(staticRsrcFolder, "variation"+str(variationID))

    # Rounding the distortion value to nearest integer
    shadowDistortion = round(distortion)

    # Absolute path to the specific variation folder
    # The specific file to show is indexed by the distortion value.
    file = os.path.join(variationsFolder, filenames[shadowDistortion])
    print("Distortion: ", shadowDistortion)
    print("File: ", file)

    bokehFig.image_url(url=[file], x=0, y=1, w=None, h=None)

    return bokehFig