#program to retrieve the tweets from github
import pandas as pd
from datetime import datetime
from datetime import timedelta
#string=[]
#generate today time
datenow= datetime.now().date()
date=input("enter the date:(2019-04-17)")
company=input("enter the name of the company")
header=['Id','Text','Date','Time','Followers count']

date=datetime.strptime(date,"%Y-%m-%d").date()
url="https://raw.githubusercontent.com/d4datas/twitterdata/master/"+str(company)+"-final-"+str(date)+".csv"
sort_by_time=pd.read_csv(url,sep='\^',error_bad_lines=False,names=header,usecols = ['Id','Text','Date','Followers count'],skiprows='1',engine='python')
#sort_by_time = val.sort_values('Date',ascending=False)
#sort_by_time.drop_duplicates(subset ='Id',keep = False, inplace = True)

datenow=datenow-timedelta(days=1)
#for i in range(0,5):
while date<datenow:
	date=date+timedelta(days=1)
	url="https://raw.githubusercontent.com/d4datas/twitterdata/master/"+str(company)+"-final-"+str(date)+".csv"
	sort_by_time1=pd.read_csv(url,sep='\^',error_bad_lines=False,names=header,usecols = ['Id','Text','Date','Followers count'],skiprows='1',engine='python')
	#sort_by_time1 = val1.sort_values('Date',ascending=False)
	#sort_by_time1.drop_duplicates(subset ='Id',keep = False, inplace = True)
	sort_by_time = pd.concat([sort_by_time, sort_by_time1], ignore_index=True)

sort_by_time.drop_duplicates(subset ='Id',keep = False, inplace = True)
sort_by_time.drop_duplicates(subset = 'Text',keep = False, inplace = True)
print(sort_by_time)
#sort_by_time.to_csv("new1.csv")
