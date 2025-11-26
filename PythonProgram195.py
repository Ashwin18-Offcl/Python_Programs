#simple pandas code
import pandas as pd
#1.Create a simple dataset
data = {
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,30,35,40],
    'City';['New York','Los Angeles','Chicago','Houston']
    #2.Convert dictionary to Dataframe
    df=pd.DataFrame(data)
    #3.Shows the first few rows
    print("Dataframe:")
    print(df)
    #4.Filter:People older than 30
    print("\nPeople older than 30:")
    print(df[df['Age']>30])
    #5.Basic statistics
    print("\nSummary statistic:")
    print(df.describe())

}