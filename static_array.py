from abc import ABC, abstractmethod


class StaticArrayADT(ABC):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def get(self, index_):
        pass

    @abstractmethod
    def index_of(self, value_):
        pass

    @abstractmethod
    def contains(self, value_):
        pass

    @abstractmethod
    def clear(self):
        pass


class StaticArray(StaticArrayADT):
    def __init__(self, *args, type_=int):
        self.__size = len(list(map(type_, [*args])))
        self.__items = [*args]

    def __str__(self):
        return f"[{', '.join([str(i) for i in self.__items])}]"

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def get(self, index_):
        return self.__items[index_]

    def index_of(self, value_):
        return self.__items.index(value_)

    def contains(self, value_):
        return value_ in self.__items

    def clear(self):
        self.__items = [None] * self.__size


if __name__ == "__main__":
    int_arr = StaticArray(1, 2, 3, 4, 5)
    print(int_arr)
    print(int_arr.size())
    print(int_arr.is_empty())

    print(int_arr.get(0))
    print(int_arr.get(1))
    print(int_arr.get(2))
    print(int_arr.get(3))
    print(int_arr.get(4))

    print(int_arr.index_of(1))
    print(int_arr.index_of(2))
    print(int_arr.index_of(3))
    print(int_arr.index_of(4))
    print(int_arr.index_of(5))

    print(int_arr.contains(6))
    print(int_arr.contains(5))

    # print(int_arr.get(5))
    # print(int_arr.index_of(6))

    int_arr.clear()
    print(int_arr)
    print(int_arr.size())
