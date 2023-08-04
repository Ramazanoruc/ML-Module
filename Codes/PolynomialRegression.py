import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures



class PolynomialRegression():

    def __init__(self) -> None:
        pass



    def polynomialregression(self):
        path = input("Enter a path : ")
        df = pd.read_csv(path,sep=";")


        print("***************OUR DATASET***************")
        print(df.head())

        plt.scatter(df['deneyim'],df['maas'])
        plt.xlabel('Deneyim (yıl)')
        plt.ylabel('Maaş')
        
        plt.show()

        reg = LinearRegression()
        reg.fit(df[['deneyim']],df['maas'])

        plt.xlabel('Deneyim (yıl)')
        plt.ylabel('Maaş')

        plt.scatter(df['deneyim'],df['maas'])   

        xekseni = df['deneyim']
        yekseni = reg.predict(df[['deneyim']])
        plt.plot(xekseni, yekseni,color= "green", label = "what if we used linear regression")
        plt.legend()
        plt.show()

        polynomial_regression = PolynomialFeatures(degree = 4) #n is changable 

        x_polynomial = polynomial_regression.fit_transform(df[['deneyim']])

        reg = LinearRegression()
        reg.fit(x_polynomial,df['maas'])

        y_head = reg.predict(x_polynomial)
        plt.plot(df['deneyim'],y_head,color= "red",label = "polynomial regression")
        
        plt.legend()

        
        plt.scatter(df['deneyim'],df['maas'])   
        

        plt.show()


        predict = int(input("Enter a years of experience : "))
        x_polynomial1 = polynomial_regression.fit_transform([[predict]])
        predict_score = reg.predict(x_polynomial1)
        print("Your Salary predict is : ",int(predict_score))



