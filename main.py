# Python source code for property prediction rates.

# To prevent all warnings
import warnings
warnings.filterwarnings('ignore')

# Importing joblib to export the machine learning model
import joblib

# Importing Libraries
import os                           # Built - IN Modules
import sys                          # Built - IN Modules
import time                         # Built - IN Modules
from datetime import datetime       # Built - IN Modules

try:
    import numpy as np
except:
    print("NUMPY is not installed\nINSTALLING NUMPY!!")
    os.system("pip3 install numpy")
    import numpy as np

try:
    import pandas as pd # plotting
except:
    print("pandas is not installed\nINSTALLING PANDAS!!")
    os.system("pip3 install pandas")
    import pandas as pd

# Scikit-learn modules
try:
    from sklearn.model_selection import train_test_split
except:
    print("Scikit-learn in not installed.\nINSTALLING Scikit-learn!!")
    os.system("pip3 install scikit-learn")
    print("Scikit-learn INSTALLED!!")
    from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeRegressor

# Importing our concole desingner RICH
try:
    from rich.console import Console
    from rich.markdown import Markdown
except:
    print("Installing Rich module....")
    os.system("pip3 install rich")
    try:
        from rich.console import Console
        from rich.markdown import Markdown
    except:
        print("Rich Can't be installed for some reason...")
        pass
try:
    console = Console()
except:
    pass

# Rich Styling
style = "cyan"
style1 = "yellow"
style2 = "magenta"
style3 = "red"

def p(x,style):           #Rich Handling if not installed properly
        try:
            console.print(x,style=style)
        except:
            print(x)

# Loader
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

# Loading Printer
def load(x):
    spinner = spinning_cursor()
    for _ in range(x):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def initial_printer():
        console.print(Markdown("# Property Rate Prediction."))
        console.print("[bold] Talk is Cheap, Show me the Code[/bold] -- Linus Torvalds".center(130),style="yellow")

# CODE STARTS HERE
if __name__ == "__main__":
    #Printing Date
    console.print("Date -",datetime.date(datetime.now()),style=style2)
    console.print("Time -",datetime.time(datetime.now()),style=style2)
    console.print()
    initial_printer()

    #Training our machine

    # Reading required csv file
    df = pd.read_csv("filtered_data.csv")

    # one hot encodding concept
    df1 = pd.get_dummies(df,columns=["Status","Furnishing","Transaction","Type"])

    # Feature Scalling
    X = df1[["Area(sqft)","BHK","Bathroom","Parking","Status_Almost_ready","Status_Ready_to_move","Furnishing_Furnished","Furnishing_Semi-Furnished"
         ,"Furnishing_Unfurnished","Transaction_New_Property","Transaction_Resale","Type_Apartment","Type_Builder_Floor"]]
    y = df1["Price"]

    # Preparing data for new model
    X_train, X_test, y_train, y_test = train_test_split(X,y ,random_state=104,test_size=0.25,shuffle=True)

    # using sklearn library in order to train our machine
    # we will use decision tree regressor because it has the highest accuracy.
    regr2 = DecisionTreeRegressor(random_state = 0)
    regr2.fit(X_train, y_train) # 77% accurate

    if os.path.isfile("model.pkl"):
        pass
    else:
        joblib.dump(regr2, "model.pkl")
    # Accuracy has been already checked in jupyter file i.e.PROJECT JUPYTER FILE

    # Now we have to create a system to take input from the USER.
    # Here we will use rich library in order to create a well interative CLI.


    # Error handling
    try:
        area = float(input("Enter the area in sqft :"))
        bhk = int(input("Enter the number of BHK :"))
        bathroom = int(input("Number of bathrooms :"))
        parking = int(input("Enter the number of parking slots :"))
    except:
        print("Please enter the input in numbers!!")
        area = float(input("Enter the area in sqft :"))
        bhk = int(input("Enter the number of BHK :"))
        bathroom = int(input("Number of bathrooms :"))
        parking = int(input("Enter the number of parking slots :"))

    # Taking input of categorical values by creating a MENU

    p("CHOOSE THE STATUS :",style=style)
    p("1. ALMOST READY",style=style1)
    p("2. READY TO MOVE",style=style1)

    try:
        status = int(input("Enter your choice :"))
    except:
        p("Please enter your choice in numbers!!")
        status = int(input("Enter your choice :"))

    status_list = [0,0]
    if status == 1:
        status_list[0] = 1
    elif status == 2:
        status_list[1] = 1
    else:
        p("Wrong choice\nTerminating Program...",style3)
        load(25)
        exit()


    p("CHOOSE Furnishing :",style=style)
    p("1. Furnished",style=style1)
    p("2. Semi-Furnished",style=style1)
    p("3. Unfurnished",style=style1)

    try:
        furnished = int(input("Enter your choice :"))
    except:
        p("Please enter your choice in numbers!!")
        furnished = int(input("Enter your choice :"))

    furnished_list = [0,0,0]
    if furnished == 1:
        furnished_list[0] = 1
    elif furnished == 2:
        furnished_list[1] = 1
    elif furnished == 3:
        furnished_list[2] = 1
    else:
        p("Wrong choice\nTerminating Program...",style3)
        load(25)
        exit()


    p("CHOOSE TRANSACTION :",style=style)
    p("1. NEW PROPERTY",style=style1)
    p("2. RESALE",style=style1)

    try:
        transaction = int(input("Enter your choice :"))
    except:
        p("Please enter your choice in numbers!!")
        transaction = int(input("Enter your choice :"))

    transaction_list = [0,0]
    if transaction == 1:
        transaction_list[0] = 1
    elif transaction == 2:
        transaction_list[1] = 1
    else:
        p("Wrong choice\nTerminating Program...",style3)
        load(25)
        exit()


    p("CHOOSE TYPE :",style=style)
    p("1. APPARTMENT",style=style1)
    p("2. BUILDING FLAT",style=style1)

    try:
        type1 = int(input("Enter your choice :"))
    except:
        p("Please enter your choice in numbers!!")
        type1 = int(input("Enter your choice :"))

    type1_list = [0,0]
    if type1 == 1:
        type1_list[0] = 1
    elif type1 == 2:
        type1_list[1] = 1
    else:
        p("Wrong choice\nTerminating Program...",style3)
        load(25)
        exit()


    # Now its time to predict the price of the given property info.
    predicted_price = regr2.predict([[area,bhk,bathroom,parking,status_list[0],status_list[1],
        furnished_list[0],furnished_list[1],furnished_list[2],transaction_list[0],transaction_list[1],
        type1_list[0],type1_list[1]]])

    p(f"PRICE PREDICTED = {predicted_price[0]}",style2)
