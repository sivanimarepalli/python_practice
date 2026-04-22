# "A dataset contains columns like Gender (Male, Female) and City (New York, Paris, Tokyo).
# Task:
# Implement One-Hot Encoding and Label Encoding."
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv(r"E:\python_Practice\hands-on_pract(py)\DSA\preprocessing\dataset.csv")
print(data)
le=LabelEncoder()
data["Gender_label"]=le.fit_transform(data["Gender"])
print(data)
df_encode=pd.get_dummies(data,columns=["City"])
print(df_encode)
