# -*- coding: utf-8 -*-
"""DesicionTree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IJq4tDP88asCBdsZ6A1CrZQBLJTdVyid
"""

from google.colab import files
data_to_load=files.upload()



"""One of the most commonly used machine learning algorithm is the decision tree,it looks like a float chat.This structure leads to an outcome based on the data and the decision it takes.
Decision tree has following components
1.Root node: The root node is the one which represent the entire population this the point from where the population gets divided into two or more groups.
2.Internal node: An internal is agin like the root node but it does not contain the entire population we further divide our data into more groups from here.
3.Leaf node: A leaf node is the one which represent the final outcome.
"""

import pandas as pd
col_names=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
df=pd.read_csv("diabetes_data.csv",names=col_names).iloc[1:]
print(df.head())

features=['pregnant','insulin','bmi','age','glucose','bp','pedigree']
X=df[features]
y=df.label
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)
clf=DecisionTreeClassifier()
clf=clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("accuracy:",metrics.accuracy_score(y_test,y_pred))