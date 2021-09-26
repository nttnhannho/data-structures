from abc import ABC, abstractmethod


class IteratorADT(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass


class Counter(IteratorADT):
    def __init__(self, start_, end_):
        self.__start = start_
        self.__end = end_

    def __iter__(self):
        return self

    def __next__(self):
        current = self.__start
        if self.__start <= self.__end:
            self.__start += 1
            return current
        raise StopIteration


if __name__ == "__main__":
    print("Iter:")
    counter1 = Counter(1, 5)
    iter_ = iter(counter1)
    print(next(iter_))
    print(next(iter_))
    print(next(iter_))
    print(next(iter_))
    print(next(iter_))

    print("For loop:")
    counter2 = Counter(1, 10)
    for item in counter2:
        print(item)
