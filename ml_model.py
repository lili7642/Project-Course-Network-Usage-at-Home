import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_columns', None)


current_directory = os.path.dirname(__file__)
f_path = current_directory + "/../../project_course_data/"
csv_filename = "owndata_processed.csv"

# read csv
data = pd.read_csv(f_path + csv_filename, sep=",", na_values="NaN")

# 




