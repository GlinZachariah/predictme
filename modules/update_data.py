from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd
from datetime import datetime 
import numpy as np

def upd(symbol):
	cnx = sqlite3.connect('db.sqlite3')
	conn = cnx.cursor()
	df = pd.read_sql_query("SELECT * FROM mainapp_"+symbol.lower(), cnx)
	df.price_date =pd.to_datetime(df.price_date)
	ln =df.shape[0]
	new_date = df['price_date'].values;
	last_date = new_date[ln-1]
	last_date =np.datetime64(last_date,'D')
	dat =str(last_date)
	last_date =datetime.strptime(dat, "%Y-%m-%d").date()
	tick =symbol.upper()
	page = requests.get("https://in.finance.yahoo.com/quote/"+str(tick)+"/history?p="+str(tick))
	soup = BeautifulSoup(page.content, 'html.parser')
	cnts=[]
	lst=[]
	for row in soup.find_all('tr'):
		cnts.append(row)
	for k in range(1,len(cnts)-1):
		data= cnts[k]
		l = []
		for j in data:
			l.append(j.get_text())
		if len(l) ==7 :
			final_date = l[0]
			f_date =datetime.strptime(final_date, "%d-%b-%Y").date()
			if f_date>last_date:
				lst.append(l)
	for i in range(len(lst)-1,-1,-1):
		dat =lst[i][0]
		dt =datetime.strptime(dat, "%d-%b-%Y").date()	
		op = lst[i][1]
		high = lst[i][2]
		low = lst[i][3]
		clse = lst[i][4]
		adj_cl = lst[i][5]
		vol = lst[i][6]
		# print(dt)
		conn.execute("INSERT INTO mainapp_"+symbol+''' (price_date,open_price,high_price,low_price,close_price,adj_close_price,volume) VALUES(?,?,?,?,?,?,?)''',(dt,op,high,low,clse,adj_cl,vol))
	cnx.commit()
	cnx.close()