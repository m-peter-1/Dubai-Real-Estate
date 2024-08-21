# This script performs an initial exploration of the Dubai real estate dataset.
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the Dubai real estate dataset
df = pd.read_csv('dubai_properties.csv')
# Display the first few rows of the dataset to inspect
print(df.head())
