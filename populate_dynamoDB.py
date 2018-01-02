'''
populate_dynamoDB.py

12/30/2017
Emerson Wenzel

Purpose: Populate dynamoDB with csv data
'''


import pandas as pd
import boto3
import sys
from decimal import Decimal


def main(argv):

    if (len(argv) != 3):
        print("Improper use. Usage as follows:\npython populate_dynamoDB.py [csv name] [table name]")
        exit()

    csv_file = argv[1]
    table_name = argv[2]

    # Pull csv file into dataframe
    df = pd.read_csv(csv_file) 

    #Make sure price can be represented as numeric
    df['Price'] = df['Price'].str.strip('$')



    dynamodb = boto3.resource('dynamodb')

    # Choose the table used
    table = dynamodb.Table(table_name)


    #Obtain keys to use later when checking blank spaces
    keys = list(df.ix[0].to_dict().keys())

    for i in list(range(len(df['Dept_1']))):
        if df.ix[i]['ID'] == 0 or pd.isnull(curr_book[key]):
            print("Book does not have a valid ID. Will continue to process other books")
            continue

        curr_book = df.ix[i].to_dict()
        clean_curr_book = {}

        #Make a dictionary from the row with no blank values and ensure all numbers are represented as numerics
        for key in keys:
            if curr_book[key] != '#' and not pd.isnull(curr_book[key]):
                if is_number(curr_book[key]):
                    curr_book[key] = float(curr_book[key])
                    if curr_book[key].is_integer():
                        clean_curr_book[key] = int(curr_book[key])
                    else:
                        clean_curr_book[key] = Decimal(repr(curr_book[key]))           
                elif isinstance(curr_book[key], int):
                        clean_curr_book[key] = curr_book[key].item()
                else:
                    clean_curr_book[key] = curr_book[key]
            
        #Print book for error checking. Can comment this line out
        print(clean_curr_book)
    
        #Insert book into table
        table.put_item(Item=clean_curr_book)


    print("done!")

#Function to help understand what csv values are numerics
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

    
if __name__ == "__main__":
    main(sys.argv)
