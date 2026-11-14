def my_decorator(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper
@my_decorator
def greet():
    print('hello world')
greet()

#decorators with arguments using args and kwargs

def new_decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
        return func(*args, **kwargs)
    return wrapper
@new_decorator
def add(a,b):
    return a+b
print(add(10,20))
