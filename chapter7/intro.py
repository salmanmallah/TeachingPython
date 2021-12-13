"""
    Introduction to Dictionaries.

    why we use dictionaries?
    -Because of limitation of lists, list are not enought to represent real data.
        EXAMPLE:
            user = ['salman', 20, [fav_movies, 'tarzan'], ['fav_hero', 'superMan']]
            #this list contains usr's name, age, fav movies, far_hero,
            #you can do this but this is not good way to do this.

        Q: what are dictionaries?
        A: Unordered collections of data in [key: value] pair.
"""

user_info = {'key': 'value', 'name':'salman', 'age': 20}

second_dict = dict(name='salman', age=20, sex='male')
print(second_dict)

print(second_dict['name'])