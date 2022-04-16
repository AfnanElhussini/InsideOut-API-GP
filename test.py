from tensorflow.keras.models import load_model
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
data = pd.read_csv("emotions.csv")

new = load_model("model.h5")
y = data.pop('label')
X = data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=48)
X_train = np.array(X_train).reshape((X_train.shape[0],X_train.shape[1],1))
X_test = np.array(X_test).reshape((X_test.shape[0],X_test.shape[1],1))
y_train = pd.get_dummies(y_train)
y_test = pd.get_dummies(y_test)

def predict(list1):
    res=new.predict(list1)
    return res

print(predict(X_test))