import pandas as pd
import os

# read data into a dataframe and split by L, W, H
data = pd.read_csv("list_of_presents.csv", sep = "x", header = 0,  names = ["Length", "Width", "Height"])

def total_material(L,W,H):
  sa = 2*(L*W+W*H+H*L)
  sorted_dims = sorted([L, W, H])
  min = sorted_dims[0]
  mid = sorted_dims[1]
  max = sorted_dims[2]
  extra = min*mid
  total = sa + extra
  return total

data['result'] = data.apply(lambda row: total_material(row['Length'], row['Width'], row['Height']), axis=1)

print(f"Total wrappping material needed: {data.result.sum()}")
