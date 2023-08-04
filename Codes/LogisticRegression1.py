
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


class LogisticRegression1():

    def __init__(self) -> None:
        pass


    def logisticregression(self):
        path = input("Enter a path : ")
        df = pd.read_csv(path, sep = ";")


        print("OUR DATASET")
        print(df.head)

        #Draw
        plt.xlabel('Yaş')
        plt.ylabel('Sigorta (yok:0 / var:1)')
        plt.scatter(df.yas, df.sigorta, color='red', marker='+')
        plt.show()

        # We create our train and test data using our main dataset.
        # We want our data to be set to be 80% train and 20% test:
        X_train, X_test, y_train, y_test = train_test_split(df[['yas']], df.sigorta, train_size=0.8)

        ### We create our model object and then start training it


        model = LogisticRegression()

        model.fit(X_train, y_train)


        y_predicted = model.predict(X_test)



        # our model also gives us the probability result it calculates for each test data as a 2-dimensional array.
        # probability for the first result 0
        # probability for the second result 1

        print(model.predict_proba(X_test))

        #Let'S predict 
        #0 hayır
        #1 evet
        list = []
        age1 = int(input("Enter age : "))
        age2 = int(input("Enter age : "))
        list.append([age1])
        list.append([age2])
        print(list)


        predict = model.predict(list)
        print(predict)
        
        sayac = 1

        for i in predict:
            if(i==1):
                print(sayac,".Person have a Insurance (his age = {} )".format(list[1]))
                sayac+=1
            else:
                print(sayac,".Person will have no insurance (his age = {} )".format(list[0]))
                sayac+=1

        





        

