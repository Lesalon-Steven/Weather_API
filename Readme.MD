# Stock Trading Alert

## Description
This is a stock trading alert system that sends an email alert when a stock price is above or below a certain threshold. The system uses the Alpha Vantage API to get the stock price data and the SendGrid API to send the email alerts.

## Installation

1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Create a free account on [Alpha Vantage](https://www.alphavantage.co/) and get the API key
4. Create a free account on [SendGrid](https://sendgrid.com/) and get the API key
5. Create a `.env` file in the root directory and add the following environment variables:
    ```
    ALPHA_VANTAGE_API_KEY=<your_alpha_vantage_api_key>
    SENDGRID_API_KEY=<your_sendgrid_api_key>
    ```
6. Run the script using `python stock_alert.py`
7. Enter the stock symbol, the price threshold, and the email address to send the alert to
8. The script will run every 5 minutes and send an email alert if the stock price is above or below the threshold


