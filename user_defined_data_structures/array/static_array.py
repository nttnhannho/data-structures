from abc import ABC, abstractmethod


class StaticArrayADT(ABC):
    @abstractmethod
    def __len__(self):
        """
        Length of array
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Print array
        """
        pass

    @abstractmethod
    def __setitem__(self, index_, item_):
        """
        Set item by index
        """
        pass

    @abstractmethod
    def __getitem__(self, index_):
        """
        Fetch item by index
        """
        pass

    @abstractmethod
    def __contains__(self, item_):
        """
        Check if array contains given item
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear array
        """
        pass

    @abstractmethod
    def search(self, item_):
        """
        Search index of item
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Check if array is empty
        """
        pass


class StaticArray(StaticArrayADT):
    def __init__(self, *args):
        self.__n = len([*args])
        self.__arr = [*args]

    def __len__(self):
        return self.__n

    def __str__(self):
        return f"{[self.__arr[i] for i in range(self.__n)]}"

    def __setitem__(self, index_, item_):
        if not self.__is_valid_index(index_):
            raise IndexError("Index error")
        self.__arr[index_] = item_

    def __getitem__(self, index_):
        if not self.__is_valid_index(index_):
            raise IndexError("Index error")
        return self.__arr[index_]

    def __contains__(self, item_):
        for i in range(self.__n):
            if item_ == self.__arr[i]:
                return True
        return False

    def clear(self):
        self.__n = 0

    def search(self, item_):
        for i in range(self.__n):
            if item_ == self.__arr[i]:
                return i
        return -1

    def is_empty(self):
        return self.__n == 0

    def __is_valid_index(self, index_):
        return 0 <= index_ < self.__n


if __name__ == "__main__":
    arr = StaticArray(1, 2, 3, 4, 5)
