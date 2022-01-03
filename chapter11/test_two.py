"""
    CHAPTER 11
    TEST TWO

    define a function.
    name=['salman', 'nouman']
    func(name)
    output=> ['Salman', 'Nouman']
"""

# def title_char(*args, reverse=True):
#     temp = []
#     for i in args:
#         if reverse==True:
#             temp.append(i[::-i].title())
#             return temp
#         temp.append(i.title())
#
# print(
#     title_char(['salman','nouman'])
# )

# def rev(name, default_arg=False):
#     return [i[::-1].title() if default_arg==True else i.title() for i in name]

def rev(l,**kwargs):
    return [i[::-1].title() if kwargs.get('reverse_str')==True else i.title() for i in l]




print(
    rev(['salman', 'noman'], reverse_str=True)
)