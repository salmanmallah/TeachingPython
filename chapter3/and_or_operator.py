"""
    Chapter Three
    and, or Operators in python
"""
import webbrowser as web
import time as t

name = input('Enter your name : ')
age = int(input('Enter your age : '))

if name == 'salman' and age == 20:
    t.sleep(0.5)
    print("Results loading... %25")
    t.sleep(0.5)
    print("        loading... %50")
    t.sleep(0.5)
    print("        loading... %75")
    t.sleep(1.5)
    print("        loading... %100")
    t.sleep(1)
    print("\n Your Identity has been successfully Matched...")
    t.sleep(3)
    print("\n Opening your url...")
    t.sleep(2)
    web.open('https://www.youtube.com/watch?v=gPnfbTTsVl4&ab_channel=WaqasNasir', 1, autoraise=True)
