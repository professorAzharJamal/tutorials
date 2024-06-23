#pip install pandas numpy scikit-learn matplotlib yfinance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import yfinance as yf

# Function to download stock data
def download_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Function to prepare the data
def prepare_data(data, future_days):
    data = data[['Close']]
    data['Prediction'] = data['Close'].shift(-future_days)
    X = np.array(data.drop(['Prediction'], axis=1))[:-future_days]
    y = np.array(data['Prediction'])[:-future_days]
    return X, y, data

# Function to train the model
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Function to visualize the results
def visualize_results(data, future_days, predictions, ticker):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Actual Price')
    plt.plot(range(len(data) - future_days, len(data)), predictions, label='Predicted Price')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'{ticker} Stock Price Prediction')
    plt.show()

# Main function to run the stock prediction
def main():
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    future_days = 30

    # Download stock data
    data = download_stock_data(ticker, start_date, end_date)

    # Prepare the data
    X, y, data = prepare_data(data, future_days)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train the linear regression model
    model = train_model(X_train, y_train)

    # Test the model
    confidence = model.score(X_test, y_test)
    print(f'Model Confidence: {confidence}')

    # Get the last 'future_days' rows from the original dataset
    X_future = np.array(data.drop(['Prediction'], axis=1))[-future_days:]

    # Make predictions for the next 'future_days'
    predictions = model.predict(X_future)

    # Visualize the results
    visualize_results(data, future_days, predictions, ticker)

# Run the main function
if __name__ == "__main__":
    main()
