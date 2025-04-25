import pandas as pd

def merging_and_joining_datasets():
    # Create two sample DataFrames
    df1 = pd.DataFrame({'ID': [1, 2, 3, 4],
                        'Name': ['John', 'Jane', 'Mike', 'Emily']})
    df2 = pd.DataFrame({'ID': [1, 2, 3, 5],
                        'Age': [30, 25, 35, 28],
                        'City': ['New York', 'London', 'Paris', 'Tokyo']})

    # Merge the DataFrames based on the 'ID' column
    merged_df = pd.merge(df1, df2, on='ID', how='inner')
    print("Merged DataFrame:\n", merged_df)

    # Join the DataFrames based on the index
    df3 = pd.DataFrame({'Grade': ['A', 'B', 'C', 'D']}, index=[1, 2, 3, 4])
    joined_df = df1.join(df3, on='ID', how='inner')
    print("\nJoined DataFrame:\n", joined_df)

merging_and_joining_datasets()
