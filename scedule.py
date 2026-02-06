# from pandas import 
import pandas as pd

data = pd.read_excel('Book1.xlsx')

scedule_ = data.to_dict(orient='records')
print(scedule_)