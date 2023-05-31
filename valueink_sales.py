# -*- coding: utf-8 -*-
"""
Created on Mon May  8 10:10:14 2023

@author: david
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

# Summary of the datat
data.info()

# Working with calculations
# Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased*SellingPricePerItem

# CostPerTransaction Calculation

# CostPerTransaction = NumberofItemsPurchased
# variable = dataframe{'column_name"}

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to dataform

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - CostDay+'-+

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales -Cost)/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Rounding markup

roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#Combining data fields

data['date'] = data['Day']+'-'+data['Month']+'-'+data['Year']

my_date = data['Day']
data['my_date'] = data['Day']
# data['date'] = my_date

#Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
roundday = round(data['Day'])
roundyear = round(data['Year'])
data['Day'] = round(data['Day'])
data['Year'] = round(data['Year'])
my_date = day+'-'+data['Month']+'-'+year
data['date'] = my_date
my_date = data['my_date'].astype(str)

#using iloc to view specific columns/rows

data.iloc[0] #views for rows with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column

data.iloc[4,2] #brings in 4th row, 2nd column

#split to split the client keywords field
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords,,'].str.split(',' , expand=True)

#create new columns for the split columns in ClientKeyword

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofTheContract'] = split_col[2]                              

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofTheContract'] = data['LengthofTheContract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping colums

# df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords,,', axis =1)

data = data.drop('Day', axis = 1)

data = data.drop (['Year', 'Month'], axis = 1)
data = data.drop('my_date', axis = 1)

#export into a csv

data.to_csv('ValueInc_Cleaned.csv', index = False)




