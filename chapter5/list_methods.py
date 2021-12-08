"""
    CHAPTER 5
    - method to add data in list
     append()
        Add a single element to the end of the list
     insert()
        insert an element to the list
    extend()
        adds iterable elements to the end of the list


    pop()
        Removes element at the given index
    remove()
        Removes item from the list

"""
animal = ['Cat', 'Dog', 'Elephant']

# append() method
# animal.append('Frog')
# print(animal)

# adding list to a list
animalTwo = ['Giraffe', 'Horse']
# animal.append(animalTwo)
# print(animal)

# insert() method
animal.insert(0, 'Alligator', )
# print(animal)

vowels = ['a', 'e', 'i', 'u']
# vowels.insert(3, 'o')
# print(vowels)

# concatenate two list by using + operator
empty_list = animal + vowels
# print(empty_list)

# extend() method
# animal.extend(vowels)
# print(animal)

'''
    DELETE DATA FROM LIST
'''
passwords = ['salman', 'namlas06', 'google.com.com.com']

# pop() method
# print(passwords)
# print(passwords.pop(1))
# print(passwords)

# del operator
# print(passwords)
# del passwords[1]

# remove() method
passwords.remove('namlas06')
print(passwords)


name = input("enter your name : ")
if name in passwords:
    print('password found in data base')
else:
    print('not found ')
