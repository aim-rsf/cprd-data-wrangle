# Code snippet to generate a file containing SQL queries which creates the individual tables, loads in data from data csv files, and reads the data 
# Run as: python Step1C-Generate-SQL-queries.py path-to-files  metadata_version
# E.g. python Step1C-Generate-SQL-queries.py /proc-data/SYN_AURUM v2p9
# User gives the directory path which should contain two sub directories 'metadata_csv' and 'data_csv' created & populated from Step1A and Step1B respectively 

# Libraries
import os
import csv
import pandas as pd

# Inputs and directories 
data_input_path = sys.argv[1] + '/data_csv' #directory containing csv data files
metadata_input_path = sys.argv[1] + '/metadata_csv' #directory containing csv metadata files
output_path = sys.argv[1] + '/create-tables' 
metadata_version = sys.argv[2]

## ! don't change code below

#assignment
directory = os.fsencode(data_input_path)
list_csv= []

#loop over data files in directory    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".csv"): 
        #filename without csv extension
        name = filename.split('.')[0]
        print('name:', name)
        #read metadata to dataframe and replace datatypes to psql compatible format
        df = pd.read_csv(metadata_input_path + name + "-" + metadata_version + ".csv")
        df = df.replace('INTEGER','INT')
        # zip column field names and data types
        if 'Dictionary' in name:
         pairs = zip(df['Column name'],df['Type'])
         field_name =  df['Column name']
        else:
         pairs = zip(df['Field name'],df['Type'])
         field_name =  df['Field name']
        no_fields = len(df['Type'])
        #print('no_fields:', no_fields)
        
        # append complete SQL query to csv file
        list_csv.append( "DROP TABLE IF EXISTS " + name + ";\n" + \
        "CREATE TABLE " + name +  " ("+ \
        " ".join([p[1][0] + " " + p[1][1] + "," if p[0]+1 != no_fields else p[1][0] + " " + p[1][1] for p in enumerate(pairs) ]) + \
        "); \n"  + "COPY " + name + "(" + \
        " ".join(f[1] + "," if f[0]+1 != no_fields else f[1] for f in enumerate(field_name)) + \
        ") FROM '" + data_input_path + filename + "' WITH (FORMAT 'csv', DELIMITER ',', HEADER, QUOTE '\"'); \n" + \
        'SELECT * FROM ' + name + ' LIMIT 5; \n'         
      )

        print('done, next')
        continue
     else:
        print('No csv files found in directory specified.')
        continue

# write contents list_csv into a file (that can be run to create tables in sql)
with open(output_path + '/Step1C-create-tables.sql', 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = '\n', quoting = csv.QUOTE_NONE, escapechar = '\t')
    csvwriter.writerow(list_csv)
