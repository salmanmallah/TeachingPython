"""
    Chapter Three
    Test Two

    # Watch COCO
        *Ask user's name and age
        *if user's name start with ('S' or 's') and age is above 10.
        *print you can watch coco movie
        *else print Sorry, you can't watch coco.

"""
name = input('Enter you name: ')
age = int(input('Enter you age: '))
if age >= 10 and (name[0] == 'S' or name[0] == 's'):
    print('You can watch Coco')
else:
    print('You can\'t  watch coco')
