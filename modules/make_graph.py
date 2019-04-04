import pandas as pd
import plotly
plotly.tools.set_credentials_file(username='glinzac', api_key='moDRm2Z9SEjJnBVKfsPQ')
import plotly.plotly as py
import plotly.graph_objs as go

def graph(symbol,df):
    df.price_date =pd.to_datetime(df.price_date)
    df = df.sort_values('price_date')
    data = [go.Scatter(x=df.price_date, y=df['close_price'])]
    py.iplot(data, filename = 'basic-graph.html')
