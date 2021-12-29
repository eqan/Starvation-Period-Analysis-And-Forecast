import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r'./Project-Dataset.csv', skiprows=range(1,55))

n=len(data)
r = np.arange(n)
width = 0.25
  
plt.bar(r, (data["Wheat Consumption Growth Rate"] + data["Barley Consumption Growth Rate"] + data["Meat Consumption Growth Rate"] + data["Rice Consumption Growth Rate"] )/4, color = 'b',
        width = width, edgecolor = 'black',
        label='Production')

plt.bar(r+width, (data["Wheat Production Growth Rate"] + data["Barley Production Growth Rate"] + data["Meat Production Growth Rate"] + data["Rice Production Growth Rate"] )/4, color = 'g',
        width = width, edgecolor = 'black',
        label='Consumption')

plt.bar(r+width*2, data["Hunger Annual Change"], color = 'y',
        width = width, edgecolor = 'black',
        label='Hunger')


plt.xlabel("Year")
plt.ylabel("Annual Rate")
plt.title("Comparison of Consumption & Production of Wheat with Hunger Growth")
  
plt.xticks(r + width/2, data["Year"])
plt.legend()
  
plt.show()