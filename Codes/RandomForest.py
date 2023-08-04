import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import category_encoders as ce
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
class RandomForest():
    
    def __init__(self) -> None:
        pass


    def rndforest(self):
        path = input("Enter a path : ")
        df = pd.read_csv(path)
        print("DATASET")
        df.head()

        #Let's see the datas
        sns.lmplot(x='age', y='charges', data=df)

        X=df.drop(['charges'],axis=1)#Drop the charges column for Random Forest Classificiation model
        y=df['charges']

        
        X_train,X_test,y_train,y_test=(train_test_split(X,y,test_size=0.20,random_state=50))

        #Encoding the Dataset

        encoder=ce.OrdinalEncoder(cols=['sex','smoker','region'])
        X_train=encoder.fit_transform(X_train)
        X_test=encoder.fit_transform(X_test)
        X_train=X_train.astype(int)
        X_test=X_test.astype(int)
        y_train=y_train.astype(int)
        y_test=y_test.astype(int)

        #Train the model

        rnd_fr_clf=RandomForestClassifier(n_estimators=50,random_state=25)
        rnd_fr_clf=rnd_fr_clf.fit(X_train,y_train)

        y_pred=rnd_fr_clf.predict(X_test)

        #See the accuary rate 
        score = r2_score(y_test,y_pred)
        scorestr = str(score)
        print("Accuary Rate")
        print("%",scorestr[2:4])

        
        
        
        #age 19
        #famele
        #28bmi
        #0 childeren
        #someker
        #southwest 

        res1=rnd_fr_clf.predict([[19,1,28,0,1,2]])
        print("Estimated insurance cost = ",int(res1))

        