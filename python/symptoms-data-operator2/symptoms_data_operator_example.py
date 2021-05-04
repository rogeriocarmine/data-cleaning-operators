import pandas as pd
import symptoms_data_operator as sdo

#Open the dirty dataset
df = pd.read_csv("outbreak_dataset.csv")

#Execute the data cleaning operator
#Symptoms
sdo.symptoms_transform(df, "symptoms-tiredness")

#Save the clean dataset 
df.to_csv("outbreak_dataset_fixed.csv", index=False)


