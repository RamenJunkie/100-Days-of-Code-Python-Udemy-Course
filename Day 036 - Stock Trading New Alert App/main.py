import mailer_class
import stock
# Add each Stock class to the stocks to watch and create an stock class
tesla = stock.Stock("TSLA","Tesla Inc")
microsoft = stock.Stock("MSFT", "Microsoft")
apple = stock.Stock("APPL", "Apple Inc")
att = stock.Stock("T", "AT&T")
#stocks_to_watch = [tesla, microsoft, apple, att]
stocks_to_watch = [microsoft]

### The Free Tier is limited to like 5 calls per minute or something,
### so this is really only actually useful for checking one stock at a time.
### However it COULD do more.

mailer = mailer_class.Mailer()

def check_stock(which_stock):
    message = ""
    change = which_stock.get_stock()
    #print(change)
    # Create Message
    if change <= -5:
        message = f"Subject:{which_stock.name} is down {int(change)}%.\n\n"
        message += which_stock.get_news()
    elif change >= 5:
        message = f"Subject:{which_stock.name} is Up! {int(change)}%.\n\n"
        message += which_stock.get_news()

    if message != "":
        print(message)
        #mailer.send_email(message)

for each in stocks_to_watch:
    check_stock(each)

