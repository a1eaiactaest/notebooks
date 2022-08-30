#!/usr/bin/env python3

import os
import sys
import requests
import hashlib
from datetime import date
from typing import Optional

def fetch(url: str) -> str:
  fp = os.path.join('/tmp', hashlib.md5(url.encode('utf-8')).hexdigest())

  if os.path.isfile(fp):
    with open(fp, 'rb') as file:
      data = file.read()
  else:
    with open(fp, 'wb') as file:
      data = requests.get(url).content
      file.write(data)
  return fp    


def set_url(ticker: str, interval: str, start_date: Optional[str] = None) -> str:
  """Set url for stooq.com csv download.
    Example  URLs:
      Data for S&P 500 since 1789 monthly.
      https://stooq.com/q/d/l/?s=^spx&i=m
      
      Date for S&P 500 since 2010-05-01 to 2022-09-29 monthly.
      https://stooq.com/q/d/l/?s=^spx&d1=20100501&d2=20220929&i=m
    
    :param ticker: Ticker of the asset recognizable by stooq.com.
    :type ticker: string
    :param interval: Frequency of the data samples. (d, w, m, q, y)
    :type interval: string
    :param start_date: First date of historical data.
    :type start_date: string | None
    :return: URL to the data download, examples above.
    :rtype: string
  """

  today = date.today()
  end_date = today.strftime('%Y%m%d')
  if start_date is None:
    # all possible data 
    url = f'https://stooq.com/q/d/l/?s={ticker}&i={interval}'
  else:
    start_date = ''.join(start_date.split('-'))
    url = f'https://stooq.com/q/d/l/?s={ticker}&d1={start_date}&d2={end_date}&i={interval}'
  return url


if __name__ == "__main__":
  url = set_url('BTCUSD', 'm', '2021-10-28')
  print(url)
  file_path = fetch(url)
  print(file_path)
