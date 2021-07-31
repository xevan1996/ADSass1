from django.shortcuts import render
from django.http import HttpResponse
from myassignment.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.views.generic import TemplateView, View 

from movie.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from movie.models import UserProfileInfo

import re
import csv
import numpy as np
import pandas as pd
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sb

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'movie/index.html', context=None)

class Api(TemplateView):

    def movie_prod_country(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        real_path = 'Movie Production Countries'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Country', 'No. of Movies', 'Average Production Budget ($)', 'Total Worldwide Box Office ($)']
        country_prod = making_table(csv_file, 1, 5, name_list)

        country_prod = country_prod.drop(country_prod.index[15:])
        temp = country_prod.to_numpy()
        country_prod = spchar_removal(temp, 1, name_list)

        country_prod['No. of Movies'] = country_prod['No. of Movies'].astype(int)
        country_prod['Average Production Budget ($)'] = country_prod['Average Production Budget ($)'].astype(np.int64)
        country_prod['Total Worldwide Box Office ($)'] = country_prod['Total Worldwide Box Office ($)'].astype(np.int64)
        temp = []

        x = []
        temp = country_prod['Country'].to_numpy()
        x = np.append(temp, x)
        y1 = []
        temp = country_prod['No. of Movies'].to_numpy()
        y1 = np.append(temp, y1)


        plt.figure(figsize = (12, 8), dpi= 100)
        plt.bar(x, y1)
        plt.title('Number of Movies vs Country', fontsize = 14)
        plt.xlabel("Country", fontsize = 14)
        plt.ylabel("Number of Movies", color="black", fontsize = 14)
        plt.xticks(rotation = 90)

        plt.grid(True)
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def average_production_budget(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        real_path = 'Movie Production Countries'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Country', 'No. of Movies', 'Average Production Budget ($)', 'Total Worldwide Box Office ($)']
        country_prod = making_table(csv_file, 1, 5, name_list)

        country_prod = country_prod.drop(country_prod.index[15:])
        temp = country_prod.to_numpy()
        country_prod = spchar_removal(temp, 1, name_list)

        country_prod['No. of Movies'] = country_prod['No. of Movies'].astype(int)
        country_prod['Average Production Budget ($)'] = country_prod['Average Production Budget ($)'].astype(np.int64)
        country_prod['Total Worldwide Box Office ($)'] = country_prod['Total Worldwide Box Office ($)'].astype(np.int64)
        temp = []

        x = []
        temp = country_prod['Country'].to_numpy()
        x = np.append(temp, x)
        y1 = []
        temp = country_prod['Average Production Budget ($)'].to_numpy()
        y1 = np.append(temp, y1)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.plot(x, y1, color='red', marker='o', label = 'Average Production Budget')
        plt.title('Average Production Budget vs Country', fontsize = 14)
        plt.xlabel("Country", fontsize = 14)
        plt.ylabel("Average Production Budget ($)", color="black", fontsize = 14)
        plt.xticks(rotation = 90)

        plt.grid(True)
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def total_box_office(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        real_path = 'Movie Production Countries'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Country', 'No. of Movies', 'Average Production Budget ($)', 'Total Worldwide Box Office ($)']
        country_prod = making_table(csv_file, 1, 5, name_list)

        country_prod = country_prod.drop(country_prod.index[15:])
        temp = country_prod.to_numpy()
        country_prod = spchar_removal(temp, 1, name_list)

        country_prod['No. of Movies'] = country_prod['No. of Movies'].astype(int)
        country_prod['Average Production Budget ($)'] = country_prod['Average Production Budget ($)'].astype(np.int64)
        country_prod['Total Worldwide Box Office ($)'] = country_prod['Total Worldwide Box Office ($)'].astype(np.int64)
        temp = []

        x = []
        temp = country_prod['Country'].to_numpy()
        x = np.append(temp, x)
        y1 = []
        temp = country_prod['Total Worldwide Box Office ($)'].to_numpy()
        y1 = np.append(temp, y1)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.plot(x,y1, color='blue', marker='o', label = 'Total Worldwide Box Office')
        plt.title('Total Worldwide Box Office vs Country', fontsize = 14)
        plt.xlabel("Country", fontsize = 14)
        plt.ylabel("Total Worldwide Box Office ($)", color="black", fontsize = 14)
        plt.xticks(rotation = 90)

        plt.grid(True)
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def total_box_year(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        real_path = 'Annual Ticket Sales'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Year', 'Tickets Sold', 'Total Box Office($)', 'Total Inflation Adjusted Box Office($)', 'Average Ticket Price ($)']
        annual_sale = making_table(csv_file, 1, 6, name_list)

        temp = annual_sale.to_numpy()
        annual_sale = spchar_removal(temp, 1, name_list)

        annual_sale['Year'] = annual_sale['Year'].astype(int)
        annual_sale['Tickets Sold'] = annual_sale['Tickets Sold'].astype(np.int64)
        annual_sale['Total Box Office($)'] = annual_sale['Total Box Office($)'].astype(np.int64)
        annual_sale['Total Inflation Adjusted Box Office($)'] = annual_sale['Total Inflation Adjusted Box Office($)'].astype(np.int64)
        annual_sale['Average Ticket Price ($)'] = annual_sale['Average Ticket Price ($)'].astype(float)

        max_year = annual_sale.iloc[0]['Year'].astype(int)
        min_year = annual_sale.iloc[len(annual_sale) - 1]['Year'].astype(int)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.plot(annual_sale['Year'], annual_sale['Total Box Office($)'], color='red', marker='o')
        plt.title('Total Box Office vs Year', fontsize = 14)
        plt.xlabel('Year', fontsize = 14)
        plt.ylabel('Total Box Office($)', fontsize = 14)
        plt.xticks(np.arange(min_year, max_year + 1, 1), rotation = 90)

        plt.grid(True)
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def tikcet_sold_price(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        real_path = 'Annual Ticket Sales'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Year', 'Tickets Sold', 'Total Box Office($)', 'Total Inflation Adjusted Box Office($)', 'Average Ticket Price ($)']
        annual_sale = making_table(csv_file, 1, 6, name_list)

        temp = annual_sale.to_numpy()
        annual_sale = spchar_removal(temp, 1, name_list)

        annual_sale['Year'] = annual_sale['Year'].astype(int)
        annual_sale['Tickets Sold'] = annual_sale['Tickets Sold'].astype(np.int64)
        annual_sale['Total Box Office($)'] = annual_sale['Total Box Office($)'].astype(np.int64)
        annual_sale['Total Inflation Adjusted Box Office($)'] = annual_sale['Total Inflation Adjusted Box Office($)'].astype(np.int64)
        annual_sale['Average Ticket Price ($)'] = annual_sale['Average Ticket Price ($)'].astype(float)

        max_year = annual_sale.iloc[0]['Year'].astype(int)
        min_year = annual_sale.iloc[len(annual_sale) - 1]['Year'].astype(int)

        fig, ax = plt.subplots(figsize = (12, 8), dpi= 100)
        ins1 = ax.plot(annual_sale['Year'], annual_sale['Tickets Sold'], color='red', marker='o', label = 'Tickets Sold')
        ax.set_xlabel("Year", fontsize = 14)
        ax.set_ylabel("Tickets Sold", color="black", fontsize = 14)
        plt.xticks(np.arange(min_year, max_year + 1, 1), rotation = 90)

        ax2=ax.twinx()
        ins2 = ax2.plot(annual_sale['Year'], annual_sale['Average Ticket Price ($)'], color='blue', marker='o', label = 'Average Ticket Price')
        ax2.set_ylabel("Average Ticket Price ($)", color="black", fontsize = 14)

        ins = ins1 + ins2
        labs = [l.get_label() for l in ins]
        ax.legend(ins, labs, loc = 2)

        plt.title('Ticket Sold and Average Ticket Price vs Year', fontsize = 14)
        plt.grid(True)
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def release_per_year(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        real_path = 'Number of Wide Releases Each Year'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Year', 'Warner Bros', 'Walt Disney', '20th Century Fox', 'Paramount Pictures', 'Sony Pictures', 'Universal', 'Total Major 6', 'Total Other Studios']
        distributor_release = making_table(csv_file, 1, 10, name_list)

        distributor_release['Year'] = distributor_release['Year'].astype(str)
        distributor_release['Warner Bros'] = distributor_release['Warner Bros'].astype(int)
        distributor_release['Walt Disney'] = distributor_release['Walt Disney'].astype(int)
        distributor_release['20th Century Fox'] = distributor_release['20th Century Fox'].astype(int)
        distributor_release['Paramount Pictures'] = distributor_release['Paramount Pictures'].astype(int)
        distributor_release['Sony Pictures'] = distributor_release['Sony Pictures'].astype(int)
        distributor_release['Universal'] = distributor_release['Universal'].astype(int)
        distributor_release['Total Major 6'] = distributor_release['Total Major 6'].astype(int)
        distributor_release['Total Other Studios'] = distributor_release['Total Other Studios'].astype(int)

        distributor_release = distributor_release.iloc[::-1]

        temp = []
        x = []
        temp = distributor_release['Year'].to_numpy()
        x = np.append(temp, x)

        distributor_release = distributor_release.drop('Year', axis = 1)
        distributor_release = distributor_release.drop('Total Major 6', axis = 1)

        distributor_percentage = distributor_release.div(distributor_release.sum(axis = 1, numeric_only = True) , axis = 0).multiply(100)

        y1 = []
        temp = distributor_percentage['Warner Bros'].to_numpy()
        y1 = np.append(temp, y1)
        y2 = []
        temp = distributor_percentage['Walt Disney'].to_numpy()
        y2 = np.append(temp, y2)
        y3 = []
        temp = distributor_percentage['20th Century Fox'].to_numpy()
        y3 = np.append(temp, y3)
        y4 = []
        temp = distributor_percentage['Paramount Pictures'].to_numpy()
        y4 = np.append(temp, y4)
        y5 = []
        temp = distributor_percentage['Sony Pictures'].to_numpy()
        y5 = np.append(temp, y5)
        y6 = []
        temp = distributor_percentage['Universal'].to_numpy()
        y6 = np.append(temp, y6)
        y7 = []
        temp = distributor_percentage['Total Other Studios'].to_numpy()
        y7 = np.append(temp, y7)

        plt.figure(figsize = (12, 8), dpi= 100)
        Distributors = ['Warner Bros', 'Walt Disney', '20th Century Fox', 'Paramount Pictures', 'Sony Pictures', 'Universal', 'Total Other Studios']
        plt.bar(x, y1, color = 'red')
        plt.bar(x, y2, bottom = y1, color = 'orange')
        plt.bar(x, y3, bottom = y1+y2, color = 'y')
        plt.bar(x, y4, bottom = y1+y2+y3, color = 'g')
        plt.bar(x, y5, bottom = y1+y2+y3+y4, color = 'c')
        plt.bar(x, y6, bottom = y1+y2+y3+y4+y5, color = 'b')
        plt.bar(x, y7, bottom = y1+y2+y3+y4+y5+y6, color = 'm')
        plt.xticks(rotation = 90)
        plt.legend(Distributors, loc = 'best')
        plt.xlabel("Year")
        plt.ylabel("Movies Production Percentage (%)")
        plt.title("Movies Production Percentage by Different Production Distributor")
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def top_per_year(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        real_path = 'Top Movie of Each Year'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Year', 'Movie', 'Creative Type', 'Production Method', 'Source', 'Genre', 'MPAA Rating', 'Distributor', 'Total for Year ($)', 'Total in 2019 ($)', 'Tickets Sold']
        movie_best = making_table(csv_file, 1, 12, name_list)

        temp = movie_best.to_numpy()
        movie_best = spchar_removal(temp, 8, name_list)

        movie_best['Year'] = movie_best['Year'].astype(int)
        movie_best['Total for Year ($)'] = movie_best['Total for Year ($)'].astype(np.int64)
        movie_best['Total in 2019 ($)'] = movie_best['Total in 2019 ($)'].astype(np.int64)
        movie_best['Tickets Sold'] = movie_best['Tickets Sold'].astype(np.int64)

        temp = []
        y1 = []
        temp = movie_best['Creative Type'].to_numpy()
        y1 = np.append(temp, y1)
        y2 = []
        temp = movie_best['Production Method'].to_numpy()
        y2 = np.append(temp, y2)
        y3 = []
        temp = movie_best['Source'].to_numpy()
        y3 = np.append(temp, y3)
        y4 = []
        temp = movie_best['Genre'].to_numpy()
        y4 = np.append(temp, y4)
        y5 = []
        temp = movie_best['MPAA Rating'].to_numpy()
        y5 = np.append(temp, y5)
        y6 = []
        temp = movie_best['Distributor'].to_numpy()
        y6 = np.append(temp, y6)

        movie_best_new = pd.DataFrame(list(zip(y1, y2, y3, y4, y5, y6)),
                                    columns = ["Creative Type", "Production Method", "Source", "Genre", "MPAA Rating", "Distributor" ])

        all_columns = ['Creative Type', 'Production Method', 'Source', 'Genre', 'MPAA Rating', 'Distributor']
        fig, axs = plt.subplots(2, 3, sharex=False, sharey=False, figsize=(20, 15), dpi= 100)
        counter = 0

        for all_column in all_columns:
            value_counts = movie_best_new[all_column].value_counts()
            
            trace_x = counter // 3
            trace_y = counter % 3
            x_pos = np.arange(0, len(value_counts))
            
            axs[trace_x, trace_y].bar(x_pos, value_counts.values, tick_label = value_counts.index, color='g')
            
            axs[trace_x, trace_y].set_title(all_column)
            
            for tick in axs[trace_x, trace_y].get_xticklabels():
                tick.set_rotation(20)
            
            counter += 1

        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def ticket_sold(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        real_path = 'Top Movie of Each Year'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Year', 'Movie', 'Creative Type', 'Production Method', 'Source', 'Genre', 'MPAA Rating', 'Distributor', 'Total for Year ($)', 'Total in 2019 ($)', 'Tickets Sold']
        movie_best = making_table(csv_file, 1, 12, name_list)

        temp = movie_best.to_numpy()
        movie_best = spchar_removal(temp, 8, name_list)

        movie_best['Year'] = movie_best['Year'].astype(int)
        movie_best['Total for Year ($)'] = movie_best['Total for Year ($)'].astype(np.int64)
        movie_best['Total in 2019 ($)'] = movie_best['Total in 2019 ($)'].astype(np.int64)
        movie_best['Tickets Sold'] = movie_best['Tickets Sold'].astype(np.int64)

        temp = []

        x1 = []
        temp = movie_best['Year'].to_numpy()
        x1 = np.append(temp, x1)

        max_year = x1[-1]
        min_year = x1[0]

        fig, ax = plt.subplots(figsize = (12, 8), dpi= 100)
        ins1 = ax.plot(x1, movie_best['Tickets Sold'], color='red', marker='o', label = 'Tickets Sold')
        ax.set_xlabel("Year", fontsize = 14)
        ax.set_ylabel("Tickets Sold", color="black", fontsize = 14)
        plt.xticks(np.arange(min_year, max_year + 1, 1), rotation = 90)

        ax2=ax.twinx()
        ins2 = ax2.plot(x1, movie_best['Total for Year ($)'], color='blue', marker='o', label = 'Total Sales for Annual Top Movie')
        ax2.set_ylabel("Total Sales for Top Movie ($)", color="black", fontsize = 14)

        ins = ins1 + ins2
        labs = [l.get_label() for l in ins]
        ax.legend(ins, labs, loc = 2)

        plt.title('Ticket Sold and Total Sales for Annual Top Movie vs Year', fontsize = 14)
        plt.grid(True)
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def top_dist_ms(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return '{p:.2f}%'.format(p = pct, v = val)
            return my_autopct
        
        real_path = 'Top-Grossing Distributors 1995 to 2021'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Rank', 'Distributor', 'Number of Movies', 'Total Gross ($)', 'Average Gross ($)', 'Market Share (%)']
        distributor_gross = making_table(csv_file, 0, 6, name_list)

        temp = distributor_gross.to_numpy()
        distributor_gross = spchar_removal(temp, 3, name_list)

        distributor_gross['Rank'] = distributor_gross['Rank'].astype(int)
        distributor_gross['Number of Movies'] = distributor_gross['Number of Movies'].astype(np.int64)
        distributor_gross['Total Gross ($)'] = distributor_gross['Total Gross ($)'].astype(np.int64)
        distributor_gross['Average Gross ($)'] = distributor_gross['Average Gross ($)'].astype(np.int64)
        distributor_gross['Market Share (%)'] = distributor_gross['Market Share (%)'].astype(float)

        temp = []

        x = []
        temp = distributor_gross['Total Gross ($)'].to_numpy()
        x = np.append(temp, x)
        y = []
        temp = distributor_gross['Distributor'].to_numpy()
        y = np.append(temp, y)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.pie(x, labels = y, autopct = make_autopct(x))
        plt.title('Market Share of Different Distributors')
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def top_genre_ms(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return '{p:.2f}%'.format(p = pct, v = val)
            return my_autopct
        
        real_path = 'Top-Grossing Genres 1995 to 2021'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Rank', 'Genre', 'Number of Movies', 'Total Box Office ($)', 'Tickets', 'Market Share(%)']
        genre_sales = making_table(csv_file, 1, 7, name_list)

        temp = genre_sales.to_numpy()
        genre_sales = spchar_removal(temp, 2, name_list)

        genre_sales['Rank'] = genre_sales['Rank'].astype(int)
        genre_sales['Number of Movies'] = genre_sales['Number of Movies'].astype(np.int64)
        genre_sales['Total Box Office ($)'] = genre_sales['Total Box Office ($)'].astype(np.int64)
        genre_sales['Tickets'] = genre_sales['Tickets'].astype(np.int64)
        genre_sales['Market Share(%)'] = genre_sales['Market Share(%)'].astype(float)

        temp = []

        x = []
        temp = genre_sales['Total Box Office ($)'].to_numpy()
        x = np.append(temp, x)
        y = []
        temp = genre_sales['Genre'].to_numpy()
        y = np.append(temp, y)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.pie(x, labels = y, autopct = make_autopct(x))
        plt.title('Market Share of Different Genres')
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def top_mpaa_ms(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return '{p:.2f}%'.format(p = pct, v = val)
            return my_autopct
        
        real_path = 'Top-Grossing MPAA Ratings 1995 to 2021'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Rank', 'MPAA Rating', 'Number of Movies', 'Total Gross ($)', 'Average Gross ($)', 'Market Share (%)']
        MPAA_sales = making_table(csv_file, 0, 6, name_list)

        temp = MPAA_sales.to_numpy()
        MPAA_sales = spchar_removal(temp, 2, name_list)

        MPAA_sales['Rank'] = MPAA_sales['Rank'].astype(int)
        MPAA_sales['Number of Movies'] = MPAA_sales['Number of Movies'].astype(np.int64)
        MPAA_sales['Total Gross ($)'] = MPAA_sales['Total Gross ($)'].astype(np.int64)
        MPAA_sales['Average Gross ($)'] = MPAA_sales['Average Gross ($)'].astype(np.int64)
        MPAA_sales['Market Share (%)'] = MPAA_sales['Market Share (%)'].astype(float)

        temp = []

        x = []
        temp = MPAA_sales['Total Gross ($)'].to_numpy()
        x = np.append(temp, x)
        y = []
        temp = MPAA_sales['MPAA Rating'].to_numpy()
        y = np.append(temp, y)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.pie(x, labels = y, autopct = make_autopct(x))
        plt.title('Market Share of Different MPAA Ratings')
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def top_source_ms(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return '{p:.2f}%'.format(p = pct, v = val)
            return my_autopct
        
        real_path = 'Top-Grossing Sources 1995 to 2021'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Rank', 'Source', 'Number of Movies', 'Total Gross ($)', 'Average Gross ($)', 'Market Share (%)']
        source_sales = making_table(csv_file, 0, 6, name_list)

        temp = source_sales.to_numpy()
        source_sales = spchar_removal(temp, 2, name_list)

        source_sales['Rank'] = source_sales['Rank'].astype(int)
        source_sales['Number of Movies'] = source_sales['Number of Movies'].astype(np.int64)
        source_sales['Total Gross ($)'] = source_sales['Total Gross ($)'].astype(np.int64)
        source_sales['Average Gross ($)'] = source_sales['Average Gross ($)'].astype(np.int64)
        source_sales['Market Share (%)'] = source_sales['Market Share (%)'].astype(float)

        temp = []

        x = []
        temp = source_sales['Total Gross ($)'].to_numpy()
        x = np.append(temp, x)
        y = []
        temp = source_sales['Source'].to_numpy()
        y = np.append(temp, y)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.pie(x, labels = y, autopct = make_autopct(x))
        plt.title('Market Share of Different Sources')
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def top_method_ms(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return '{p:.2f}%'.format(p = pct, v = val)
            return my_autopct
        
        real_path = 'Top-Grossing Production Methods 1995 to 2021'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Rank', 'Production Method', 'Number of Movies', 'Total Gross ($)', 'Average Gross ($)', 'Market Share (%)']
        methods_sales = making_table(csv_file, 0, 6, name_list)

        temp = methods_sales.to_numpy()
        methods_sales = spchar_removal(temp, 2, name_list)

        methods_sales['Rank'] = methods_sales['Rank'].astype(int)
        methods_sales['Number of Movies'] = methods_sales['Number of Movies'].astype(np.int64)
        methods_sales['Total Gross ($)'] = methods_sales['Total Gross ($)'].astype(np.int64)
        methods_sales['Average Gross ($)'] = methods_sales['Average Gross ($)'].astype(np.int64)
        methods_sales['Market Share (%)'] = methods_sales['Market Share (%)'].astype(float)

        temp = []

        x = []
        temp = methods_sales['Total Gross ($)'].to_numpy()
        x = np.append(temp, x)
        y = []
        temp = methods_sales['Production Method'].to_numpy()
        y = np.append(temp, y)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.pie(x, labels = y, autopct = make_autopct(x))
        plt.title('Market Share of Different Production Method')
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def top_creative_ms(request):

        def making_table(csv_file, column_start, column_end, name_list):
            dst = pd.read_csv(csv_file, header = None, index_col = False)
            dst = dst.iloc[:,column_start:column_end].values
            dst_movie = pd.DataFrame(dst, columns = [name_list])
    
            return dst_movie
        
        def spchar_removal(array, starting_column, name_list):
            Lrow = len(array)
            Lcol = len(array[0])
        
            current_row = 0
            current_column = starting_column
        
            while current_column < Lcol:
                current_row = 0
                while current_row < Lrow:
                    array[current_row, current_column] = re.sub(r",", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"\$", "", array[current_row, current_column])
                    array[current_row, current_column] = re.sub(r"%", "", array[current_row, current_column])
                    current_row = current_row + 1
                
                current_column = current_column + 1
            
            dst_movie = pd.DataFrame(array, columns = [name_list])
        
            return dst_movie

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct * total / 100.0))
                return '{p:.2f}%'.format(p = pct, v = val)
            return my_autopct
        
        real_path = 'Top-Grossing Creative Types 1995 to 2021'
        csv_file = MEDIA_ROOT+'/data/'+ real_path +'.csv'
        name_list = ['Rank', 'Creative Type', 'Number of Movies', 'Total Gross ($)', 'Average Gross ($)', 'Market Share (%)']
        creative_sales = making_table(csv_file, 0, 6, name_list)

        temp = creative_sales.to_numpy()
        creative_sales = spchar_removal(temp, 2, name_list)

        creative_sales['Rank'] = creative_sales['Rank'].astype(int)
        creative_sales['Number of Movies'] = creative_sales['Number of Movies'].astype(np.int64)
        creative_sales['Total Gross ($)'] = creative_sales['Total Gross ($)'].astype(np.int64)
        creative_sales['Average Gross ($)'] = creative_sales['Average Gross ($)'].astype(np.int64)
        creative_sales['Market Share (%)'] = creative_sales['Market Share (%)'].astype(float)

        temp = []

        x = []
        temp = creative_sales['Total Gross ($)'].to_numpy()
        x = np.append(temp, x)
        y = []
        temp = creative_sales['Creative Type'].to_numpy()
        y = np.append(temp, y)

        plt.figure(figsize = (12, 8), dpi= 100)
        plt.pie(x, labels = y, autopct = make_autopct(x))
        plt.title('Market Share of Different Creative Type')
        plt.show()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

def index(request):
    return render(request,'movie/index.html')

@login_required
def special(request):
    all_users = UserProfileInfo.objects.select_related('user')
    return HttpResponse(all_users[0].occupation)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else: # if GET request
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'movie/registration.html',
    {'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered}
    )

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'movie/login.html')



