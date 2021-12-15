"""
    CHAPTER 7
    update() method
"""
user_info = {
    'name' : 'salman',
    'age'  : '21',
    'fav_bike' : 'heavy bike',
    'fav_cars' : 'GT MUSTANG',
    'fav_mobile': 'Xiomi 120 watt charing'
}

more_info = {
    'email': 'sufisalman06@gmail.com',
    'password' : 'salman00',
}

user_info.update(more_info)
print(user_info)