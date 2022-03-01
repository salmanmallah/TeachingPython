
"""
    CHAPTER 7
    TEST TWO
    -Take data from user and store it in dictionary
    -Print dictionary data vertically.
"""

name = input('Enter your name : ')
age = input('Enter your age : ')
email = input('Enter your email : ')
fav_color = input('Enter your favourite color comma seperated : ').split(',')

user_info_dict = {'name': name, 'age': age, 'email': email, 'fav_color': fav_color}

for key, value in user_info_dict.items():
    print(f"{key} : {value}")



