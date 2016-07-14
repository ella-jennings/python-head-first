import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = (text.find(">$"))
    start = where + 2
    end = start + 4
    return(text[start:end])

print("Welcome to the coffee bean pricing system.")
choice = input("Do you require a price immediately? (Y/N)?")

if choice == "Y":
    price = float(get_price())


if choice == "N":
    price = float(get_price())
    while price > 4.74:
        print ("price is too high, checking in 5s")
        time.sleep(5)
        get_price()
        price = float(get_price())

output = 'Current cost of coffee is £' + str(price) + ' - you should buy it now!'
print (output)
