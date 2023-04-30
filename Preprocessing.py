import pandas as pd
import numpy as np
import csv
class PreProcessing():
    def __init__(self, data):
        self.data = data
        
        
    def clean_data(self):
        data = self.data
        #data.drop('Unnamed: 0', axis=1, inplace=True)
        for col in data.columns:
            if np.sum(data[col].isnull())>(data.shape[0]*0.8):
                data.drop(columns=col, inplace=True) # This will drop company because it has more than 80% missing values
            #df.drop("company",axis=1, inplace=True)
            data["country"].fillna(data.country.mode().to_string(), inplace=True)
            data.dropna(subset=["agent"], inplace=True)
            data["agent"].fillna(data.country.mode().to_string(), inplace=True)
            data["children"].fillna(round(data.children.mean()), inplace=True)
            
        print(f'The shape of the data: {data.shape}')
        #print(f'Total Number of Null values: {data.isnull().sum().sum()}')
    def data_format(self):
        data = self.data
        data['arrival_date']=pd.to_datetime(data.arrival_date_year.astype(str)+'/'+data.arrival_date_month.astype(str)+'/'+data.arrival_date_day_of_month.astype(str))
        data.drop(columns=["arrival_date_week_number","arrival_date_day_of_month"],inplace=True)
        data[["children","agent",]]=data[["children","agent"]].astype('int64')
        data['total_stay'] = data['stays_in_weekend_nights']+data['stays_in_week_nights']
        data.drop(data[data['adr'] > 5000].index, inplace = True)
        data.drop_duplicates(inplace=True)
        print(f'The shape of the data: {data.shape}')    
        data.to_csv('Results/cleaned_data1.csv', index=False,sep=',')
        #print(f'Total Number of Null values: {data.isnull().sum().sum()}')
        
def total_preprocessing(data):
    data = PreProcessing(data)
    data.clean_data()
    data.data_format()
    return data.data
data = pd.read_csv('hotel_bookings.csv')
total_preprocessing(data)