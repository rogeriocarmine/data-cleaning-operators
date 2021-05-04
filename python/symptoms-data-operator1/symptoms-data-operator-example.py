# install dependencies
# pip install pandas
import pandas as pd
import numpy as np
import symptoms-data-operator as sdo
 
complete_path = ''

path_to_read_csv = complete_path+'trudata-outbreak-data.csv'
path_to_save_csv = complete_path+'trudata-outbreak-data-fixed.csv'
 
df = pd.read_csv(path_to_read_csv)
 
sdo.symptoms_validate(df, 'symptoms-fever')
 
df.to_csv(path_to_save_csv)