import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='glinzac', api_key='moDRm2Z9SEjJnBVKfsPQ')


def graph(symbol,df):
    trace1 = go.Scatter(
    	x=df.price_date, 
    	y=df['volume'],
    	name="volume"
	    )
    trace2 = go.Scatter(
    	x=df.price_date, 
    	y=df['open_price'],
    	name="open_price"
	    )
    trace3 = go.Scatter(
    	x=df.price_date, 
    	y=df['high_price'],
    	name="high_price"
	    )
    trace4 = go.Scatter(
    	x=df.price_date, 
    	y=df['low_price'],
    	name="low_price"
	    )
    trace5 = go.Scatter(
    	x=df.price_date, 
    	y=df['adj_close_price'],
    	name="adj_close_price"
	    )
    trace6 = go.Scatter(
    	x=df.price_date, 
    	y=df['close_price'],
    	name="close_price"
	    )
    # data = [go.Scatter(x=df.price_date, y=df['close_price'],text=str(df.open_price)+"<br/>"+str(df.close_price)+"<br/>"+str(df.high_price)+"<br/>"+str(df.low_price)+"<br/>"+str(df.adj_close_price)+"<br/>"+str(df.volume))]
    layout = dict(
	    title='',
	    xaxis=dict(
		        rangeselector=dict(
		        	borderwidth =0,
		        	bgcolor='rgb(255, 255,255)',
		            buttons=list([
		            	dict(count=5,
		                     label=' 5 days ',
		                     step='day',
		                     stepmode='backward'),
		                dict(count=1,
		                     label=' 1 month ',
		                     step='month',
		                     stepmode='backward'),
		                dict(count=6,
		                     label=' 6 month ',
		                     step='month',
		                     stepmode='backward'),
		                dict(count=1,
		                     label=' YTD ',
		                     step='year',
		                     stepmode='todate'),
		                dict(count=1,
		                     label=' 1 year ',
		                     step='year',
		                     stepmode='backward'),
		                dict(step='all',
		                	 label=' Max ')
		            ])
		        ),
		        rangeslider=dict(
		            visible = True
		        ),
		        type='date'
		    ),
		)
    data =[trace1,trace2,trace3,trace4,trace5,trace6]
    fig = dict(data=data,layout=layout)
    py.iplot(fig, filename = 'basic-graph.html')

def find_price(symbol,df):
	len =df.shape[0]
	close = df['close_price'].values;
	last_price = close[len-1]
	secondlast_price = close[len-2]
	return secondlast_price,last_price

# plotly.tools.set_credentials_file(username='glincool.zac', api_key='rmrECoBzqWNa3uG6sCkY')

# def graph(symbol,df):
#     trace1 = go.Scatter(
#     	x=df.price_date, 
#     	y=df['volume'],
#     	name="volume"
# 	    )
#     trace2 = go.Scatter(
#     	x=df.price_date, 
#     	y=df['open_price'],
#     	name="open_price"
# 	    )
#     trace3 = go.Scatter(
#     	x=df.price_date, 
#     	y=df['high_price'],
#     	name="high_price"
# 	    )
#     trace4 = go.Scatter(
#     	x=df.price_date, 
#     	y=df['low_price'],
#     	name="low_price"
# 	    )
#     trace5 = go.Scatter(
#     	x=df.price_date, 
#     	y=df['adj_close_price'],
#     	name="adj_close_price"
# 	    )
#     trace6 = go.Scatter(
#     	x=df.price_date, 
#     	y=df['close_price'],
#     	name="close_price"
# 	    )
#     # data = [go.Scatter(x=df.price_date, y=df['close_price'],text=str(df.open_price)+"<br/>"+str(df.close_price)+"<br/>"+str(df.high_price)+"<br/>"+str(df.low_price)+"<br/>"+str(df.adj_close_price)+"<br/>"+str(df.volume))]
#     layout = dict(
# 	    title='',
# 	    xaxis=dict(
# 		        rangeselector=dict(
# 		        	borderwidth =0,
# 		        	bgcolor='rgb(255, 255,255)',
# 		            buttons=list([
# 		            	dict(count=5,
# 		                     label=' 5 days ',
# 		                     step='day',
# 		                     stepmode='backward'),
# 		                dict(count=1,
# 		                     label=' 1 month ',
# 		                     step='month',
# 		                     stepmode='backward'),
# 		                dict(count=6,
# 		                     label=' 6 month ',
# 		                     step='month',
# 		                     stepmode='backward'),
# 		                dict(count=1,
# 		                     label=' YTD ',
# 		                     step='year',
# 		                     stepmode='todate'),
# 		                dict(count=1,
# 		                     label=' 1 year ',
# 		                     step='year',
# 		                     stepmode='backward'),
# 		                dict(step='all',
# 		                	 label=' Max ')
# 		            ])
# 		        ),
# 		        rangeslider=dict(
# 		            visible = True
# 		        ),
# 		        type='date'
# 		    ),
# 		)
#     # data =[trace1,trace2,trace3,trace4,trace5,trace6]
#     data =[trace6]
#     fig = dict(data=data,layout=layout)
#     py.iplot(fig, filename = 'basic-graph.html')