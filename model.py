from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import random
model = load_model("model.h5")
Emo_Signals=pd.read_csv("test_csv.csv")


def EmoPredictor(signals):
    predicted=np.array(list(map(lambda x: np.argmax(x), new_model.predict(signals))))
    if predicted == [0]:
        return "Sad"
    elif predicted == [1]:
        return "Natural"
    else:
        return "Happy"


def emopredict(data_test):
    y = data_test.pop('label')
    X = data_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9)
    X_train = np.array(X_train).reshape((X_train.shape[0],X_train.shape[1],1))
    X_test = np.array(X_test).reshape((X_test.shape[0],X_test.shape[1],1))
    y_train = pd.get_dummies(y_train)
    y_test = pd.get_dummies(y_test)
    
    predicted=np.array(list(map(lambda x: np.argmax(x), model.predict(X_test))))
    if predicted == [0]:
        return "\N{crying face}  Sad"
    elif predicted == [1]:
        return "\N{neutral face}  Natural"
    else:
        return "\N{grinning face with smiling eyes}  Happy"
def extract_signals(data):
    y = data.pop('label')
    X = data
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)
    X_train = np.array(X_train).reshape((X_train.shape[0],X_train.shape[1],1))
    X_test = np.array(X_test).reshape((X_test.shape[0],X_test.shape[1],1))
    y_train = pd.get_dummies(y_train)
    y_test = pd.get_dummies(y_test)
    return X_test
extracted_signals= extract_signals(Emo_Signals)    
def Get_Emo():
    predicted=np.array(list(map(lambda x: np.argmax(x), model.predict(extracted_signals))))
    predicted_emo=random.choice(predicted)
    Happy=["Feeling Happy, hope you have a great day too","Feelin Happy, hope you have the same ",
    "I am feeling happy.. Don't try to make me upset"]
    happy=random.choice(Happy)
    Sad=["Sorry, Feeling Sad, hope you can make me happy","Feeling Sad, why don't you make difference",
    "I am feeling sad..Think of what changes my mood"]
    sad=random.choice(Sad)
    Natural=["I am natural..Neither happy nor sad .. Don't mess me up","Natural, better to call!"]
    natural=random.choice(Natural)

    if predicted_emo == [0]:
        return "\N{crying face} ", sad
    elif predicted_emo == [1]:
        return "\N{smiling face with halo} ", natural
    else:
        return "\N{grinning face with smiling eyes} ", happy
#get_emo=Get_Emo()
#print(get_emo)

        
