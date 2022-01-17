import csv
from time import sleep
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{
         "x" : coffee,
         "y" : sleep
    }

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between temperature and ice cream sales is",correlation[0,1])

def setup():
    data_path = "coffee.csv"
    data_source = getDataSource(data_path)
    plotFigure(data_path)
    findCorrelation(data_source)

setup()
