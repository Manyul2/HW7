#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:41:25 2023

@author: laura
"""

#!/usr/bin/env python
# coding: utf-8

# # Manyu Luo HW7


# ! pip install pandas_datareader
import os
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas_datareader import wb
import requests
from bs4 import BeautifulSoup


# ### Question 1


# create start and end date
start = datetime.date(year=2000, month=1, day=1)
end= datetime .date(year=2010, month=12, day=31)

# monthly interest rate for us
# read in 
interest_us = web.DataReader('INTDSRUSM193N', 'fred', start, end)
# rename interest rate column
interest_us = interest_us.rename(columns = {'INTDSRUSM193N' : 'interest_rate'})
# convert to annual frequency
interest_us = interest_us.resample('A').mean()
# add country column
interest_us['country'] = 'United States'
# get date column
interest_us = interest_us.reset_index()
# convert date column to yaer format
interest_us['DATE'] = interest_us['DATE'].dt.to_period('A')
# rename date column
interest_us = interest_us.rename(columns = {'DATE' : 'date'})

# monthly interest rate for us
# read in
interest_kr = web.DataReader('INTDSRKRM193N', 'fred', start, end)
# rename interest rate column
interest_kr = interest_kr.rename(columns = {'INTDSRKRM193N' : 'interest_rate'})
# convert to annual frequency
interest_kr = interest_kr.resample('A').mean()
# add country column
interest_kr['country'] = 'Korea, Rep.'
# get date column
interest_kr = interest_kr.reset_index()
# convert date column to year format
interest_kr['DATE'] = interest_kr['DATE'].dt.to_period('A')
# rename date column
interest_kr = interest_kr.rename(columns = {'DATE' : 'date'})

# annual gdp for us
# read in
gdp_us = wb.download(indicator = 'NY.GDP.MKTP.CD', country = 'US', start = 2000, end = 2010)
# sort out by year
gdp_us = gdp_us.reset_index().set_index('year').sort_index().reset_index()
# rename columns
gdp_us = gdp_us.rename(columns = {'NY.GDP.MKTP.CD' : 'gdp', 'country' : 'region'})

# annual gdp for korea
# read in
gdp_kr = wb.download(indicator = 'NY.GDP.MKTP.CD', country = 'KR', start = 2000, end = 2010)
# sort out by year
gdp_kr = gdp_kr.reset_index().set_index('year').sort_index().reset_index()
# rename columns 
gdp_kr = gdp_kr.rename(columns = {'NY.GDP.MKTP.CD' : 'gdp', 'country' : 'region'})



# concatenate us interest rate with gdp
us = pd.concat([interest_us, gdp_us], axis = 1)[['date', 'country', 'interest_rate', 'gdp']]
# concatenate korea interest rate with gdp
kr = pd.concat([interest_kr, gdp_kr], axis = 1)[['date', 'country', 'interest_rate', 'gdp']]
# concatenate us and korea dataframes
q1 = pd.concat([us, kr], axis = 0).reset_index().drop(columns = 'index')

q1.head()


os.chdir('/Users/laura/Documents/GitHub/HW7')
os.getcwd()

# output to csv
q1.to_csv('q1.csv', index=False)


# ### Question 2


# read in url
url = 'https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')



# get required courses
required_1 = soup.find('h3', text = 'Required courses').find_next('ul').find_all('li')
required_2 = soup.find('h3', text = 'Required courses').find_next('ul').find_next('ul').find_all('li')
# get elective courses
elective = soup.find('h3', text = 'Elective courses').find_next('ul').find_all('li')



csv_doc = []
# store required courses into csv_doc
for des in required_1:
    des = des.get_text()
    lis = [index for index, item in enumerate(des.split()) if item.isdigit()]
    code = ' '.join(des.split()[: lis[-1] + 1])
    course = ' '.join(des.split()[lis[-1] + 1:])
    typ = 'required'
    csv_doc.append(', '.join([typ, code, course]) + '\n')
for des in required_2:
    des = des.get_text()
    lis = [index for index, item in enumerate(des.split()) if item.isdigit()]
    code = ' '.join(des.split()[: lis[-1] + 1])
    course = ' '.join(des.split()[lis[-1] + 1:])
    typ = 'required'
    csv_doc.append(', '.join([typ, code, course]) + '\n')
# store elective courses into csv_doc
for des in elective:
    des = des.get_text()
    lis = [index for index, item in enumerate(des.split()) if item.isdigit()]
    code = ' '.join(des.split()[: lis[-1] + 1])
    course = ' '.join(des.split()[lis[-1] + 1:])
    typ = 'elective'
    csv_doc.append(', '.join([typ, code, course]) + '\n')



# change commas to slashes to avoid creating extra columns with Winter and Spring
csv_doc[-2] = csv_doc[-2].replace('Autumn, Winter, Spring', 'Autumn/Winter/Spring')




# create column names
header = 'type,code,course\n'
csv_doc.insert(0, header)
document = ''.join(csv_doc)




# write to csv file
with open(os.getcwd()+'/q2.csv', 'w') as ofile:
    ofile.write(document)



# read in as pandas dataframe
df = pd.read_csv('q2.csv')




df.head()



# assert the dataframe has 16 rows and three columns
assert df.shape == (16, 3)




