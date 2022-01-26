import csv
import pandas as pd
import plotly.express as px
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
df=pd.read_csv("data_part2.csv")
gre_score=df["GRE Score"].tolist()
chance_of_admit=df["Chance"].tolist()
#equation of the line y=mx+c
m=0.95
c=-93
y=[]
for x in gre_score:
    y_value=m*x+c
    y.append(float (y_value))
fig=px.scatter(df,x=gre_score,y=chance_of_admit)
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=min(y),y1=max(y),
        x0=min(gre_score),x1=max(gre_score)
    )
])
fig.show()

