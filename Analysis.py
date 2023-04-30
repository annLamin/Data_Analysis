import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

class Analysis():
    def __init__(self, new_data):
        self.new_data = new_data
        
        
    def statistics(self):
        stats = self.new_data.describe()
        stats.to_csv('Results/statistics1.csv', index=True,sep=',')
    def correlation(self):
        corrmatrix = self.new_data.corr()
        fig = plt.figure(figsize = (12, 9))
        sns.heatmap(corrmatrix, vmax = .9, square = True)
        fig.figure.savefig("Results/correlation1.pdf")
        #plt.show()
    def scatter_plot(self):
        grp_by_country = self.new_data.groupby('country')
        data2 = pd.DataFrame(grp_by_country.size()).rename(columns = {0:'no. of bookings'}).sort_values('no. of bookings', ascending = False)
        data2 = data2[:10]
        scatter=sns.scatterplot(x = data2.index, y = data2['no. of bookings'])
        plt.show()
        scatter.figure.savefig('Results/Scatterplot11.pdf')
    def box_plot(self):
        months = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
        self.new_data['arrival_date_month'] = pd.Categorical(self.new_data['arrival_date_month'],categories=months,ordered=True)
        plt.figure(figsize = (15,8))
        plot2 = sns.boxplot(x = self.new_data['arrival_date_month'],y = self.new_data['adr'])
        plot2.figure.savefig('Results/Boxplot1.pdf')
    def barplot(self):
        grouped_by_hotel = self.new_data.groupby('hotel')
        data11 = pd.DataFrame((grouped_by_hotel.size()/self.new_data.shape[0])*100).reset_index().rename(columns = {0:'Booking %'})      #Calculating percentage
        plt.figure(figsize = (8,5))
        plot3 = sns.barplot(x = data11['hotel'], y = data11['Booking %'] )
        plot3.figure.savefig('Results/Barplot1.pdf')
        #plt.show()
    def barplot2(self):
        bar = pd.DataFrame(self.new_data['agent'].value_counts()).reset_index().rename(columns = {'index':'agent','agent':'num_of_bookings'}
                                                                   ).sort_values(by = 'num_of_bookings', ascending = False)
        bar.drop(bar[bar['agent'] == 0].index, inplace = True)            # 0 represents that booking is not made by an agent
        bar = bar[:10]                                                   # Selecting top 10 performing agents
        plt.figure(figsize = (10,8))
        sns.barplot(x = 'agent', y = 'num_of_bookings', data = bar, order = bar.sort_values('num_of_bookings', ascending = False).agent)
        plt.savefig('Results/Agent-bookings.pdf')
        #plt.show()
    def lineplot(self):
        months = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
        sorted_months = self.new_data.arrival_date_month.value_counts().reindex(months)
        x = sorted_months.index
        y = sorted_months/sorted_months.sum()*100
        plt.figure(figsize=(15,8))
        plt.xlabel('Months')
        plt.ylabel('Booking (%)')
        plt.title('Monthly booking trend')
        plt.plot(x, y)
        plt.grid()
        plt.savefig('Results/lineplot.pdf')
        plt.show()
def complete_analysis(new_data):
    new_data = Analysis(new_data)
    new_data.statistics()
    new_data.correlation()
    new_data.barplot()
    new_data.scatter_plot()
    new_data.barplot2()
    new_data.box_plot()
    new_data.lineplot()
new_data = pd.read_csv('Results/cleaned_data1.csv')
complete_analysis(new_data)