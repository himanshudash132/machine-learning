import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori


store_data = pd.read_csv('store_data.csv',header=None)
num_records = len(store_data)
print(num_records)
