import numpy as np
import pandas as pd
from sklearn import tree


class DecisionTree():
    def __init__(self) -> None:
        pass




    def decisiontree(self):
        path = input("Enter a path : ")
        df = pd.read_csv(path)

        print("*********DATASET*********")
        df.head()

        #The scikit-learn library expects everything to be numeric for decision trees to work properly,
        #so we fix all Y and N values in our dataset to 0 and 1. 
        #For the same reason we update the education level to BS:0 MS:1 and PhD:2. Using map() empty cells or cells with invalid values will be filled with NaN,
        #we don't need this in our current dataset but you will need it in the future when you work with data intensive data.


        duzetme_mapping = {'Y': 1, 'N': 0}

        df['IseAlindi'] = df['IseAlindi'].map(duzetme_mapping)
        df['SuanCalisiyor?'] = df['SuanCalisiyor?'].map(duzetme_mapping)
        df['Top10 Universite?'] = df['Top10 Universite?'].map(duzetme_mapping)
        df['StajBizdeYaptimi?'] = df['StajBizdeYaptimi?'].map(duzetme_mapping)
        duzetme_mapping_egitim = {'BS': 0, 'MS': 1, 'PhD': 2}
        df['Egitim Seviyesi'] = df['Egitim Seviyesi'].map(duzetme_mapping_egitim)
        df.head()

        #We separate the result column:
        
        y = df['IseAlindi']
        X = df.drop(['IseAlindi'], axis=1)

        #We create our Decision Tree:


        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X,y)


        ## Let's make a prediction now
        # 5 years of experience, currently working somewhere and worked in 3 former companies, education level Bachelor's degree
        # not a graduate of top-tier-school


        res1= (clf.predict([[5, 1, 3, 0, 0, 0]]))


        ## Total 2 years of work experience, changed jobs 7 times, not a very good school graduate, currently working

        res2= (clf.predict([[2, 1, 7, 0, 0, 0]]))

       # Total 20 years of work experience, changed jobs 5 times, graduated from a good school, currently not working
        res3 =  (clf.predict([[20, 0, 5, 1, 1, 1]]))
        list =[]
        list.append(int(res1))
        list.append(int(res2))
        list.append(int(res3))
        print(list)
        sayac=1

        for i in list:
            if (i == 1):
                print(sayac,".Person Got the job!")
                sayac+=1
            else:
                print(sayac,".Person does not got the job!")
                sayac+=1
                
