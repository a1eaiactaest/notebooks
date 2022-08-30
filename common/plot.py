#!/usr/bin/env python3

import math
import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib import ticker as mplticker
import matplotlib.pyplot as plt

import fetch
from lib import least_squares

def trendline_stdev(ticker: str):
  data_url = fetch.set_url(ticker, 'm')
  file_path = fetch.fetch(data_url)

  df = pd.read_csv(file_path)

  Y = np.log10(df['Close'])
  X = range(df.shape[0])
  est, slope, y_intercept = least_squares(X,Y)

  DATES_INTERVAL = df.shape[0]//10

  fig, ax = plt.subplots(figsize=(20,10))

  len_range = range(df.shape[0])

  plt.plot(len_range, Y)

  plt.plot(len_range, est, '--k', label='least squares method trend')

  plt.plot(len_range, est + np.std(est)/2, "r", label="+ 2 STDEV")
  plt.plot(len_range, est + np.std(est)/4, "r", label="+ 1 STDEV")
  plt.plot(len_range, est - np.std(est)/4, "g", label="- 1 STDEV")
  plt.plot(len_range, est - np.std(est)/2, "g", label="- 2 STDEV")

  legend = plt.legend(loc='upper left')
  ax.yaxis.set_major_formatter(mplticker.FuncFormatter(lambda y, _: '{:g}'.format(10**y)))

  plt.xticks(range(0, df.shape[0], DATES_INTERVAL), df['Date'].loc[::DATES_INTERVAL], rotation=45)

  plt.grid(True)
  plt.title(ticker)
  plt.ylabel('Close price in USD')

  plt.show()


if __name__ == "__main__":
  trendline_stdev('ETH.V')
