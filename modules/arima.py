# import os;
# path="C:/Users/photon/Documents/dataset"
# os.chdir(path)
# os.getcwd()
import pandas
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima_model import ARIMA

def make_model(cdf):
	# var=pandas.read_csv('AAPL.csv')
	price=cdf['Close']
	lnprice=np.log(price)
	price_matrix=lnprice.as_matrix()
	model = ARIMA(price_matrix, order=(5,2,0))
	model_fit = model.fit(disp=0)
	# print(model_fit.summary())
	prediction=model_fit.predict(7380,7385, typ='levels')
	predictionadj=np.exp(prediction)
	return predictionadj
	




