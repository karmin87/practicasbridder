from videocap import df
from bokeh.plotting import figure,show,output_file
from bokeh.models import ColumnDataSource

p=figure(x_axis_type='datetime',height=100,width=500,responsive=True,title="Motion Graph")

q=p.quad(left="start",right="end",bottom=0,top=1,color="green")

output_file("motion_graph.html")

show(p)



