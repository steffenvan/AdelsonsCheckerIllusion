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

default_parameters = {
    "originalID": None # Represents the actual ID of our illusion. 
}

## This variable specifies the parameter variations we will apply 
illusion_variations = {
    1: {"originalID": 1}, 
    2: {"originalID": 2}, 
    3: {"originalID": 3}, 
    4: {"originalID": 4}    
}

# remaining_indices = range(max(illusion_variations.keys()) + 1, len(angles) + max(illusion_variations.keys()) + 1)
# for i, ang in zip(remaining_indices, angles): 
#     illusion_variations[i] = {"pattern_angle": ang, "originalID": i}
    
llusion_count = len(illusion_variations)

## This dictionary contains the final illusion parameters for each illusion variation we will 
# display to the subject. 
illusion_variation_dict = {}
illusions_to_modify = list(illusion_variations.keys())

# Create a dictionary with default parameters
for i in illusions_to_modify: 
    illusion_variation_dict[i] = default_parameters.copy()

# Modify the parameters according to our illusion variations 
for variationId, variation in illusion_variations.items(): 
    for key, value in variation.items(): 
        illusion_variation_dict[variationId][key] = value


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

## More complex implementation of the pattern. 
# Allows to specify the angle of the black lines.

def plot_variations(filename, offset=.05, linewidth=4, figsize=(20, 20), dpi=150):
    """"Generate striped pattern, and save as .png. 
    
    :param filename: the filename to save the pattern to
    :param angle: the angle of the lines 
    :param offset: the distance between the lines
    :param linewidth: the width of the liens 
    :param figsize: the size of the saved image
    :param dpi: the dpi of the image"""
    fig = plt.figure(figsize=figsize, dpi=dpi, frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ## Generate lines at an angle 
    # angle_radians = np.radians(angle)
        
    # Remove as much whitespace around plot as possible. 
    ax.set_ylim(0., 1.)
    ax.set_xlim(0., 1.)
    a=fig.gca()
    a.set_frame_on(False)
    a.set_xticks([])
    a.set_yticks([])
    plt.axis('off')
    ax.axis('off')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.clf()
    plt.close()

def plot_illusion():
#     """Combine striped patterns to get our illusion background
    
#     :param angle: the angle of the lines 
#     :param size: the size of the figure
#     :param offsets: the space between the lines for each pattern (manually determined, depend on the image scale)
#     :param linewidth: the thickness of the line 
#     :param linewidth_step: increase the line thickness by this amount for every smaller pattern
#     :param dpi: the dpi of the output image
#     :param force_replot: if true, will redraw the pattern every time, otherwise load from disc 
    
#     :return: list of filenames that contain the patterns"""
#     size=pattern_square_widthfig2
#     offsets=[0.03, 0.05, 0.08, 0.21]
#     linewidth=8.
#     linewidth_step=1.
#     dpi=100
#     # force_replot=force_replot
    # size_step = size / 4
    # variation_length = len(os.listdir(variations_folder))
    # filenames = [] 
    # for i in range(variation_length):
    #     filename = "{}/variation_{}.png".format(variations_folder, i)
    #     plot_variations(filename)    
    #     # linewidth += linewidth_step
    # Decrease size of figure
        # size -= size_step
    # Alternate the angle
    #     filenames.append(filename)
    # return filenames
    return 

def init(_staticRsrcFolder):
    """This function will be called before the start of the experiment
    and can be used to initialize variables and generate static resources
    
    :param _staticRsrcFolder: path to a folder where static resources can be stored
    """
    global staticRsrcFolder
    staticRsrcFolder = _staticRsrcFolder

    # global variations
    # variations = "variations"

    # if not os.path.exists(pattern_folder):
    #     os.makedirs(pattern_folder)

    # Generate the images of the background pattern in advance, to save computation  
    for _ in illusion_variation_dict.values(): 
        plot_illusion()


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
    return llusion_count


def draw(variationID, distortion):
    """This function generates the optical illusion figure.
    The function should return a bokeh figure of size 500x500 pixels.

    :param variationID: select which variation to draw (range: 0 to getNumVariations()-1)
    :param distortion: the selected distorion (range: 0.0 to 1.0)
    :return handle to bokeh figure that contains the optical illusion
    """

    ## Create bokeh figure and disable axes and tools
    bokehFig = figure(plot_width=500, plot_height=500, x_range=(0, 1), y_range=(0, 1))
    fig = plt.figure(figsize=(20, 20), dpi=100)
    path = os.path.abspath(staticRsrcFolder)
    # Change relative path to 
    # TODO: modify, so this does not become necessary
    os.chdir(path)
    variations_list = os.listdir(path)
    img = Image.open(variations_list[variationID])
    plt.imshow(img, interpolation="none", aspect="equal", origin='upper')




    illusion_selector = variationID+1
    # distort = (distortion*2-1)*0.15
    print("path for variations: ", path)
    ### Render final figure 
    ax = fig.add_axes([0, 0, 1, 1])
    
    # Clean extra whitespace around the plot and remove axes 
    axes = plt.gca()
    axes.set_xlim([0., 100.])
    axes.set_ylim([0., 100.])
    plt.axis('off')
    axes.xaxis.set_major_locator(NullLocator())
    axes.yaxis.set_major_locator(NullLocator())

    # convert matplotfig to bitmap and display it on bokeh figure
    bokehFig.image_rgba([np.flip(fig2data(fig),0)], x=[0], y=[0], dw=[1], dh=[1]) 

    #img = Image.fromarray(fig2data(fig), 'RGBA')
    #img.save('my.png')    

    plt.close(fig)
    return bokehFig
