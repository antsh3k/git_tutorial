import pandas as pd
import os

# read data into a dataframe and split by L, W, H
data = pd.read_csv("list_of_presents.csv", sep = "x", header = 0,  names = ["Length", "Width", "Height"])

def total_material(L,W,H):
  sa = 2*(L*W+W*H+H*L)
  extra = L*W
  total = sa + extra
  return total

data['result'] = data.apply(lambda row: total_material(row['Length'], row['Width'], row['Height']), axis=1)

print(f"Total wrappping material needed: {data.result.sum()}")
