#program to retrieve the news from github
import pandas as pd
from datetime import datetime
from datetime import timedelta
#generate today time
datenow = datetime.now().date()
datenow = datenow-timedelta(days=1)
#datenow="2019-04-19"
#datenow=datetime.strptime(datenow, '%Y-%m-%d').date()
date=input("enter the date:(2019-04-17)")
#date = "2019-04-10"
headers = ['ticker','company', 'date', 'title', 'news', 'priority']
print("Retrieving days...")
date = datetime.strptime(date, '%Y-%m-%d').strftime('%m%d%Y')
#getting data
url = "https://raw.githubusercontent.com/d4datas/stocknews/master/news_"+str(date)+".csv"
val = pd.read_csv(url,names = headers,usecols = ['ticker','date','title', 'news'],engine = 'python')

#val.drop_duplicates(subset ='news',keep = False, inplace = True)
#print(val)

date = datetime.strptime(date,'%m%d%Y').strftime('%Y-%m-%d')
date = datetime.strptime(date,'%Y-%m-%d').date()
while date < datenow:

	date = date + timedelta(days=1)
	date = datetime.strptime(str(date), '%Y-%m-%d').strftime('%m%d%Y')
	#if  no news on that day,skip
	try:
		url="https://raw.githubusercontent.com/d4datas/stocknews/master/news_"+str(date)+".csv"
		val1=pd.read_csv(url,names=headers,usecols=['ticker','date','title', 'news'],engine='python')

		val = pd.concat([val, val1], ignore_index=True)

	except:
		#print("not found")
		pass
	date = datetime.strptime(date,'%m%d%Y').strftime('%Y-%m-%d')
	date = datetime.strptime(date,'%Y-%m-%d').date()
val.drop_duplicates(subset ='news',keep = False, inplace = True)
print()
print(val)
#to generate csv file
#val.to_csv("new1.csv")
