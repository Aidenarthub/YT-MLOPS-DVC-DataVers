import pandas as pd
import os

# create a sample DataFrame with column names
data={"Name":['Alice','Bob','Charlie'],
      'age':[25,30,35],
      'City':['New York','Los Angeles','Chicago']}

df=pd.DataFrame(data)

# Adding new row to df for v2
new_row_loc={'Name':'Gf2','Age':20,'City':'city1'}
df.loc[len(df.index)]=new_row_loc

# Adding new row to df for v3
# new_row_loc2={'Name':'v3','Age':30,'City':'city1'}
# df.loc[len(df.index)]=new_row_loc2

# Ensure the "data" directory exists at the root level
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#Define the file path
file_path=os.path.join(data_dir,'sample_data.csv')

#save the DataFrame to a csv file, includingcolumn names
df.to_csv(file_path,index=False)

print(f'csv file saved to {file_path}')