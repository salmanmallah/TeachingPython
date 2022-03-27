"""
    CHAPTER 12
    LAMBDA PRACTICE
"""
# lambda expression practice
is_even = lambda n : n%2==0
print(is_even(9))

name_reverse = lambda name : name[::-1]
print(name_reverse('salman'))


'''LAMBDA EXPRESSION WITH IF ELSE STATEMENTS'''

func = lambda name: True if len(name) > 5 else False

# now the simplest form
func2 = lambda name: len(name) > 5

print(
    func2('salman')
)