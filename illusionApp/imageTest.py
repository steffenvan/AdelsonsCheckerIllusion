from bokeh.plotting import figure, show, output_file

output_file('image.html')

p = figure(x_range=(0,1), y_range=(0,1))
p.image(url=['pngs/standard.png'], x=0, y=1)
show(p)