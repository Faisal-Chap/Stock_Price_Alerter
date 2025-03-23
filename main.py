import requests
import datetime as dt


# alpha vintage api key to spot the stock price changes
APIKEY = "here"
# newsapi.org key
NEWSAPI = "here"
# stock symbol
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Getting the today date
date = dt.datetime.today() 

# holiday correction, managing the subtraction factor by the difference of weekday
t_corec = 1 
y_corec = 2 
ly_corec = 3
if date.weekday()-1 in range(2,4):
    t_corec = 1
    y_corec = 2
    ly_corec = 3
elif date.weekday()-1 == 1:
    t_corec = 1
    y_corec = 2
    ly_corec = 5
elif date.weekday()-1 == 0:
    t_corec = 1
    y_corec = 4
    ly_corec = 5
elif date.weekday()-1 == 5:
    t_corec = 2
    y_corec = 3
    ly_corec = 4
elif date.weekday()-1 == 6:
    t_corec = 3
    y_corec = 4
    ly_corec = 5


# crafting the date to put in the slicing to get the desire output from the data
today = dt.datetime(year=date.year,month=date.month,day=date.day-t_corec)
yesterday = dt.datetime(year=date.year,month=date.month,day=date.day-y_corec)
last_yesterday = dt.datetime(year=date.year,month=date.month,day=date.day-ly_corec)




# Uses https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then fetches the news and alert the user.
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=5min&apikey={APIKEY}'
r = requests.get(url)
data = r.json()

today_high = float(data['Time Series (Daily)'][str(today.date())]['2. high'])
today_low = float(data['Time Series (Daily)'][str(today.date())]['3. low'])

yesterday_high = float(data['Time Series (Daily)'][str(yesterday.date())]['2. high'])
yesterday_low = float(data['Time Series (Daily)'][str(yesterday.date())]['3. low'])

last_yesterday_high = float(data['Time Series (Daily)'][str(last_yesterday.date())] ['2. high'])
last_yesterday_low = float(data['Time Series (Daily)'][str(last_yesterday.date())] ['3. low'])


# comparing the highs and lows to 5% change 
if_high = False
if_low = False
if (today_high - yesterday_high)/yesterday_high * 100 >= 2:
    if_high = True
elif (today_high - last_yesterday_high)/last_yesterday_high * 100 >=2:
    if_high = True
if (today_high - yesterday_high)/yesterday_high * 100 < 2:
    if_low = True
elif (today_high - last_yesterday_high)/last_yesterday_high * 100 <=2:
    if_low = True





## Uses https://newsapi.org
# gets the first 3 news pieces for the COMPANY_NAME. 

news_parameters = {
    'q': COMPANY_NAME,
    'from': str(last_yesterday),
    'to' : str(today),
    'apiKey' : NEWSAPI,
    'searchIn' : 'title'

}
news_url = "https://newsapi.org/v2/everything?"
d = requests.get(url=news_url,params=news_parameters)
d.raise_for_status()
news_data = d.json()
# print(news_data)


# Uses https://www.twilio.com
# Sends a seperate message with the percentage change and each article's title and description to your phone number. 
# Prepare Message
from twilio.rest import Client
if if_high or if_low:
    article = news_data["articles"][0]
    message_body = f"{STOCK}: {'🔺' if if_high else '🔻'}%\n"
    message_body += f"Headline: {article['title']}\n"
    message_body += f"Brief: {article['description']}"

    # Send SMS via Twilio
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    twilio_phone_number = "+1234567890"
    recipient_phone_number = "+0987654321"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

    print(f"Message sent! SID: {message.sid}")
