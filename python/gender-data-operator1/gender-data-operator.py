# install dependencies
# pip install pandas
import pandas as pd
import numpy as np
 
def gender_transform(data_frame, column_to_transform):
    male_synonym = ['M', 'Masculino', 'Masc', 'Homem', 'Man', 'Male', 'M.', 'Masc.']
    female_synonym = ['F', 'Feminino', 'Fem', 'Mulher', 'Woman', 'Female', 'Fem.', 'Wom.', 'Femenino']
    data_frame[column_to_transform] = np.where(data_frame[column_to_transform].isin(male_synonym), 'M', data_frame[column_to_transform])
    data_frame[column_to_transform] = np.where(data_frame[column_to_transform].isin(female_synonym), 'F', data_frame[column_to_transform])