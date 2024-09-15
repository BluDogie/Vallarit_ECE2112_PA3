#PROBLEM 1: Save your file as Surname_Pandas-P1.py
#Using knowledge obtained from the experiment and demonstrations:

#a. Load the corresponding .csv file into a data frame named cars using pandas
#b. Display the first five and last five rows of the resulting cars.

import pandas as pd #import pandas library

cars = pd.read_csv("cars.csv") #load the .csv file into a data frame named cars using pandas

# For Letter A
cars.iloc[:,::2].head() # Use iloc to specifically get which columns to display, specifically the columns that are odd-numbered.
# : to display all rows
# ::2 to start at the beginning and step by 2.