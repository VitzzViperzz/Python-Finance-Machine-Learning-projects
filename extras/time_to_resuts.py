import numpy as np        
import pandas as pd        
from pandas_datareader import data, wb

goog = data.DataReader('GOOG', data_source='google',                      
 	start='3/14/2009', end='4/14/2014')        

goog.tail()
