import numpy as np
import pandas as pd

ser1 = pd.Series(['A','B','C','D'])
print("Series 1:\n",ser1)
ser2 = pd.Series({'a': "Nagpur",'b': 'Mumbai','c':'Hyderabad',"d": "Chennai"})
print("Series 2 :\n",ser2)

ser1[0] = 'NEW'
print("Series 1:\n",ser1)
ser3 = ser2
print("Series 3:\n",ser3)
ser3 = pd.Series(['China', 'America'], index=['e','f'])
print("Series 3:\n",ser3)
