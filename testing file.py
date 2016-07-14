def bean_price():
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = (text.find(">$"))
    start = where + 2
    end = start + 4
    price = float(text[start:end])

price = 99.9
bean_price()