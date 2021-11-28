"""
    Chapter Three
    and, or Operators in python
"""
import webbrowser as web
import time as t

name = input('Enter your name : ')
age = input('Enter your age : ')

if name == 'salman'.upper() and int(age) == 20:
    t.sleep(2)
    print("Results loading... %25")
    t.sleep(0.5)
    print("        loading... %50")
    t.sleep(0.5)
    print("        loading... %75")
    t.sleep(1.5)
    print("        loading... %100")
    t.sleep(1)
    print("\n Your performance has been successfully analyzed...")
    web.open("https/:www.youtube.com")
