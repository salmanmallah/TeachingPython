"""
    CHAPTER SIX
        * Define a function which take list as input
            [1,2,3, [4, 5], [6, 7], [8, 9]]
            make function which counts list inside list.
            hint type() function.
"""
def list_counter(l):
    counter = 0
    for i in l:
        if type(i) == list:
            counter += 1
    return f'{counter} lists found in your list'

print(
    list_counter([1,2,3, [4, 5], [6, 7], [8, 9]])
)



