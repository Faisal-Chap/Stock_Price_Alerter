# Stock Price Change and News Alert Script

## Overview
This script monitors the stock price of a given company (Tesla Inc. in this case) and sends an alert via Twilio SMS if there is a significant price change. If the stock price changes by more than 2%, the script fetches related news articles and sends them along with the alert.

## Features
- Fetches daily stock price data from Alpha Vantage.
- Detects significant price changes (greater than 2%).
- Retrieves the latest news related to the company from NewsAPI.
- Sends an SMS alert with stock movement details and relevant news headlines using Twilio.

## Setup and Installation

### Prerequisites
1. Python 3 installed on your system.
2. Required Python libraries:
   - `requests`
   - `twilio`
3. API keys for the following services:
   - [Alpha Vantage](https://www.alphavantage.co) (for stock price data)
   - [NewsAPI](https://newsapi.org) (for news headlines)
   - [Twilio](https://www.twilio.com) (for sending SMS alerts)

### Installation
Run the following command to install required dependencies:
```sh
pip install requests twilio
```

## Configuration
1. **API Keys:** Replace the placeholders in the script with your actual API keys:
   - `APIKEY = "your_alpha_vantage_api_key"`
   - `NEWSAPI = "your_newsapi_key"`
   - `account_sid = "your_twilio_account_sid"`
   - `auth_token = "your_twilio_auth_token"`

2. **Stock Symbol & Company Name:** Modify the `STOCK` and `COMPANY_NAME` variables if monitoring a different company:
   ```python
   STOCK = "TSLA"
   COMPANY_NAME = "Tesla Inc"
   ```

3. **Twilio Phone Numbers:**
   - Replace `twilio_phone_number` with your Twilio-provided number.
   - Replace `recipient_phone_number` with your personal phone number.

## How It Works
1. The script determines the stock price changes over the last few days while accounting for weekends and holidays.
2. If a price change greater than 2% is detected, it fetches the latest news related to the company.
3. The news headline and brief description are formatted into a message.
4. Twilio is used to send the alert to the specified phone number.

## Example SMS Alert
```
TSLA: 🔺%
Headline: Tesla's new model reaches record sales!
Brief: Tesla's latest electric vehicle has outsold its competitors...
```

## Future Improvements
- Add support for multiple stock symbols.
- Improve error handling for API failures.
- Implement a configurable percentage threshold for alerts.
- Support for email notifications in addition to SMS.

## Disclaimer
This script is for educational purposes only. Always verify stock price data and consult financial professionals before making investment decisions.

