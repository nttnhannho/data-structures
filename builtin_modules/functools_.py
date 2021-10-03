# reduce, total_ordering, cached_property, lru_cached, partial, wraps, singledispatch
# cached_property => this module will support to cache the value for the next time execute. Only supported >= 3.8
from functools import reduce, total_ordering, lru_cache, partial, wraps, singledispatch


@total_ordering
class Car:
    def __init__(self, model_, mileage_):
        self.__model = model_
        self.__mileage = mileage_

    def __eq__(self, other):
        return self.__mileage == other.__mileage

    def __lt__(self, other):
        return self.__mileage < other.__mileage

    # @cached_property
    def model(self):
        print("Getting model...")
        return self.__model


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def add(a, b):
    print(a, b)
    return a + b


def mylogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@mylogger
def mul(a, b):
    """
    Multiply a to b
    """
    return a * b


@singledispatch
def print_type(obj):
    pass


@print_type.register(list)
def _(obj):
    return "List"


@print_type.register(str)
def _(obj):
    return "String"


@print_type.register(int)
def _(obj):
    return "Integer"


if __name__ == "__main__":
    # reduce
    red_ = [1, 2, 3, 4, 5]
    print(reduce(lambda x, y: max(x, y), red_))

    # total_ordering: support to define a handy comparison operator for a class
    # Have to define __eq__() and one of among (__lt__(), __gt__(), __le__(), __ge__())
    audi = Car("Audi", 100)
    bmw = Car("BMW", 200)
    print(audi == bmw)
    print(audi < bmw)
    print(audi > bmw)
    print(audi <= bmw)
    print(audi >= bmw)

    # # cached_property
    # audi = Car("Audi", 100)
    # print(audi.model)

    # lru_cache: efficient way to implement using memoization method
    # Allow memory to save the least recent used (lru) item in cached
    audi = Car("Audi", 100)
    import time
    ms = time.time_ns()
    print([fib(n) for n in range(1000)])
    print(time.time_ns() - ms)

    # partial
    add_one = partial(add, 1)
    print(add_one(4))

    # wraps: ignore the wrapper function inside the closure
    print(mul(2, 5))
    print(mul.__name__)
    print(mul.__doc__)

    # singledispatch: method overloading
    print(print_type("sss"))
    print(print_type(111))
    print(print_type([1, 2]))
