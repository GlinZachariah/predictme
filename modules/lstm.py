# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:52:39 2019

@author: glinzac
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')    #fivethirtyeight

with plt.style.context(('dark_background')):
    plt.plot([1,2,3,4],[1,4,9,16])

x = [1,2,3,4,5]
y = [10,11,14,16,17]

line, = plt.plot(x,y)    # x,y,fmt,scalex,scaley

line, = plt.plot(x,y,linewidth=4.0)
line, = plt.plot(x,y,'ro')      #color-marker-linestyle eg: r/g/b ./o/v/1/2  -/--/-./:

line.set_linestyle('--')
line.set_antialiased(False)

plt.setp(line,color='r',linewidth=2.0)

x = np.arange(start=0.0,stop=30.0,step=0.1)

plt.subplot(2,1,1)
plt.plot(x,np.sin(x),'b.-')

plt.subplot(2,1,2)
plt.plot(x,np.cos(x),'r--')

plt.show()