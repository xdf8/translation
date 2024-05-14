import pandas as pd
import os

print(os.getcwd())
df = pd.read_csv("data/aestik_loc_test.csv", index_col="index")
print(df)
