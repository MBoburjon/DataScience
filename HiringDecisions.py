import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import os 
from IPython.display import Image  
from sklearn.externals.six import StringIO  
import pydotplus

# here you can put your sample data file
# inputFile = "... .csv"

df = pd.read_csv(inputFile, header = 0)


#tranforming data into numerical values as 0 for no and 1 for yes
d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)

#mapping datas as 0, 1, 2 corresponding to BS, MS and PhD
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)

#separate features from the target columns
features = list(df.columns[:6])

#now we actually construct the decision tree
y = df["Hired"]
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X,y) 

# Predict employment of an employed 10-year veteran
print (clf.predict([[10, 1, 4, 0, 0, 0]]))
# ...and an unemployed 10-year veteran
print (clf.predict([[10, 0, 4, 0, 0, 0]]))







