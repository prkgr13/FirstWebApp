import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_excel('FinalList.xlsx')
d = data.fillna(0)
datatr = d.iloc[:,:12]
datatt = d.iloc[:,12:13]
trainx, testx, trainy, testy = train_test_split(datatr, datatt, test_size=0.3)
lg = LogisticRegression()
lg.fit(trainx, trainy)
model1 = lg.predict(testx)
#ex = (testy['Selected']!=model1).sum()/testy.shape[0]
#print('Performance : {}'.format(100*(1-ex)))

with open('Output.pkl','wb') as f:
    pickle.dump(model1, f)

