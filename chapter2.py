import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf8")
price = text[234:238]
output = 'Current cost of coffee is £' + str(price)
print (output)

