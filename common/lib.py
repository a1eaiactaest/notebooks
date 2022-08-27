#!/usr/bin/env python3

from typing import List, Union, Tuple

def mean(arr: List[Union[int, float]]) -> Union[int, float]:
  return sum(arr)/len(arr)

def least_squares(X: List[Union[int,float]], Y: List[Union[int, float]]) -> Tuple[list, float, float]:
  """Ordinary least squares method."""

  assert len(X) == len(Y)

  N = len(X)

  X_mean = mean(X)
  Y_mean = mean(Y)
  
  X_sigma = sum(X)
  Y_sigma = sum(Y)

  XY_sigma = 0
  X_squared_sigma = 0

  for x,y in zip(X,Y):
    XY_sigma += x*y
    X_squared_sigma += x**2
    
  slope = ((N * XY_sigma) - (X_sigma * Y_sigma)) / ((N * X_squared_sigma) - (X_sigma)**2)
  y_intercept = (Y_sigma - slope * X_sigma) / N

  slope_intercept = lambda x: (slope * x) + y_intercept

  estimates = []
  for x,y in zip(X,Y):
    estimation_y = slope_intercept(x)
    estimates.append(estimation_y)

  return estimates, slope, y_intercept

def test_ls():
  a1 = [_ for _ in range(1,8)]
  a2 = [1.5, 3.8, 6.7, 9.0, 11.2, 13.6, 16]
  est, _, _ = least_squares(a1, a2)
  # 2.4142857142857133
  # -0.8285714285714231
  for e, a in zip(est, a2):
    error = a - e
    print(round(e), round(a))
    print(error) 

if __name__ == "__main__":
  test_ls()
