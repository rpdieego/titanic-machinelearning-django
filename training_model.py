# import relevant libraries

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Opening the Dataframes using Pandas

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Saving datasets indexes
train_idx = train.shape[0]
test_idx = test.shape[0]

# Saving PassengerID for Kaggle submission template
passengerId = test['PassengerId']

# Removing 'Survived' Column from train dataset before merging all the data
target = train.Survived.copy()
train.drop(['Survived'], axis=1, inplace=True)

# Merging both datasets

merged_df = pd.concat(objs=[train, test], axis=0).reset_index(drop=True)

# Dropping the features which we judged not to be relevant

merged_df.drop(['PassengerId','Name','Ticket','Cabin'], axis=1, inplace=True)

# Replacing "Age" missing values

median_age = merged_df['Age'].median()
merged_df['Age'].fillna(median_age, inplace=True)

# Replacing "Fare" missing values

median_fare = merged_df['Fare'].median()
merged_df['Fare'].fillna(median_fare, inplace=True)

# Replacing "Embarked" missing values

mostfreq_embarked = merged_df['Embarked'].value_counts()[:1]
merged_df['Embarked'].fillna(mostfreq_embarked, inplace=True)

# Preparing the 'Sex' variable:

merged_df['Sex'] = merged_df['Sex'].map({'male' : 0, 'female' : 1})


# Preparing the Dummie Variables for 'Embarked'

embarked_dummies = pd.get_dummies(merged_df['Embarked'], prefix='Embarked', drop_first=True)
merged_df = pd.concat([merged_df, embarked_dummies], axis=1)
merged_df.drop('Embarked', axis=1, inplace=True)

# Splitting the datasets using the indexes we saved

preprocessed_train = merged_df.iloc[:train_idx]
preprocessed_test = merged_df.iloc[train_idx:]

# Creating the Logistic Regression Model

lr_model = LogisticRegression(solver='liblinear')
lr_model.fit(preprocessed_train, target)

#Save Model
pickle.dump(lr_model, open('titanic_model.sav', 'wb'))