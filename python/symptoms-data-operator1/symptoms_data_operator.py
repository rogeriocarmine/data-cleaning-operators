# install dependencies
# pip install pandas
import pandas as pd
import numpy as np
 
def symptoms_validate(data_frame, column_to_transform):

    yes = ['SIM', 'YES', 'Y', 'X', 'SI']
    no = ['NAO', 'NO', 'N']
    
    data_frame[column_to_transform] = np.where(data_frame[column_to_transform].isin(yes), 1, data_frame[column_to_transform])
    data_frame[column_to_transform] = np.where(data_frame[column_to_transform].isin(no), 0, data_frame[column_to_transform])