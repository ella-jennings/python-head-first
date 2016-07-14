import urllib.request
import time

price = 99.9

while price > 4.74:
    time.sleep(900)
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = (text.find(">$"))
    start = where+2
    end = start+4
    price = float(text[start:end])

output = 'Current cost of coffee is £' + str(price) + ' - you should buy it now!'
print (output)
