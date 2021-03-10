#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061144.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
#first task
count=0
for row in data[:]:
    if row['HUMD'] == -99.000:
        data[row]=[]
        count=count+1
    if row['HUMD'] == -999.000:
        data[row]=[]
        count=count+1
#    target_data=[target_data temp]
target_data = data[:10]

#second task
summ1=summ2=summ3=summ4=summ5=0
for row in data[:]:
    if (row['station_id']=='C0A880'):
        temp=float(row['HUMD'])
        summ1=summ1+temp
    if (row['station_id']=='C0F9A0'): 
        temp=float(row['HUMD'])
        summ2=summ2+temp
    if (row['station_id']=='C0G640'): 
        temp=float(row['HUMD'])
        summ3=summ3+temp
    if (row['station_id']=='C0R190'):
        temp=float(row['HUMD'])
        summ4=summ4+temp
    if (row['station_id']=='C0X260'):
        temp=float(row['HUMD'])
        summ5=summ5+temp
if summ1==0:
    summ1=str['None']
if summ1==0:
    summ2=str['None']
if summ1==0:
    summ3=str['None']
if summ1==0:
    summ4=str['None']
if summ1==0:
    summ5=str['None']
#third task
output=[['C0A880',str(summ1)],['C0F9A0',str(summ2)],['C0F9A0',str(summ3)],['C0R190',str(summ4)],['C0X260',str(summ5)]]

    
    
#=======================================

# Part. 4
#=======================================
# Print result
print(output)
#========================================


# In[ ]:




