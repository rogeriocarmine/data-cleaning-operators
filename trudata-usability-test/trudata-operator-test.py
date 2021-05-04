import pandas as pd

path_to_read_csv = "outbreak-dataset.csv"
 
df = pd.read_csv(path_to_read_csv)

# Check 200 lines and 11 columns
print(df.shape)

print("All set!")