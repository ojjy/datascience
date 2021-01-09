import time
import os
import pandas as pd
import re


# load train dataset
train = pd.read_csv('datasets/titanic/train.csv')
print("train: ", train)

# load test dataset
test = pd.read_csv('datasets/titanic/test.csv')
print("test", test)

print(train.head(5))
print(test.head(5))

print(train.shape)
print(test.shape)

print(train.info())

print(train.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

train_test_data = [train, test]
for titanic_df in train_test_data:
    titanic_df['Title'] = titanic_df['Name'].str.extract('([A-Za-z]+)\.',expand=False)

train['Title'].value_counts()
test['Title'].value_counts()

title_mapping = {"Mr":0, "Miss":1, "Ms":1, "Mrs":2,
                 "Master":3,"Dr":3,"Rev":3,"Major":3,"Col":3,
                 "Mlle":3,"Sir":3,"Jonkheer":3,"Capt":3,"Mme":3,
                 "Lady":3,"Countess":3,"Don":3, "Dona":3}
for titanic_df in train_test_data:
    titanic_df['Title'] = titanic_df['Title'].map(title_mapping)


gender_mapping = {"male":0, "female":1}
for titanic_df in train_test_data:
    titanic_df['Sex']=titanic_df['Sex'].map(gender_mapping)

train["Age"].fillna(train.groupby("Title")["Age"].transform("median"), inplace=True)
test["Age"].fillna(test.groupby("Title")["Age"].transform("median"), inplace=True)



train.head()

train["Age"].fillna(train.groupby("Title")["Age"].transform("median"), inplace=True)
test["Age"].fillna(test.groupby("Title")["Age"].transform("median"), inplace=True)
train.groupby("Title")["Age"].transform("median")

facet = sns.FacetGrid(train, hue="Survived", aspect=4)
facet.map(sns.kdeplot, "Age", shade=True)
facet.set(xlim=(0, train["Age"].max()))
facet.add_legend()

plt.show()


for titanic_df in train_test_data:
    titanic_df.loc[ titanic_df['Age'] <= 16, 'Age'] = 0,
    titanic_df.loc[(titanic_df['Age'] > 16) & (titanic_df['Age'] <= 26), 'Age'] = 1,
    titanic_df.loc[(titanic_df['Age'] > 26) & (titanic_df['Age'] <= 36), 'Age'] = 2,
    titanic_df.loc[(titanic_df['Age'] > 36) & (titanic_df['Age'] <= 62), 'Age'] = 3,
    titanic_df.loc[ titanic_df['Age'] > 62, 'Age'] = 4