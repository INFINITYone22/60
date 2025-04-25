import pandas as pd

def excel_file_handling_with_pandas():
    # Create a sample DataFrame
    data = {'Name': ['John', 'Jane', 'Mike', 'Emily'],
            'Age': [30, 25, 35, 28],
            'City': ['New York', 'London', 'Paris', 'Tokyo']}
    df = pd.DataFrame(data)

    # Write the DataFrame to an Excel file
    df.to_excel("output.xlsx", sheet_name="Sheet1", index=False)
    print("DataFrame written to output.xlsx")

    # Read the Excel file into a DataFrame
    df_read = pd.read_excel("output.xlsx", sheet_name="Sheet1")
    print("\nDataFrame read from output.xlsx:\n", df_read)

excel_file_handling_with_pandas()
