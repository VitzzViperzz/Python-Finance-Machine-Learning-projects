import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# start = dt.datetime(2000, 1,1)
# end = dt.datetime(2017,8,19)
# df = web.DataReader('AMZN', 'google', start, end)
# df.to_csv('AMZN.csv')

df = pd.read_csv('AMZN.csv', parse_dates = True, index_col=0)

print(df[['Open','High']].head())


df['Close'].plot()
plt.show()