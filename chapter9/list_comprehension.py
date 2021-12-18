"""
    CHAPTER 9
    WHAT IS LIST COMPREHENSION?

"""
# create square from 1 to 10.

# creating a list of sqaure from 1 to 10
s = []
for i in range(1, 11):
    s.append(i**2)
    print(s)


# NOW by using list comprehension
square_list = [i**2 for i in range(1, 11)]
print(square_list)