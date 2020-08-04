import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from time import sleep

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2019, 12, 31)


# def eval():
df = web.DataReader('TSLA', 'yahoo', start, end)
# print(df.info())
print(df.tail(10))
# eval()
# sleep(2)

# print(df.tail())


# x = df['Open', 'Close'].plot(figsize=(15, 5))
# print(x)
