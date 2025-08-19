import pandas as pd
import os
import json
from sklearn.model_selection import train_test_split

data = "data\\llm-classification-finetuning"

# getting file paths from the directory
file_paths = {"train.csv": "", "test.csv": ""}
for dirname, _, filenames in os.walk(data):
    for filename in filenames:
        fullpath = os.path.join(dirname, filename)
        # print(fullpath)
        if filename in file_paths:
            file_paths[filename] = fullpath

# reading data from file
df = pd.read_csv(file_paths['train.csv'])

# converting key columns into strings, joining all the items in the list & removing None in list
df["prompt"] = df["prompt"].apply(lambda x: ' '.join(json.loads(x)))
df["response_a"] = df["response_a"].apply(lambda x: ' '.join([i for i in json.loads(x) if i is not None]))
df["response_b"] = df["response_b"].apply(lambda x: ' '.join([i for i in json.loads(x) if i is not None]))

# create labels
label = []
for index, row in df.iterrows():
    if row["winner_model_a"] == 1:
        label.append(0)
    elif row["winner_model_b"] == 1:
        label.append(1)
    else:
        label.append(2) 

df["label"] = label

# Adding prompts to the responses columns
df["response_a"] = "Prompt: " + df["prompt"] + " Response: " + df["response_a"]
df["response_b"] = "Prompt: " + df["prompt"] + " Response: " + df["response_b"]

train_df, valid_df = train_test_split(df, test_size=0.2, stratify=df["label"])

print(df.head(1))