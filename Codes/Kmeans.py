import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans


class Kmeans():
    def __init__(self) -> None:
        pass


    def kmeans(self):
        path = input("Enter a path : ")
        df = pd.read_csv(path)

        plt.scatter(df.Yas,df['Gelir'])
        plt.xlabel('Yaş')
        plt.ylabel('Gelir')
        plt.show()

        """Before training my model, I need to do Normalization,
        Normalization = Eliminating data duplication in the database and increasing data consistency (accuracy),
        I have done the normalization process manually before,
        this time using the MinMaxScaler library."""

        scaler=MinMaxScaler()

        scaler.fit(df[['Gelir']])
        df['Gelir']=scaler.transform(df[['Gelir']])
        scaler.fit(df[['Yas']])
        df['Yas']=scaler.transform(df[['Yas']])

        #df.head()
        ##As you can see I pulled the data between 0-1, so my model will be better trained



        plt.scatter(df.Yas,df['Gelir'])
        plt.xlabel('Yaş')
        plt.ylabel('Gelir')
        plt.show()

        #I am creating a model for #K=3
        k_means_modelim=KMeans(n_clusters=3)
        y_preticted=k_means_modelim.fit_predict(df[['Yas','Gelir']])
        print(y_preticted)#We'll See Groups

        df['Grubu']=y_preticted
        df.head()

        #let's draw
        df1=df[df.Grubu==0]
        df2=df[df.Grubu==1]
        df3=df[df.Grubu==2]
        plt.xlabel('Yaş')
        plt.ylabel('Gelir')
        plt.scatter(df1.Yas,df1['Gelir'],color='green')
        plt.scatter(df2.Yas,df2['Gelir'],color='red')
        plt.scatter(df3.Yas,df3['Gelir'],color='black')
        

        
        plt.scatter(k_means_modelim.cluster_centers_[:,0],k_means_modelim.cluster_centers_[:,1],
                color='blue',marker='X',label='Ağırlık Merkezleri')
        plt.legend()
        plt.show()



        #To view who is in which group
        df.sort_values('Grubu')[['Ad','Grubu']]

        
        



