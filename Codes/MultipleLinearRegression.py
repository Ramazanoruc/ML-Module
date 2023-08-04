import pandas as pd
import matplotlib.pyplot as plt
# sklearn library
from sklearn import linear_model


class MultipleLinearRegression():

    def __init__(self) -> None:
        pass


    def multiple_linear_regression(self):
        path = input("Enter a path : ")
        df = pd.read_csv(path,sep = ";")


        print("***************OUR DATASET***************")
        print(df.head())



        #Let's Predict 
        reg = linear_model.LinearRegression()
        reg.fit(df[['alan', 'odasayisi', 'binayasi']], df['fiyat'])


        area = int(input("Enter area : "))
        room_number = int(input("Number of rooms : "))
        age_of_building = int(input("Age of building : "))

        predict_score = reg.predict([[area,room_number,age_of_building]])

        print("Your predict price  is : ",int(predict_score))


