import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='glinzac', api_key='moDRm2Z9SEjJnBVKfsPQ')


def graph(symbol,df):
    data = [go.Scatter(x=df.price_date, y=df['close_price'])]
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
		    )
		)
    fig = dict(data=data,layout=layout)
    py.iplot(fig, filename = 'basic-graph.html')

def find_price(symbol,df):
	len =df.shape[0]
	close = df['close_price'].values;
	last_price = close[len-1]
	secondlast_price = close[len-2]
	return secondlast_price,last_price