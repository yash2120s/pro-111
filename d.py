import pandas as pd
import plotly.figure_factory as ff
import csv
import random 
import statistics
import plotly.graph_objects as go

df = pd.read_csv("data1.csv")
data = df['Math_score'].tolist()
fig = ff.create_distplot([data],["Math_score"],show_hist= False,show_rug=False)
fig.show()

m = statistics.mean(data)
dev = statistics.stdev(data)
print("m =>" ,m ,"stv =>" , dev )