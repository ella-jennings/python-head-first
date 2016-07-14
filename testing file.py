import urllib.request

def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = (text.find(">$"))
    start = where + 2
    end = start + 4
    print(text[start:end])

get_price()
