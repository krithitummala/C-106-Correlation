import csv
from time import sleep
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    roll_no = []
    percentage = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            roll_no.append(float(row["Roll No"]))
            percentage.append(float(row["Marks In Percentage"]))
    return{
         "x" : roll_no,
         "y" : percentage
    }

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Roll No", y = "Marks On Percentage")
        fig.show()

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between temperature and ice cream sales is",correlation[0,1])

def setup():
    data_path = "marks.csv"
    data_source = getDataSource(data_path)
    plotFigure(data_path)
    findCorrelation(data_source)

setup()
