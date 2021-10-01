from abc import ABC, abstractmethod
from functools import singledispatch


class IteratorADT(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass


class Iter(IteratorADT):
    def __init__(self, iter_):
        self.__iter = iter_
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if isinstance(self.__iter, int):
            if self.__i >= self.__iter:
                raise StopIteration
            i = self.__i
            self.__i += 1
            return i
        elif isinstance(self.__iter, str):
            if self.__i >= len(self.__iter):
                raise StopIteration
            i = self.__iter[self.__i]
            self.__i += 1
            return i
        else:
            raise Exception("Not supported")


def iter_generator(iter_):
    current = 0
    while current < iter_:
        yield current
        current += 1


if __name__ == "__main__":
    print("Next:")
    iter1 = Iter(5)
    itr = iter(iter1)
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))

    print("For loop:")
    iter2 = Iter("nhan_nguyen")
    for item in iter2:
        print(item)

    print("Generator:")
    iter3 = iter_generator(5)
    print(next(iter3))
    print(next(iter3))
    print(next(iter3))
    print(next(iter3))
    print(next(iter3))
