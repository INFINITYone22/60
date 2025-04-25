import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def time_series_analysis():
    # Create a sample time series DataFrame
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    values = np.random.randn(100).cumsum()
    df = pd.DataFrame({'Date': dates, 'Value': values})
    df.set_index('Date', inplace=True)

    # Plot the time series
    plt.figure(figsize=(12, 6))
    plt.plot(df['Value'])
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    plt.savefig('time_series.png')
    print("Time series plot saved to time_series.png")

    # Calculate the rolling mean
    rolling_mean = df['Value'].rolling(window=7).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Value'], label='Original')
    plt.plot(rolling_mean, label='Rolling Mean (7 days)')
    plt.title('Time Series with Rolling Mean')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.savefig('time_series_rolling_mean.png')
    print("Time series plot with rolling mean saved to time_series_rolling_mean.png")

time_series_analysis()
