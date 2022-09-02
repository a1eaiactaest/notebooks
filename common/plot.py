#!/usr/bin/env python3

import sys
import math
import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib import ticker as mplticker
import matplotlib.pyplot as plt

import fetch
from lib import least_squares, standard_deviation

def trendline_stdev(ticker:str, start_date:str=None, interval:str='m')-> None:
  """Fetch and plot data for a specific asset.

    :param ticker: Ticker of the asset recognizable by stooq.com.
    :type ticker: string
    :param start_date: Start date of time series axis.
    :type start_date: string 
    :param interval: Frequency of the data samples. (d, w, m, q, y)
    :type interval: string
    :return: None
  """

  data_url = fetch.set_url(ticker, interval, start_date)
  file_path = fetch.fetch(data_url)
  print(file_path)

  df = pd.read_csv(file_path)

  Y = np.log10(df['Close'])
  X = range(df.shape[0])
  est, slope, y_intercept = least_squares(X,Y)
  print(slope, y_intercept)
  print('mean: ', sum(est)/len(est))
  print(standard_deviation(est))
  print(np.std(est))

  SD = np.std(est)

  DATES_INTERVAL = df.shape[0]//10

  fig, ax = plt.subplots(figsize=(20,10))

  len_range = range(df.shape[0])

  plt.plot(len_range, Y)

  plt.plot(len_range, est, '--k', label='least squares method trend')

  plt.plot(len_range, est + SD/4, "r", label="+ 2 STDEV")
  plt.plot(len_range, est + SD/2, "r", label="+ 1 STDEV")
  plt.plot(len_range, est - SD/2, "g", label="- 1 STDEV")
  plt.plot(len_range, est - SD/4, "g", label="- 2 STDEV")

  legend = plt.legend(loc='upper left')
  ax.yaxis.set_major_formatter(mplticker.FuncFormatter(lambda y, _: '{:g}'.format(10**y)))

  plt.xticks(range(0, df.shape[0], DATES_INTERVAL), df['Date'].loc[::DATES_INTERVAL], rotation=45)

  plt.grid(True)
  plt.title(ticker)
  plt.ylabel('Close price in USD')

  plt.show()

if __name__ == "__main__":
  ticker = sys.argv[1]
  try: 
    interval = sys.argv[2]
    start_date = sys.argv[3] # 2020-01-01
    trendline_stdev(ticker, start_date, interval)
  except IndexError:
    trendline_stdev(ticker)

