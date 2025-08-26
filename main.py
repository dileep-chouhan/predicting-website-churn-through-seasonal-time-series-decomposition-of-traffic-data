import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
# --- 1. Synthetic Data Generation ---
np.random.seed(42)  # for reproducibility
dates = pd.date_range(start='2022-01-01', periods=365)
traffic = 1000 + 200 * np.sin(2 * np.pi * np.arange(365) / 365) + 50 * np.random.randn(365) #Seasonal trend + noise
churn = np.random.binomial(1, 0.05, size=365) # 5% churn rate
df = pd.DataFrame({'Date': dates, 'WebsiteTraffic': traffic, 'Churn': churn})
# --- 2. Time Series Decomposition ---
decomposition = seasonal_decompose(df['WebsiteTraffic'], model='additive', period=30) # Assuming roughly monthly seasonality
# --- 3. Visualization and Saving ---
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df['WebsiteTraffic'], label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(decomposition.trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(decomposition.seasonal, label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(decomposition.resid, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
output_filename = 'time_series_decomposition.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# --- 4.  Churn Correlation Analysis (Illustrative) ---
#  This section is illustrative and would need more sophisticated modeling for a real-world application.
#  It simply checks for correlation between the residuals (noise) and churn.  
correlation = df['Churn'].corr(decomposition.resid)
print(f"\nCorrelation between Residuals (Noise) and Churn: {correlation}")
# Note: A strong correlation might suggest that unaccounted factors in the residuals are impacting churn.
# More advanced modeling (e.g., ARIMA, Prophet, incorporating other features) would be needed for robust prediction.
# --- 5.  Further Analysis (Suggestions) ---
# 1. Explore other time series models (ARIMA, SARIMA, Prophet) for more accurate forecasting.
# 2. Incorporate other relevant features (e.g., marketing campaigns, website updates) to improve model accuracy.
# 3. Develop a churn prediction model using machine learning techniques (e.g., logistic regression, random forest).
# 4. Evaluate model performance using appropriate metrics (e.g., AUC, precision, recall).