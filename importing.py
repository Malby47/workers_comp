import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('raw_data/Review-Decisions.csv', header=0)

pivotframe = df.set_index(['Appeal year', 'appellant', 'Review outcome'])

print(pivotframe)
