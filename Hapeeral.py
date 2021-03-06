

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/My Drive

patients=pd.read_csv('indian_liver_patient.csv')

patients.head()

patients.shape

"""Dataframe is imported."""

patients['Gender']=patients['Gender'].apply(lambda x:1 if x=='Male' else 0)
patients.isnull().sum()

patients['Albumin_and_Globulin_Ratio'].mean()

patients=patients.fillna(0.94)
patients.isnull().sum()

"""Building the Model."""

from sklearn.model_selection import train_test_split

X=patients[['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin',
       'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
       'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin',
       'Albumin_and_Globulin_Ratio']]
y=patients['Dataset']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=123)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

#print(X_test)
y_pred = logmodel.predict(X_test)
y_pr = logmodel.predict_proba(X_test)
#print(y_pred)
#print(y_pr)
#df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred,})
#df
#logmodel.score

INPUT = [[65,0,0.7,0.1,187,16,18,6.8,3.3,0.9]]

print(INPUT)
y_pr = logmodel.predict(INPUT)
y_prb = logmodel.predict_proba(INPUT)
print(y_pr)
print(y_prb)

print("the probability of you being affected is : "+str(y_prb[0][0]*100)+" %")

from sklearn.model_selection import KFold, cross_val_score
kfold = KFold(n_splits=5,random_state=42)

results = cross_val_score(logmodel, X_train,y_train,cv = kfold)
print(results)
print("Accuracy of this ML model is :",results.mean()*100)

corr=patients.corr()
plt.figure(figsize=(20,10)) 
sns.heatmap(corr,cmap="Greens",annot=True)

sns.set_style('darkgrid')
plt.figure(figsize=(25,10))
patients['Age'].value_counts().plot.bar(color='darkviolet')
