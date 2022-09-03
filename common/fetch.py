#!/usr/bin/env python3

import os
import sys
import requests
import hashlib
from datetime import date
from typing import Optional
from dateutil.relativedelta import relativedelta

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


def set_url(ticker:str, interval:str, years_of_data:Optional[str]=None) -> str:
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
    :param start_date: First date of historical data. Format: %y-%m-%d
    :type start_date: string | None
    :return: URL to the data download, examples above.
    :rtype: string
  """

  today = date.today()
  begin_date = (today - relativedelta(years=years_of_data)).strftime('%Y%m%d')
  end_date = today.strftime('%Y%m%d')
  if years_of_data is None:
    # all possible data 
    url = f'https://stooq.com/q/d/l/?s={ticker}&i={interval}'
  else:
    url = f'https://stooq.com/q/d/l/?s={ticker}&d1={begin_date}&d2={end_date}&i={interval}'
  return url

if __name__ == "__main__":
  url = set_url('^SPX', 'm', 50)
  print(url)
  file_path = fetch(url)
  print(file_path)
