import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the dataset
df = pd.read_csv('h1n1_vaccine_prediction.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
# Define the layout of the app
app.layout = html.Div([
    html.H1("H1N1 Vaccine Prediction Dashboard"),
    
    html.Div([
        dcc.Dropdown(
            id='dropdown-column',
            options=[
                {'label': 'Column 1', 'value': 'column1'},
                {'label': 'Column 2', 'value': 'column2'},
                # Add more options as needed
            ],
            value=None,  # Set default value
            placeholder='Select a column'
        ),
        dcc.Graph(id='correlation-heatmap'),
        dcc.Graph(id='categorical-countplot'),
    ])
])


# Define callbacks
@app.callback(
    Output('correlation-heatmap', 'figure'),
    Output('categorical-countplot', 'figure'),
    [Input('dropdown-column', 'value')]
)
def update_charts(selected_column):
    # Correlation heatmap
    corr = df.corr()
    fig1 = px.imshow(corr, x=corr.index, y=corr.columns, color_continuous_scale='RdBu', title='Correlation Heatmap')

    # Categorical countplot
    if selected_column:
        fig2 = px.histogram(df, x=selected_column, title=f'Countplot of {selected_column}')
    else:
        fig2 = px.histogram(df, x='default_column', title='Countplot of default_column')
    
    return fig1, fig2

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True , port = 8086)
