import numpy as np
import pandas as pd
import os 
import time


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


directory = os.getcwd()
# Unzipped data is put in the following path
data_path = directory + '\\Voice\\data\\unzipped\\train'

# Create a file with file description and labels (gender and accent)
df = pd.DataFrame()
subdirs = get_immediate_subdirectories(data_path)
for subdir in subdirs:
    filenames = os.listdir(data_path + "\\" + subdir)
    gender = subdir.split("_")[0]
    accent = subdir.split("_")[1]
    df1 = pd.DataFrame({
            'Filename' : filenames,
            'Foldername' : subdir,
            'Gender' : gender,
            'Accent' : accent

        })
    print(df1.head())
    df = df.append(df1, ignore_index=True)
    

print(df)
df.to_csv("description.csv")
    

