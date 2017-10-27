"""

clean-class-nums.py
Written by: Mohsin Rizvi

Asks for the name of a .csv file (including .csv) and parses its data
contained in the "Class Name" column. It saves the parsed data in a csv file
called "cleaned_[originalfile]", where [originalfile] is the name of the
original file. It puts the department name in the 2nd column, then the
class numbers in the following 6 columns.

This is a pretty rough script.

"""

import pandas as pd

file = input('What file would you like to open?\n')
df = pd.read_csv(file)

dpt_name = []
nums = []
class_nums = [list() for i in range(10)]

# Parse the data in the csv.
for i in df['Class Name']:
    # Split the data and add department name
    dpt = str(i).split()
    if len(dpt) != 0:
        nums = dpt[len(dpt) - 1].split('/')
        dpt_name.append(dpt[0].upper())
    else:
        dpt_name.append('#')

    # Add class number data
    for j in range(len(class_nums)):
        if len(nums) > j:
            class_nums[j].append(nums[j])
        else:
            class_nums[j].append('#')

# Put the data in a DataFrame and save in another csv.
df = pd.DataFrame(dpt_name)
for i in range(len(class_nums)):
    df[str(i)] = class_nums[i]
df.to_csv('cleaned_' + file)