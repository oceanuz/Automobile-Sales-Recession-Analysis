import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv'
)

# Initialize app
app = dash.Dash(__name__)

year_list = [i for i in range(1980, 2024)]

# Layout
app.layout = html.Div([

    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 24}
    ),

    dcc.Dropdown(
        id='dropdown-statistics',
        options=[
            {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
            {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
        ],
        placeholder='Select a report type',
        style={'width': '80%', 'margin': 'auto'}
    ),

    dcc.Dropdown(
        id='select-year',
        options=[{'label': i, 'value': i} for i in year_list],
        placeholder='Select-year',
        style={'width': '80%', 'margin': 'auto'}
    ),

    html.Div(id='output-container', className='chart-grid')

])

# Enable / Disable year dropdown
@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_year_dropdown(stat):
    return stat != 'Yearly Statistics'


# Update graphs
@app.callback(
    Output('output-container', 'children'),
    [
        Input('dropdown-statistics', 'value'),
        Input('select-year', 'value')
    ]
)
def update_output_container(stat, year):

    if stat == 'Recession Period Statistics':

        recession_data = data[data['Recession'] == 1]

        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        avg_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        unemp = recession_data.groupby(
            ['unemployment_rate', 'Vehicle_Type']
        )['Automobile_Sales'].mean().reset_index()

        return [
            dcc.Graph(figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
                                     title='Average Automobile Sales During Recession')),
            dcc.Graph(figure=px.bar(avg_sales, x='Vehicle_Type', y='Automobile_Sales',
                                    title='Average Automobile Sales by Vehicle Type')),
            dcc.Graph(figure=px.pie(exp_rec, values='Advertising_Expenditure',
                                    names='Vehicle_Type',
                                    title='Advertising Expenditure Share')),
            dcc.Graph(figure=px.bar(unemp, x='unemployment_rate',
                                    y='Automobile_Sales', color='Vehicle_Type',
                                    title='Effect of Unemployment Rate on Sales'))
        ]

    elif stat == 'Yearly Statistics' and year:

        yearly_data = data[data['Year'] == year]

        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        mas = data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        avg_vehicle = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        exp_year = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()

        return [
            dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales',
                                     title='Average Yearly Automobile Sales')),
            dcc.Graph(figure=px.line(mas, x='Month', y='Automobile_Sales',
                                     title='Total Monthly Automobile Sales')),
            dcc.Graph(figure=px.bar(avg_vehicle, x='Vehicle_Type', y='Automobile_Sales',
                                    title=f'Average Vehicles Sold in {year}')),
            dcc.Graph(figure=px.pie(exp_year, values='Advertising_Expenditure',
                                    names='Vehicle_Type',
                                    title='Advertisement Expenditure by Vehicle Type'))
        ]

    return []


# Run app
if __name__ == '__main__':
    app.run(debug=True)
