import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
#import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def Calc(radius_mean,texture_mean,smoothness_mean,compactness_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,smoothness_se,compactness_se,symmetry_se,fractal_dimension_se):
    df = pd.read_csv('dataset/breast_cancer.csv')
    ans=0
    df.drop('id',axis=1,inplace=True)
    df.drop('Unnamed: 32',axis=1,inplace=True)
    df['diagnosis']=df['diagnosis'].map({'B':0,'M':1})
    df.drop(['concavity_mean',	'concave points_mean','radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst','concave points_worst','symmetry_worst','fractal_dimension_worst','concavity_se','concave points_se','perimeter_se','area_se','perimeter_mean',	'area_mean'], axis = 1,inplace=True)
    from sklearn.model_selection import train_test_split
    x = df.drop(['diagnosis'],axis=1)
    y = df['diagnosis']
    mean = x.mean()
    sd = x.std()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=40)
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    x_train = sc_x.fit_transform(x_train) 
    x_test = sc_x.transform(x_test)
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(x_train, y_train)
    inputs = [radius_mean,texture_mean,smoothness_mean,compactness_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,smoothness_se,compactness_se,symmetry_se,fractal_dimension_se]
    for i in range(len(inputs)):
        inputs[i] = (inputs[i]-mean[i])/sd[i]
    ans = classifier.predict([inputs])

    cols=['radius_mean','texture_mean','smoothness_mean','compactness_mean','symmetry_mean','fractal_dimension_mean','radius_se','texture_se','smoothness_se','compactness_se','symmetry_se','fractal_dimension_se']
    for i in range(len(cols)):
        a=df[cols[i]]
        b=df['diagnosis']
        plt.scatter(b,a)
        plt.plot(ans[0],(inputs[i]*sd[i])+mean[i],'r*')
        plt.ylabel(cols[i])
        plt.xlabel('Diagnosis')
        plt.savefig('static/'+str(i)+'.png')
        plt.close()
    if ans[0]==1:
        return "Malignant"
    else:
        return "Benign"











