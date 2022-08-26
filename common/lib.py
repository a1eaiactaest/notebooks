#!/usr/bin/env python3

from typing import List, Union

def mean(arr: List[Union[int, float]]) -> Union[int, float]:
  return sum(arr)/len(arr)

def least_squares(X: List[Union[int,float]], Y: List[Union[int, float]]):
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
  return slope

    
def test_ls():
  a1 = [_ for _ in range(1,8)]
  a2 = [1.5, 3.8, 6.7, 9.0, 11.2, 13.6, 16]
  print(least_squares(a1, a2))


if __name__ == "__main__":
  test_ls()
