# 필요한 라이브러리를 가져옵니다.
from dash import Dash, html, dash_table
import pandas as pd

# pandas를 이용하여 데이터를 불러옵니다.
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# 앱의 레이아웃을 설계합니다.
app.layout = html.Div([
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

# 앱을 실행합니다.
if __name__ == '__main__':
    app.run(debug=True)
