import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df=pd.read_csv('data.csv')
data=df['temp'].tolist()
fig=ff.create_distplot([data],['temp'],show_hist=False)
fig.show()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print('population mean is :',population_mean)
print('standard deviation is :',std_deviation)

def random_set_of_mean(counter):
  data_set=[]
  for i in range(0,counter):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    data_set.append(value)
  mean=statistics.mean(data_set)
  #std_deviation1=statistics.stdev(data_set)
  return mean
  #print('standard deviation of sample is : ',std_deviation1)

def show_fig(mean_list):
  df=mean_list
  fig=ff.create_distplot([df],['temp'],show_hist=False)
  mean=statistics.mean(mean_list)
  print('mean of sampling distribution is :',mean)
  std_deviation=statistics.stdev(mean_list)
  print('standard deviation of sampling distribution is : ',std_deviation)
  fig.show()

def setup():
  mean_list=[]
  for i in range(0,100):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
  show_fig(mean_list)

setup()