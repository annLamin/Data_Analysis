import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
import Preprocessing as pp
from Preprocessing import total_preprocessing
import Analysis as ca
import warnings
import csv
warnings.filterwarnings("ignore")

data = pd.read_csv('hotel_bookings.csv')
data = pp.total_preprocessing(data)
#data.to_csv('Results/cleaned_data1.csv', index=True,sep=',')
new_data = pd.read_csv('Results/cleaned_data1.csv')
ca.complete_analysis(new_data)
