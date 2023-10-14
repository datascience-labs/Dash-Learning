from dash import Dash, html, dash_table, dcc, Input, Output,callback
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/datascience-labs/Dash-Learning/main/electricity_usage.csv', encoding='utf-8')
print(df.info())
df.columns = df.columns.str.strip()
# 컬럼은 연도, 시도, 시군구, 계약종별, 1월, 2월, 3월, 4월이다.
app = Dash(__name__)
app.layout = html.Div([
    html.H1(children='시군구별 전력사용량 분석'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=15),

    html.H2(children='시도 선택하기'),
    dcc.Dropdown(df['시도'].unique().tolist(), id='dropdown1'),
    
    html.Div(id='chk_result'),

    html.H2(children='시군구 선택하기'),
    dcc.Dropdown(id='dropdown2'),
    
    html.H2(children='계약종별 선택'),
    dcc.RadioItems(df['계약종별'].unique().tolist(), id='radio'),
    
    html.H2(children='집계 월'),
    dcc.Checklist(df.columns[4:], id='chklist'),

    html.P(),

    html.Div(id='chk_result2'),

    html.P(),
    html.H2("선택한 정보에 대한 막대그래프"),
    dcc.Graph(id='graph')
    
])

@app.callback(
        Output('dropdown2', 'options'),
        Input('dropdown1', 'value')
)
def update_dropdown(value):
    dfs = df[df['시도']==value]
    return dfs['시군구'].unique().tolist()

@app.callback(
    Output('chk_result2', 'children'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('radio', 'value'),
    Input('chklist', 'value')
)
def update_div(drop1, drop2, radio, chklist):
    if drop1 and drop2 and radio and chklist:
        return f'선택한 내용은 {drop1} {drop2}이며, 선택한 계약 종류는 {radio}의 {chklist} 정보 입니다.'
    else:
        return f'지역, 시군구, 계약종별 및 집계 월을 선택해주세요.'

@app.callback(
    Output('graph', 'figure'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('radio', 'value'),
    Input('chklist', 'value'),
)
def update_graph(drop1, drop2, radio, chklist):
    if drop1 and drop2 and radio and chklist:
        filtered_df = df[(df['시도'] == drop1) & (df['시군구'] == drop2) & (df['계약종별'] == radio)] # 사용자가 선택한 시도, 시군구, 계약종별을 데이터에서 필터링함.

        # 현재 데이터는 1월, 2월 3월 4월이 각각의 컬럼으로 지정되어 집계월-사용량의 그래프를 그리는 것이 매우 어려움
        # 따라서 집계 월을 늘어트려 사용량과 매칭시킨다.
        df_melted = filtered_df.melt(id_vars=['연도', '시도', '시군구', '계약종별'], value_vars=chklist, 
                   var_name='월', value_name='사용량')
        
        # 사용량의 데이터는 쉼표가 포함되어 문자열로 인식함 따라서 정수형으로 변환
        df_melted['사용량'] = df_melted['사용량'].astype('int')

        # df_melted를 기준으로 x축은 월, y축은 사용량 체크리스트 순서와 상관없이 1월 ~ 4월 순서대로 막대가 생성되도록 지정
        fig = px.bar(df_melted, x='월', y='사용량', color='사용량', title=f'{drop1} {drop2}의 전력 사용량',  
                     category_orders={"월":  ['1월', '2월', '3월', '4월']})
        return fig
    else:
        return px.bar()
    
if __name__ == '__main__':
    app.run(debug=True)
