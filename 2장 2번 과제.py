#컴퓨터 공학과, 20234057,김운호 
print("컴퓨터 공학 ,20234057,김운호")


import urllib.request
import time
price = 99.99

while price >4.74:
    
    
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price:end_of_price])
    
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    when = text.find("<p>Price on")
    start_of_time = when + 12
    end_of_time=start_of_time + 25
time =  str(text[start_of_time:end_of_time])
print(price)
print(time)

