"""
    CHAPTER 7
    LOOPING IN DICTIONARY | IN KEYWORD IN DICTIONARY

"""

# user_info = {
#     'name' : 'salman',
#     'age'  : '21',
#     'fav_bike' : 'heavy bike',
#     'fav_mobile' : 'Xiomi 120 watt charing'
# }

# check if key exists in dict or not
# if 'name' in user_info:
#     print('Present', user_info['name'])
# else:
#     print('name is not present')


# check value exist in dict or not
# if 'salman' in user_info.values():
#     print('present')
# else:
#     print('not present')


# looping with dictionary
# for i in user_info:
#     print(i)
#
# for i in user_info.values():
#     print(i)

# info_values = user_info.values()
# print(type(info_values))



# IMPORTANT METHOD items()

user_info = {
    'name' : 'salman',
    'age'  : '21',
    'fav_bike' : 'heavy bike',
    'fav_mobile' : 'Xiomi 120 watt charing'
}

# printing dict keys
for i in user_info:
    print(i)

# printing dict values
for i in user_info.values():
    print(type(i))


for key, value in user_info.items():
    print(f"key is : {key} = {value} ")

