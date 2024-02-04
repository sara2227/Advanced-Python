from typing import Any
import time
from functools import wraps


'''
This file includes the examples of using decorators. One of the most using decorators is add logging and timer for any function.
'''
def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

class decorator_class(object):
    def __init__(self,original_function):
        self.original_function = original_function
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

# using @decorator_function is equal to: display_info == decorator_function(display_info)
print('--------- Examples of using decorator_function---------------')

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

@decorator_function
def display():
    print('display ran!')

display_info('John' , 25)
display()

print('********** Examples of using decorator_class ***********')

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('Sara',30)

print('********** Example of using timer and logger decorator ***********')

def my_timer(func):
    import time
    @wraps(func)
    def time_wrapper(a,b):
        print('inside time wrapper.')
        start = time.time()
        func(a,b)
        end = time.time()
        print(f'duaration of executing the {func.__name__} is: {end-start}')
    return time_wrapper

def my_logger(func):
    import logging
    logging.basicConfig(filename = f'{func.__name__}.log', level=logging.INFO)
    @wraps(func)
    def wrapper_logger(*args,**kwargs):
        print('inside logging wrapper.')
        logging.info(f'Ran {func.__name__} with args:{args}')
        return func(*args,**kwargs)
    return wrapper_logger
        
@my_timer
@my_logger
def multiply(a,b):
    time.sleep(2)
    print('inside the multiply function.')
    c = a*b
    print(f'the result of multiplying {a},{b} is {c}')

multiply(2,3)



