"""
    CHAPTER 7
    Add Delete Data From Dictionaries
"""
user_info = {
    'KEYS' : 'VALUES',
    'name' : 'salman',
    'age'  : '21',
    'fav_bike' : 'heavy bike',
    'fav_cars' : 'GT MUSTANG',
    'fav_mobile': 'Xiomi 120 watt charing'
}

user_info['shoes'] = ['chapal', 'sleeper', 'joger']
# print(  user_info)

for key, value in user_info.items():
    print(f'{key} : {value}')


# ADD DATA TO DICTIONARY
# user_info['fav_cars'] = 'GT MUSTANG'


# for key, value in user_info.items():
#     print(f"    {key} = {value} ")


# DELETE DATA WITH  POP() METHOD

# popped_item = user_info.pop('name')
# print(user_info)
# print(popped_item)


# popitem() method
# it will randomly remove key value pair

# popped_item = user_info.popitem()
# print(user_info)
# print(popped_item)

