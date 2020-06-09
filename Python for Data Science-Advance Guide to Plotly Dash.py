import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from numpy import random

app = dash.Dash()

# initiate dataframe
df = pd.DataFrame(columns=['time', 'cats'])

app.layout = html.Div([
    dcc.Graph(
        id='graphid',
        figure={
            'data': [
                go.Scatter(x=df['time'], y=df['cats'], mode = 'lines+markers')
            ],
            'layout': {
                'title': 'Stock Price for X over time'
            }
        }
    ),
    dcc.Interval(
        id='1-second-interval',
        interval=1000, # 2000 milliseconds = 2 seconds
        n_intervals=0
    ),
    
])

@app.callback(Output('graphid', 'figure'),
              [Input('1-second-interval', 'n_intervals')])
def update_layout(n):
    df.loc[n] = [n,random.randint(10)]
    figure={
            'data': [
                go.Scatter(x=df['time'], y=df['cats'], mode = 'lines+markers')
            ],
            'layout': {
                'title': 'Stock Price for X over time'
            }
        }
    return figure

if __name__ == '__main__':
    app.run_server()