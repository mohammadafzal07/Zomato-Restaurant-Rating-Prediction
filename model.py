import numpy as pd
import pandas as pd
import sklearn
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('Zomato_df.csv')

df.drop('Unnamed: 0', axis=1, inplace=True)
#print(df.head())

X=df.drop('rate', axis=1)
y=df['rate']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=10)

#Preparing Extra Tree Regression
from sklearn.ensemble import ExtraTreesRegressor

et = ExtraTreesRegressor(n_estimators=120)
et.fit(X_train,y_train)

predict = et.predict(X_test)

import pickle
# Saving model to disk
pickle.dump(et, open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
print(predict)