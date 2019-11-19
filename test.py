# class DogToy:
#     def speak(self):
#         print("wang wang")

# class CatToy:
#     def speak(self):
#         print("miao miao")

# def toy_factory(toy_type):
#     if toy_type == 'dog':
#         return DogToy()
#     elif toy_type == 'cat':
#         return CatToy()

# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             _instance = super().__new__(cls, *args, **kwargs)
#             cls._instance = _instance
#         return cls._instance

# class MyClass(Singleton):
#     pass

# c1 = MyClass()
# c2 = MyClass()
# c1 is c2 # true


# from functools import wraps

# def cache(func):
#     store = {}

#     @wraps(func)
#     def _(n):
#         if n in store:
#             return store[n]
#         else:
#             res = func(n)
#             store[n] = res
#             return res
#     return _

# @cache
# def f(n):
#     if n <= 1:
#         return 1
#     return f(n-1) + f(n-2)


# class Singleton(type):
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instance


# # Python2
# class Foo(object):
#     __metaclass__ = Singleton


# foo1 = Foo()
# foo2 = Foo()
# print(foo1 is foo2)  # True

# class Singleton(type):
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instance


# # Python2
# class Foo(object):
#     __metaclass__ = Singleton

# # Python3
# # class Foo(metaclass=Singleton):
# #     pass

# foo1 = Foo()
# foo2 = Foo()
# print(foo1 is foo2)  # True

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    
class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)  # True
