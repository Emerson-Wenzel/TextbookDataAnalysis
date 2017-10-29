'''
Displays the number of books sold via department


'''

#Import packages. 
import pandas as pd
import numpy as np
import plotly
plotly.tools.set_credentials_file(username='Emerson_Wenzel', api_key='ObbSRdzYMhc7LuMb4JaK')

import plotly.plotly as py
import plotly.graph_objs as go

#Read csv into dataframe
df = pd.read_csv("MASTER_SOLD.csv")

#Create our x values, the departments w/o duplicates
uniqueNames = list(set(df['Department']))
zeroArray = np.zeros([len(uniqueNames), 1])[:,0]

#Create the new dataframe which we will use to plot
Occurence_df = pd.DataFrame(
        {'Department':uniqueNames,
         'Occurence':zeroArray
                })
    
#Find how often each department is listed
for i, dept in enumerate(df['Department']):
    for j, unique_dept in enumerate(Occurence_df['Department']):
        if dept == unique_dept:
            Occurence_df['Occurence'][j] += 1
            

#Sort the values via the number of occurences descending
sorted_Occurence_df = Occurence_df.sort_values(by=['Occurence'], ascending=False)

#Create Bar Graph
data = [go.Bar(
            x=sorted_Occurence_df['Department'],
            y=sorted_Occurence_df['Occurence']
    )]

#Put bar graph onto plotly
py.plot(data, filename='Popularity of Department books sold')
