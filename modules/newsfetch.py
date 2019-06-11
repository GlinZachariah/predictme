#new code to display news
#pip install newsapi-python

from newsapi import NewsApiClient
import pandas as pd
import re
from datetime import datetime

# Authentication
def gen_news(comp,fr_date):
	newsapi = NewsApiClient(api_key='545c1ff6522c4d3bb728c586421e8d70')
	datenow= datetime.now().date()
	#convert inputs to arguments
	company=""
	# date=input("enter the date:(2019-04-17)")
	if comp== "CSCO":
	 	company="cisco"
	elif comp=="MSFT":
		company="microsoft"
	# company = input("enter company name(eg:cisco):")
	# fr_date = input("enter the from date(eg:-2019-05-30):")
	all_news = newsapi.get_everything(q=str(company),
	                                      from_param=str(fr_date),
	                                      to=str(datenow),
	                                      language='en',
	                                      sort_by='relevancy',
	                                      page=2)

	df = pd.DataFrame({'news_date': [], 'news': []})

	for articl in all_news["articles"]:
		#print(articl["description"])
		new = articl["publishedAt"]
		match = re.search(r'\d{4}-\d{2}-\d{2}', new)
		new_date = datetime.strptime(match.group(), '%Y-%m-%d').date()
		#print(new_date)
		df = df.append({'news_date': new_date, 'news': articl["description"]}, ignore_index=True)
	df.drop_duplicates(subset = 'news',keep = False, inplace = True)
	df.sort_values(by=['news_date'], inplace=True, ascending=False)
	return df
