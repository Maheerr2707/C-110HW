import csv
import pandas as pd
import statistics
import statistics
import plotly.figure_factory as ff
import random

df = pd.read_csv("StudentsPerfomance.csv") 

templist = df["reading_time"].tolist()
populationMean = statistics.mean(templist)
print(populationMean)
population_stddev = statistics.stdev(templist)
print(population_stddev)

def randomSetofMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(templist)-1)
        value = templist[randomIndex]
        dataSet.append(value)
    sampleMean = statistics.mean(dataSet)
    sampleStDev = statistics.stdev(dataSet)
    return sampleMean

def setup():
    meanList = []
    for i in range(0,1000):
        setofMean = randomSetofMean(100)
        meanList.append(setofMean)
    mean = statistics.mean(meanList)
    print("Sample Mean=",mean)
    show_fig(meanList)
    print("standarddeviation=",statistics.stdev(meanList))


def show_fig(meanList):
    fig = ff.create_distplot([meanList],["temp"],show_hist=False)
    fig.show()

#show_fig(templist)
setup()    