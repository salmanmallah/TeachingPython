"""
    CHAPTER 7
    Add Delete Data From Dictionaries
"""
user_info = {
    'name' : 'salman',
    'age'  : '21',
    'fav_bike' : 'heavy bike',
    'fav_cars' : 'GT MUSTANG',
    'fav_mobile': 'Xiomi 120 watt charing'
}


# ADD DATA TO DICTIONARY
# user_info['fav_cars'] = 'GT MUSTANG'


# for key, value in user_info.items():
#     print(f"    {key} = {value} ")


# delete data
# pop() method

# popped_item = user_info.pop('name')
# print(user_info)
# print(popped_item)


# popitem() method
# it will randomly remove key value pair

popped_item = user_info.popitem()
print(user_info)
print(popped_item)

