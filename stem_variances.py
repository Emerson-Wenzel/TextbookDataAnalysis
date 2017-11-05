"""

read_data.py
Written by: Mohsin Rizvi and Emerson Wenzel

Playground for getting data from CSVs

"""

import pandas as pd
import numpy as np
import plotly as pl
pl.tools.set_credentials_file(username = 'mohsr',
                              api_key  = '7b5tLyUkpqohy7B2L4IK')
import plotly.plotly as py
import plotly.graph_objs as go

results = {}
df_total = pd.concat([pd.read_csv('MASTER_SOLD.csv'),
                      pd.read_csv('MASTER_SELLING.csv')],
                      ignore_index = True)

# Populate dictionary with dept and class number as key and amount of books
# as values.
for i in range(1, len(df_total['Department'])):
    # Skip over NaN and # (no department)
    # if (df_total['Department'][i].upper() == 'NAN' or
    #     df_total['Department'][i].upper() == '#'):
    #     continue
    # Create key from dept and class number concatenation
    key = df_total['Department'][i] + str(df_total['Class1'][i])
    # Increment the value
    if key not in results:
        results[key] = 1
    else:
        results[key] += 1

# Dump dictionary to DataFrame and sort
df_books = pd.DataFrame.from_dict(results, 'index')
df_books = df_books.sort(ascending = False, inplace = True)
print(df_books)