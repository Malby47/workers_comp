import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('raw_data/WorkersCompensation.csv')

claimsno = df.groupby('Number of Claims').size()

print(claimsno)
