from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import warnings
from sklearn.exceptions import DataConversionWarning,ConvergenceWarning


from sklearn.preprocessing import KBinsDiscretizer
import numpy as np



def fun(y,col_name):
  data = y


  k_bins = 5
  discretizer = KBinsDiscretizer(n_bins=k_bins, encode='ordinal', strategy='uniform')

  discretized_data = discretizer.fit_transform(data)

  y[col_name] = discretized_data
  return y

def lr(X,y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=23)
  logistic = linear_model.LogisticRegression(max_iter=100, C=1, tol=0.0001, fit_intercept=True, dual=False, penalty='l2')
  score = round(logistic.fit(X_train, y_train).score(X_test, y_test),3)
  print(score)


print("------------------SS-A.csv---------------")
df1 = pd.read_csv("SS-A.csv")
df1.head(2)

X = df1[['Spout_wait', 'Spliters', 'Counters']]
y = df1[['Throughput+']]

y = fun(y,"Throughput+")

lr(X,y)

X.to_csv("SS-A_X.csv",index=False)
y.to_csv("SS-A_y.csv",index=False)

print("--------------SS-B.csv------------------")

df1 = pd.read_csv("SS-B.csv")
df1.head(2)

X = df1[['A', 'B', 'C']]
y = df1[['A-']]

y = fun(y,"A-")

lr(X,y)

X.to_csv("SS-B_X.csv",index=False)
y.to_csv("SS-B_y.csv",index=False)

print("---------------------------------")
df1 = pd.read_csv("SS-C.csv")
df1.head(2)

X = df1[['Spout_wait', 'Spliters', 'Counters']]
y = df1[['Throughput+']]

y = fun(y,"Throughput+")

lr(X,y)

X.to_csv("SS-C_X.csv",index=False)
y.to_csv("SS-C_y.csv",index=False)

print("---------------dtlz2.csv------------------")

df1 = pd.read_csv("dtlz2.csv")
df1.columns

X = df1[['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9']]
y = df1[['Y0-']]

y = fun(y,'Y0-')

lr(X,y)

X.to_csv("dtlz2_X.csv",index=False)
y.to_csv("dtlz2_y.csv",index=False)

print("----------------dtlz3.csv-----------------")
df1 = pd.read_csv("dtlz3.csv")
df1.columns

X = df1[['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9']]
y = df1[['Y0-']]

y = fun(y,'Y0-')

lr(X,y)

X.to_csv("dtlz3_X.csv",index=False)
y.to_csv("dtlz3_y.csv",index=False)

print("-----------------pom3a.csv----------------")
df1 = pd.read_csv("pom3a.csv")
df1.columns

X = df1[['Culture', 'Criticality', 'Criticality Modifier', 'Initial Known',
       'Inter-Dependency', 'Dynamism', 'Size', 'Plan', 'Team Size']]
y = df1[['Cost-']]

y = fun(y,'Cost-')

lr(X,y)

X.to_csv("pom3a_X.csv",index=False)
y.to_csv("pom3a_y.csv",index=False)
print("----------------pom3b.csv-----------------")
df1 = pd.read_csv("pom3b.csv")
df1.columns

X = df1[['Culture', 'Criticality', 'Criticality Modifier', 'Initial Known',
       'Inter-Dependency', 'Dynamism', 'Size', 'Plan', 'Team Size']]
y = df1[['Score-']]

y = fun(y,'Score-')

lr(X,y)

X.to_csv("pom3b_X.csv",index=False)
y.to_csv("pom3b_y.csv",index=False)

print("---------------pom3c.csv------------------")

df1 = pd.read_csv("pom3c.csv")
df1.columns

X = df1[['Culture', 'Criticality', 'Criticality Modifier', 'Initial Known',
       'Inter-Dependency', 'Dynamism', 'Size', 'Plan', 'Team Size']]
y = df1[['Cost-']]

y = fun(y,'Cost-')

lr(X,y)

X.to_csv("pom3c_X.csv",index=False)
y.to_csv("pom3c_y.csv",index=False)

print("----------------SS-D.csv-----------------")
df1 = pd.read_csv("SS-D.csv")
df1.columns

X = df1[['Max_spout', 'Spliters', 'Counters']]
y = df1[['Throughput+']]

y = fun(y,'Throughput+')

lr(X,y)

X.to_csv("SS-D_X.csv",index=False)
y.to_csv("SS-D_y.csv",index=False)

print("-----------------Wine_quality.csv----------------")
df1 = pd.read_csv("Wine_quality.csv")
df1.columns

X = df1[['Fixedacidity', 'Volatileacidity', 'Citricacid', 'Residualsugar', 'CL',
       'FreeSO2', 'TotalS02', 'Density', 'PH', 'Sulphates']]
y = df1[['Quality+']]

y = fun(y,'Quality+')

lr(X,y)

X.to_csv("Wine_quality_X.csv",index=False)
y.to_csv("Wine_quality_y.csv",index=False)