from DecisionTree import *
from Kmeans import *
from Knn import *
from LinearRegression import *
from LogisticRegression1 import *
from MultipleLinearRegression import *
from PolynomialRegression import *
from RandomForest import *
import os
import time










# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the home screen
def show_home_screen():
    clear_screen()
    print("╔════════════════════════╗")
    print("║     Home Screen      ║")
    print("╚════════════════════════╝")
    print("          Welcome!")
    print("")

# Function to handle user input
def handle_input():
    
    
    while True:
        command = input("Enter a command (help to see options): ")
        if command.lower() == "help":
            show_help()
        elif command.lower() == "exit":
            clear_screen()
            print("Goodbye!")
            break
        
        elif command =="1":
            print("Process Starting...")
            time.sleep(2)
            lin_regression=linearRegression()
            lin_regression.linear_regression()
        elif command =="2":
            print("Process Starting...")
            time.sleep(2)
            multi_lin_regression=MultipleLinearRegression()
            multi_lin_regression.multiple_linear_regression()
        elif command == "3":
            print("Process Starting...")
            time.sleep(2)
            poly_regression=PolynomialRegression()
            poly_regression.polynomialregression()
        elif command == "4":
            print("Process Starting...")
            time.sleep(2)
            log_regression=LogisticRegression1()
            log_regression.logisticregression()
            
        elif command =="5":
            print("Process Starting...")
            time.sleep(2)
            knearest = KNN()
            knearest.knn()
        elif command == "6":
            print("Process Starting...")
            time.sleep(2)
            kmeans=Kmeans()
            kmeans.kmeans()
        elif command =="7":
            print("Process Starting...")
            time.sleep(2)
            dec_tree = DecisionTree()
            dec_tree.decisiontree()
        elif command =="8":
            print("Process Starting...")
            time.sleep(2)
            rnd_forest = RandomForest()
            rnd_forest.rndforest()         
        else:
            print("Invalid command. Please try again.")

# Function to display the help menu
def show_help():
    clear_screen()
    print("╔══════════════════════════════════════╗")
    print("║                Help                ║")
    print("╚══════════════════════════════════════╝")
    print("Available commands:")
    print("help   - Display this help menu")
    print("exit   - Exit the program")
    print("Press 1 --->   Linear Regression")
    print("Press 2 --->   Multiple Linear Regression")
    print("Press 3 --->   Polynomial Regression")
    print("Press 4 --->   Logistic Regression")
    print("Press 5 --->   K Nearest Neighbor Model")
    print("Press 6 --->   K Means Clustering Model")
    print("Press 7 --->   Decision Tree Classification Model")
    print("Press 8 --->   Random Forest Classification Model")

  
    print("")


# Call the function to display the home screen
show_home_screen()

# Call the function to handle user input
handle_input()

