import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

import os
print(os.listdir("resources"))

import warnings
warnings.filterwarnings('ignore')

df_train = pd.read_csv("resources/train.csv")
df_test = pd.read_csv("resources/test.csv")
df = pd.concat([df_train, df_test])
df.sample(5)

df.info()

title_dict = {
    "Capt": "Officer",
    "Col": "Officer",
    "Major": "Officer",
    "Jonkheer": "Royalty",
    "Don": "Royalty",
    "Sir" : "Royalty",
    "Dr": "Officer",
    "Rev": "Officer",
    "the Countess":"Royalty",
    "Mme": "Mrs",
    "Mlle": "Miss",
    "Ms": "Mrs",
    "Mr" : "Mr",
    "Mrs" : "Mrs",
    "Miss" : "Miss",
    "Master" : "Master",
    "Lady" : "Royalty"
}

df['title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip()).map(title_dict)
df.head()