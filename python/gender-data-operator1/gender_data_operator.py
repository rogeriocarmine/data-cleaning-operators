# install dependencies
# pip install pandas
import pandas as pd
import numpy as np
 
def gender_transform(data_frame, column_to_transform):
    male_synonym = ['M', 'Masculino', 'Masc', 'Homem', 'Man', 'Male', 'M.', 'Masc.']
    female_synonym = ['F', 'Feminino', 'Fem', 'Mulher', 'Woman', 'Female', 'Fem.', 'Wom.', 'Femenino']
    data_frame[column_to_transform] = np.where(df[column_to_transform].isin(male_synonym), 'M', df[column_to_transform])
    data_frame[column_to_transform] = np.where(df[column_to_transform].isin(female_synonym), 'F', df[column_to_transform])
 
complete_path = '/Users/...'

path_to_read_csv = complete_path+'trudata-outbreak-data.csv'
path_to_save_csv = complete_path+'trudata-outbreak-data-fixed.csv'
 
df = pd.read_csv(path_to_read_csv)
 
gender_transform(df, 'gender')
 
df.to_csv(path_to_save_csv)