import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



class KNN():

    def __init__(self) -> None:
        pass

    def knn(self):
        path = input("Enter a path : ")
        df = pd.read_csv(path)


        print("Our Dataset")
        print(df.head())


        seker_hastalari = df[df.Outcome == 1]
        saglikli_insanlar = df[df.Outcome == 0]

        # For now, let's just look at gloucose and make an example drawing:
          # At the end of our program, our machine learning model will make a prediction based on all other data,
          #  not just glucose.
        plt.scatter(saglikli_insanlar.Age, saglikli_insanlar.Glucose, color="green", label="sağlıklı", alpha = 0.4)
        plt.scatter(seker_hastalari.Age, seker_hastalari.Glucose, color="red", label="diabet hastası", alpha = 0.4)
        plt.xlabel("Age")
        plt.ylabel("Glucose")
        plt.legend()
        plt.show()


        # Let's define the x and y axes

        y = df.Outcome.values
        x_ham_veri = df.drop(["Outcome"],axis=1)  

        # We remove the outcome column (dependent variable) and leave only independent variables
        # The KNN algorithm will group within x values.



        # we do normalization - we update all the values in x_ham_data so that they are only between 0 and 1
        # If we don't normalize in this way,
        #  the higher digits will overwhelm the lower digits and may confuse the KNN algorithm!

        x = (x_ham_veri - np.min(x_ham_veri))/(np.max(x_ham_veri)-np.min(x_ham_veri))


        # önce
        print("Raw data before normalization:\n")
        print(x_ham_veri.head())


        print("\n\n\nData we will give to AI for training after normalization:\n")
        print(x.head())


        # We separate our train data from our test data
        # Our train data will be used to learn how the system distinguishes between healthy and sick people
        # our test data is to see if our machine learning model can correctly distinguish between sick and healthy people 
        # It will be used to test   


        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1,random_state=1)

        # we are creating our knn model.
        knn = KNeighborsClassifier(n_neighbors = 3) # n_neighbors = k (we have a another algorithm called elbow method to find best k value)
        knn.fit(x_train,y_train)
        prediction = knn.predict(x_test)
        print("Accuracy rate  : ", knn.score(x_test, y_test))

         #Let's predict according to thoose values
        nmpar  = np.array([[2,87,58,26,16,28.4,0.766,22],
                   [0,122,72,1,1,36.3,0.258,52]])
        

        x_yeni_kisi_ham_veri = pd.DataFrame(nmpar, columns = x_ham_veri.columns)
        x_yeni_kisi_normalize_edilmis_veri = (x_yeni_kisi_ham_veri - np.min(x_ham_veri))/(np.max(x_ham_veri)-np.min(x_ham_veri))

        prediction_yeni_kisi = knn.predict(x_yeni_kisi_normalize_edilmis_veri)
        print(prediction_yeni_kisi)
        for i in prediction_yeni_kisi:
            if(i==1):
                print(i+1,".Person have diabate")
            else:
                print(i+1,".Person is healty")





