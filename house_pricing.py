import pandas as pd
import numpy as np
import plotly
import plotly.express as px

house_file = "housing_prices.csv"
house_data = pd.read_csv(house_file)

#Show a histogram of the distribution of floors in the dataset. 
#What's a half of a floor????

fig = px.histogram(house_data["floors"], x='floors', title='Distribution of floors')
fig.update_layout(bargap=0.2)
#fig.show()

# Show a line plot of the average price vs the amount of floors.
# Since plotly takes a df I create a new df with two columns
df = house_data[["floors", "price"]].groupby('floors').mean()
prices = [[x] for x in df['price'].tolist()]
idx = df.index.tolist()
price_vs_floors_df = pd.DataFrame(prices, idx)

fig = px.line(price_vs_floors_df, title='Houses price based on floors number', 
                labels={ "index": "Floors number", "value": "Mean house price"})
fig.update_layout(showlegend=False)
#fig.show()

#Show a line of the average price per floor vs the amount of floors.
#Create a new list of prices vs amount of floors that would be the new column
price_per_floor = []
prices_list = [float(x[0]) for x in prices]
for num in range(len(idx)):
    price_per_floor.append(prices_list[num]/idx[num])

fig = px.line(price_per_floor, title='Price per floor based on number of floors in the house',
                labels={ "index": "Number of floors", "value": "Price per floor"})
fig.update_layout(showlegend=False)
#fig.show()

#Show a line plot with error bars (stdev) of the price vs the year built, and in the same figure, with legend, price vs year renovated.

#Line plot of the price vs the year built
cols1 = ["price","yr_built"]
price_yr_built = house_data.loc[:,cols1].set_index('yr_built').sort_index()
price_yr_built = price_yr_built.groupby(level='yr_built').mean().mean(axis=1).reset_index(name='val').set_index('yr_built').sort_index()

fig = px.line(price_yr_built, title='Price per floor based on number of floors in the house', error_y="e")
#fig.show()






