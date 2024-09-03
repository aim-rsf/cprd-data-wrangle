# Code snippet to generate the pre-processed csv files
# Run as: python Step1B-Generate-data-csv.py path-to-text-files
# User gives the directory path which contains (only) the cprd txt files to process
# The csv files are outputted into a new 'data_csv' sub-directory and used for Step1C
# (Example) list_of_filenames = ['Common_Dosages','ConsSource','Consultation','DrugIssue','EMISCodeCat','Gender','JobCat','MedicalDictionary','NumUnit','Observation','ObsType','OrgType','ParentProbRel','Patient','PatientType','Practice','Problem','ProbStatus','ProductDictionary','QuantUnit','Referral','RefMode','RefServiceType','RefUrgency','Region','Sign','Staff']

## Libraries
import os
import sys
import datetime
import csv
import numpy as np

## Inputs and directories 
path_from = sys.argv[1]
path_to = path_from + '/data_csv'

## ! don't change code below

list_of_filenames_ext = os.listdir(path_from)
list_of_filenames=[x.split('.')[0] for x in list_of_filenames_ext] # this assume no period (.) in the filename

# create 'path_to'
if os.path.isdir(path_to):
   print('There is already a csv directory. Exiting!')
   exit()
else:
   os.mkdir(path_to)

# loop over txt files
for name in list_of_filenames:
    print('reading:',name)
    # read file into variable r
    r = csv.reader(open(path_from + '/' + name + '.txt', 'r', encoding='latin1'), delimiter='	',quotechar='"')
    
    #list to store data in and appending values
    data=[]
    for row in r: 
        #print(row)
        data.append(row)
      
    #separating header of file to extract fields == 'lcd' OR that contain 'date' as substring (can tweak later to avoid hardcoding)      
    header = data[0]
    print('header:',header)
    date_fields = [idx for idx, x in enumerate(header) if ('date' in x) or (x == 'lcd')]         
    
    #looping over all rows i and cols j of list
    for i, row in enumerate(data): # loop rows
        for j, col in enumerate(row): # loop cols in rows
            #print('row:',i,'col:',j,col)
            
            #condition to filter datetime fields and reformat from dd/mm/yyyy to datetime format (YYYY-MM-DDT00:00:00.000)
            if (len(col)>6) & (j in date_fields) & (i != 0):
                data[i][j] = datetime.datetime.strptime(col, "%d/%m/%Y").strftime("%Y-%m-%d")
                #print('new col:',j,data[i][j])
                
    # open/create the file to write comma separated values to
    with open(path_to + '/' + name + '.csv', 'w') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter=',')
        for rows in data:
            csv_writer.writerow(rows)
        
        print('Exported file',name,'.csv to location:', path_to)
