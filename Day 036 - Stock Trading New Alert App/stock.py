import requests
from auth import aa_key, news_key
from datetime import date, timedelta

class Stock():

    def __init__(self, stock_id, stock_name):
        self.name = stock_name
        self.id = stock_id
        self.set_dates()

    def get_stock(self):
        # get stock data
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.id}&apikey={aa_key}'
        r = requests.get(url)
        data = r.json()["Time Series (Daily)"]
        # Get high for previous 2 days
        #print(url)

        y_high = float(data[self.yesterday]["4. close"])
        db_high = float(data[self.day_before]["4. close"])

        # Percentage Change
        return (abs(y_high - db_high)/db_high)*100

    def get_news(self):
        url = ('https://newsapi.org/v2/everything?'
               f'qInTitle={self.name}&'
               f'from={self.yesterday}&'
               'sortBy=popularity&'
               f'apiKey={news_key}')
        r = requests.get(url)
        data = r.json()
        articles = ""
        for each in range(0,3):
            source = data["articles"][each]["source"]["id"]
            if source:
                source = source.title()
            title = data["articles"][each]["title"]
            summary = data["articles"][each]["description"].encode('utf-8')
            articles+=(f"Source: {source}: {title}\nBrief: {summary}\n\n")
        return articles


    def set_dates(self):
        ## Establish dates for yesterday and day before yesterday
        days_between = 1

        if date.today().weekday() == 0:
            days_between = 3
        if date.today().weekday() == 1:
            days_before_days = 4
        else:
            days_before_days = days_between + 1

        self.yesterday = str(date.today() - timedelta(days=days_between))
        self.day_before = str(date.today() - timedelta(days=days_before_days))
