import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  
df=pd.read_csv("Groceries.csv")
df.head(10)
# Aggregate purchases by month
monthly_purchases = df.groupby('month').size()

plt.figure(figsize=(5, 3)) 
sns.lineplot(x=monthly_purchases.index, y=monthly_purchases.values, marker='o', linestyle='-')  # Create the line plot
plt.title('Distribution of Purchases by Month')  
plt.xlabel('Month')  
plt.ylabel('Number of Purchases')  
plt.show() 