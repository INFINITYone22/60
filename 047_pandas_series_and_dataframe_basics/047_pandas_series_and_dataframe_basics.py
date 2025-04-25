import pandas as pd

def pandas_series_and_dataframe_basics():
    # Create a Pandas Series
    data = [10, 20, 30, 40, 50]
    series = pd.Series(data)
    print("Pandas Series:\n", series)

    # Create a Pandas DataFrame
    data = {'name': ['John', 'Jane', 'Mike'],
            'age': [30, 25, 35],
            'city': ['New York', 'London', 'Paris']}
    df = pd.DataFrame(data)
    print("\nPandas DataFrame:\n", df)

    # Access data in the DataFrame
    print("\nName column:\n", df['name'])
    print("\nFirst row:\n", df.iloc[0])

pandas_series_and_dataframe_basics()
