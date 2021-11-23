import pandas as pd
import plotly.figure_factory as ff
import csv
import random 
import statistics
import plotly.graph_objects as go


df = pd.read_csv("data3.csv")
data = df['Math_score'].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list) 



first_std_deviation_start,first_std_deviation_end = mean - std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean -(2*std_deviation) , mean + ( 2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean -(3*std_deviation) , mean + ( 3*std_deviation)

print("std1" , first_std_deviation_start,first_std_deviation_end)
print("std2" , second_std_deviation_start,second_std_deviation_end)
print("std3" , third_std_deviation_start,third_std_deviation_end)

fig = ff.create_distplot([mean_list],["mean_list"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y =[0.17],mode = "lines" , name = "Mean"))
fig.add_trace(go.Scatter(first_std_deviation_start,))
fig.show()

print(mean,std_deviation)