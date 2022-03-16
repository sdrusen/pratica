import pandas as pd
import numpy as np
import plotly
import plotly.express as px

house_file = "housing_prices.csv"
house_data = pd.read_csv(house_file)

#Show a histogram of the distribution of floors in the dataset.
'''fig = px.histogram(house_data["floors"], title='Logarithmic distribution of floors', labels={'Floors':'Count'}, log_y=True)
fig.update_layout(bargap=0.2)
fig.show()
'''
# Show a line plot of the average price vs the amount of floors.
df = house_data[["floors", "price"]]
new_df = df.groupby('floors').mean()

#fig = px.line(new_df, x="price", y="price", title='Price based on floors number')
#fig.show()

#Show a line of the average price per floor vs the amount of floors.


#Show a line plot with error bars (stdev) of the price vs the year built, and in the same figure, with legend, price vs year renovated.





