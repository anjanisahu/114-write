import csv
import plotly.express as pe
import pandas as pd
df=pd.read_csv("data_part2.csv")
gre_score=df["GRE Score"].tolist()
chanse=df["Chance"].tolist()
fig=pe.scatter(x=gre_score,y=chanse)
fig.show()