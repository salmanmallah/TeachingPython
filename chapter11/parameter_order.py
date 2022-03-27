"""
    CHAPTER 11
    FUNCTIONS WITH ALL TYPES OF PARAMETER
        NOTE: Very important to understant.
        PADK
        parameters
        *args
        default parameters
        **kwargs
"""
# with default parameters
def prt(name='unknown', age=21):
    print(name)
    print(age)


def parameter_order(name, *args, age=21, **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)

parameter_order('salman',1, 2, 3, a=1, b=2, c=3 )