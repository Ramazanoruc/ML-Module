import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model



class linearRegression():

    def __init__(self) -> None:
        pass



    def linear_regression(self):
        
        path = input("Enter a data path : ")
        df = pd.read_csv(path,sep=";")

        plt.xlabel('Alan')
        plt.ylabel('Fiyat')
        plt.scatter(df.alan, df.fiyat, color='red', marker='+')
        plt.show() #I show the data

        print(df.head())


        # linear regression model
        reg = linear_model.LinearRegression()
        reg.fit(df[['alan']], df['fiyat'])
        reg.predict([[275]])

        # I show the algorithm
        plt.xlabel('Alan', color='red')
        plt.ylabel('Fiyat', color='red')
        plt.title("Linear Regression", color='red')
        plt.scatter(df.alan, df.fiyat, color='red', marker='+')
        plt.plot(df.alan ,reg.predict(df[['alan']]), color = 'blue')
        plt.show()


        predict = int(input("Enter your predict : "))
        predict_result = reg.predict([[predict]])
        print("Your predict result is : ",int(predict_result))
        
        



        

        

    



