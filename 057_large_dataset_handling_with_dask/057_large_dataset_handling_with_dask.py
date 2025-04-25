import dask.dataframe as dd
import pandas as pd
import numpy as np

def large_dataset_handling_with_dask():
    # Create a large CSV file (replace with your actual large dataset)
    def create_large_csv(filename, nrows=100000):
        data = {'col1': np.random.rand(nrows),
                'col2': np.random.randint(0, 100, nrows),
                'col3': np.random.choice(['A', 'B', 'C'], nrows)}
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

    filename = "large_data.csv"
    create_large_csv(filename)

    # Read the CSV file into a Dask DataFrame
    ddf = dd.read_csv(filename)

    # Perform some operations on the Dask DataFrame
    mean_col1 = ddf['col1'].mean().compute()
    print("Mean of col1:", mean_col1)

    value_counts_col3 = ddf['col3'].value_counts().compute()
    print("\nValue counts of col3:\n", value_counts_col3)

large_dataset_handling_with_dask()
