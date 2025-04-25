import pandas as pd

def grouping_and_aggregating_data():
    # Create a sample DataFrame
    data = {'Department': ['Sales', 'Sales', 'Marketing', 'Marketing', 'IT', 'IT'],
            'Employee': ['John', 'Jane', 'Mike', 'Emily', 'David', 'Sarah'],
            'Salary': [50000, 60000, 70000, 80000, 90000, 100000]}
    df = pd.DataFrame(data)

    # Group by department and calculate the mean salary
    grouped_df = df.groupby('Department')['Salary'].mean()
    print("Mean salary by department:\n", grouped_df)

    # Group by department and calculate the sum and count of salaries
    grouped_df = df.groupby('Department')['Salary'].agg(['sum', 'count'])
    print("\nSum and count of salaries by department:\n", grouped_df)

grouping_and_aggregating_data()
