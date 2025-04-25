import numpy as np
from scipy import stats

def statistical_analysis_with_scipy():
    # Generate two sample datasets
    data1 = np.random.normal(0, 1, 100)
    data2 = np.random.normal(0.5, 1.5, 100)

    # Perform a t-test
    t_statistic, p_value = stats.ttest_ind(data1, data2)
    print("T-statistic:", t_statistic)
    print("P-value:", p_value)

    # Perform a Shapiro-Wilk test for normality
    shapiro_statistic, shapiro_p_value = stats.shapiro(data1)
    print("\nShapiro-Wilk statistic:", shapiro_statistic)
    print("Shapiro-Wilk p-value:", shapiro_p_value)

statistical_analysis_with_scipy()
