import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go

house_file = "housing_prices.csv"
house_data = pd.read_csv(house_file)

#Show a histogram of the distribution of floors in the dataset. 
#What's a half of a floor????

fig = px.histogram(house_data["floors"], x='floors', title='Floors distribution',
    labels={ "floors": "Floors number", "count": "??????"})
fig.update_layout(bargap=0.2, plot_bgcolor="white",
    xaxis=dict(
        showline=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2
    ),
    yaxis=dict(
        showline=True,
        showgrid=True, gridcolor='rgb(204, 204, 204)', 
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
    ))
#fig.show()

# Show a line plot of the average price vs the amount of floors.
# Since plotly takes a df I create a new df with two columns
new_df = house_data[["floors", "price"]].groupby('floors').mean()
prices = [[x] for x in new_df['price'].tolist()]
idx = new_df.index.tolist()
price_vs_floors_df = pd.DataFrame(prices, idx)

fig = px.line(price_vs_floors_df, title='Houses price based on floors number', 
    labels={ "index": "Floors number", "value": "Mean house price"})
fig.update_layout(showlegend=False, plot_bgcolor="white",
    xaxis=dict(
        showline=True,
        showgrid=True,
        gridcolor='rgb(204, 204, 204)',
        gridwidth=0.1,  
        linecolor='rgb(204, 204, 204)', 
        linewidth=2
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        gridwidth=0.1,
        gridcolor='rgb(204, 204, 204)',        
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
    )
)
#fig.show()

#Show a line of the average price per floor vs the amount of floors.
#Create a new list of prices vs amount of floors that would be the new column
price_per_floor = []
prices_list = [float(x[0]) for x in prices]
for num in range(len(idx)):
    price_per_floor.append(prices_list[num]/idx[num])

fig = px.line(price_per_floor, title='Price per floor based on number of floors in the house',
    labels={ "index": "Number of floors", "value": "Price per floor"})
fig.update_layout(showlegend=False, plot_bgcolor="white",
    xaxis=dict(
        showline=True,
        showgrid=True,
        gridcolor='rgb(204, 204, 204)',
        gridwidth=0.1,  
        linecolor='rgb(204, 204, 204)', 
        linewidth=2
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        gridwidth=0.1,
        gridcolor='rgb(204, 204, 204)',        
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
    ))
#fig.show()

#Show a line plot with error bars (stdev) of the price vs the year built, and in the same figure, with legend, price vs year renovated.

def operations(col1,col2,mean=False,std=False):
    cols=[col1,col2]
    df=house_data.loc[:,cols].set_index(col2).sort_index()
    col2_mean=[]
    col2_std=[]
    if mean == True:
        col2_mean=df.groupby(level=0).mean() 
    if std == True:
        col2_std=df.groupby(level=0).agg({'price':'std'})
    return col2_mean,col2_std

price_yr_built_mean,price_yr_built_std=operations("price","yr_built",True,True)
price_yr_renovated_mean,price_yr_renovated_std=operations("price","yr_renovated",True)


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=price_yr_built_mean.index.tolist(),
    y=price_yr_built_mean.price.tolist(),
    error_y=dict(
        type="data", 
        array=price_yr_built_std,
        visible=True),
    mode="lines+markers", name="Price vs year built"
    ))

fig.add_trace(go.Scatter(
    x=price_yr_renovated_mean.drop(0).index.tolist(),
    y=price_yr_renovated_mean.drop(0).price.tolist(),
    mode="lines+markers", name="Price vs year renovated"
    ))

fig.update_layout(
    title="House prices by year built and year renovated",
    showlegend=True,
    plot_bgcolor="white",
    xaxis_title="Year",
    yaxis_title="Price",
    xaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
    )
)

#fig.show()