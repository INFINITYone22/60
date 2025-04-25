import pandas as pd
import numpy as np

def data_cleaning_and_preprocessing():
    # Create a sample DataFrame with missing values and duplicates
    data = {'ID': [1, 2, 3, 4, 5, 2, 4],
            'Name': ['John', 'Jane', 'Mike', 'Emily', 'John', 'Jane', 'Emily'],
            'Age': [30, 25, None, 35, 30, 25, None],
            'City': ['New York', 'London', 'Paris', 'Tokyo', 'New York', 'London', 'Tokyo'],
            'Salary': [50000, 60000, 70000, 80000, 50000, 60000, 80000]}
    df = pd.DataFrame(data)

    # Handle missing values
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    print("DataFrame with missing values filled:\n", df)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    print("\nDataFrame with duplicates removed:\n", df)

    # Convert data types
    df['Age'] = df['Age'].astype(int)
    print("\nDataFrame with converted data types:\n", df)

data_cleaning_and_preprocessing()
