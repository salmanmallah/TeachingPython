"""
    CHAPTER 11
    intro to **kwargs
    kwargs stand for keyword argument.
    **kwargs (double star argument).
"""
def func(**kwargs):
    print(kwargs)

func(name='salman', age=21)