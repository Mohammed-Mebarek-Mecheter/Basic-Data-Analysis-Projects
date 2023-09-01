import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)

# Load your player data (e.g., CSV)
data = pd.read_csv('data/players.csv')

# Define the layout of your dashboard
app.layout = html.Div([
    html.H1('NBA Player Attributes Dashboard'),

    # Visualization 1: Height vs. Weight Scatter Plot
    dcc.Graph(id='scatter-plot',
              figure=px.scatter(data, x='height', y='weight', title='Height vs. Weight')),

    # Visualization 2: Distribution of Player Positions
    dcc.Graph(id='position-distribution',
              figure=px.histogram(data, x='position', title='Distribution of Player Positions')),

    # Visualization 3: Average Height by Draft Year
    dcc.Graph(id='average-height-by-year',
              figure=px.line(data.groupby('draft_year')['height'].mean(),
                             title='Average Height by Draft Year')),

    # Add more visualizations as needed
])

if __name__ == '__main__':
    app.run_server(debug=True)
