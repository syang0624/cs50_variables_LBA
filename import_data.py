
#Import packages
import pandas as pd #Use pandas to import .csv file
pd.set_option('max_rows', 100) #shows all parts of table from the data set
#tells matplotlib to display figures in the notebook and not in a separate window
import seaborn as sns #use seaborn package for in case if I want to make my #dataviz look nicer
sns.set(color_codes=True) 

#import data from simplified .csv file
data = pd.read_csv("Assignment 2 Data collection - Sheet1.csv")
time = data["Time"]
percentage = data["% of people who are wearing their masks incorrectly"].tolist()#define list for the future calculations
data
