#importing libraries
from bs4 import BeautifulSoup
import requests
import csv
import os

#Setting up path and csv file name
name="Laliga_results_fixed.csv"
path ="C:\\Users\\Servando\\Documents\\Datasets\\my_csvs\\"
complete = os.path.join(path,name)
#Requesting html and creating a BeautifulSoup object
url ='https://www.laliga.com/laliga-santander/clasificacion'
data = requests.get(url).text
obj1= BeautifulSoup(data,'html.parser')

#Navigating the tags to extract the information of interest
rows = obj1.find_all("p",{'class':{'styled__TextRegularStyled-sc-1raci4c-0 glrfl','styled__TextRegularStyled-sc-1raci4c-0 cIcTog'}},limit=210)


#Data wrangling/processing
txt=[]
idx=0
complete_list=[]
new_list=[]


for row in rows[10:]:
    txt.append([row.text])

for i in txt:
    if idx !=10:
        new_list.extend(i)
    else:
        complete_list.append(new_list)
        idx=0
        new_list=[]
        new_list.extend(i)

    idx+=1

#Creating top columns and writing csv file with clean data
column_names = ['Abreviation','Team','Points','PJ','PG','PE','PP','GF','GC','DG']

with open(complete,"w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(column_names)
    for info in complete_list:
        writer.writerow(info)
print("Process it's done")