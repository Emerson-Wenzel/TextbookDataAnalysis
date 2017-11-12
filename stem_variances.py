"""

read_data.py
Written by: Mohsin Rizvi and Emerson Wenzel

Playground for getting data from CSVs

"""

import pandas as pd
import numpy as np
import plotly as pl
import plotly.plotly as py
import plotly.graph_objs as go

# Purpose:    Get a dataframe from the given CSV filenames, which has a row
#             for each unique class in the combined CSVs, where a class is
#             the concatenation of the department names in the 'Department'
#             CSV column and the value in the given class_col_in_csv column
#             in the CSVs.
# Parameters: A variable number of filenames and a class_col_in_csv, or
#             the name of the column to get a class number from in the CSV,
#             as well as a name for the new column in the returned DataFrame.
# Return:     A DataFrame of school classes (defined above) as rows with a
#             single column containing the amount of books for each class
#             in the combined CSVs.
def get_book_occurances(*filenames, class_col_in_csv, col_name):
    results = {}
    csvs = [pd.read_csv(i) for i in filenames]

    df_total = pd.concat(csvs, ignore_index = True)

    # Populate dictionary with dept and class number as key and amount
    # of books as values.
    for i in range(1, len(df_total['Department'])):

        # Skip over NaN and # (no department)
        if (df_total['Department'][i].upper() == 'NAN' or
            df_total['Department'][i].upper() == '#'):
            continue

        # Create key from dept and class number concatenation
        key = df_total['Department'][i] + str(df_total[class_col_in_csv][i])
        # Initialize/increment the value
        if key not in results:
            results[key] = 1
        else:
            results[key] += 1

    df = pd.DataFrame.from_dict(results, 'index')
    df.columns = [col_name]
    return df

# Get the total book occurances and sort
df = get_book_occurances('MASTER_SOLD.csv',
                         'MASTER_SELLING.csv',
                         class_col_in_csv = 'Class1',
                         col_name = 'Books')
df = df.sort_values(by = 'Books', ascending = False)
df.to_csv('cleaned_booknums.csv')