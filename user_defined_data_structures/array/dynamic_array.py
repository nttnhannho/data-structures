from abc import ABC, abstractmethod
import ctypes


class DynamicArrayADT(ABC):
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
    def append(self, item_):
        """
        Append item to the end of array
        """
        pass

    @abstractmethod
    def insert(self, index_, item_):
        """
        Insert item at specific index
        """
        pass

    @abstractmethod
    def __delitem__(self, index_):
        """
        Remove item at index
        """
        pass

    @abstractmethod
    def remove(self, item_):
        """
        Remove item
        """
        pass

    @abstractmethod
    def pop(self):
        """
        Return and remove last item
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

    @abstractmethod
    def __contains__(self, item_):
        """
        Check if array contains given item
        """
        pass


class DynamicArray(DynamicArrayADT):
    def __init__(self):
        self.__n = 0
        self.__size = 1
        self.__arr = DynamicArray.__make_array(self.__size)

    @staticmethod
    def __make_array(capacity_):
        return (capacity_ * ctypes.py_object)()

    def __len__(self):
        return self.__n

    def __str__(self):
        return f"{[self.__arr[i] for i in range(self.__n)]}"

    def __setitem__(self, index_, item_):
        if index_ < 0 or index_ > self.__n:
            raise Exception("Index error")
        self.__arr[index_] = item_

    def __getitem__(self, index_):
        if index_ < 0 or index_ > self.__n:
            raise Exception("Index error")
        return self.__arr[index_]

    def append(self, item_):
        if self.__n == self.__size:
            self.__resize(2 * self.__size)

        self.__arr[self.__n] = item_
        self.__n += 1

    def __resize(self, new_capacity_):
        new_arr = DynamicArray.__make_array(new_capacity_)
        self.__size = new_capacity_

        for i in range(self.__n):
            new_arr[i] = self.__arr[i]

        self.__arr = new_arr

    def insert(self, index_, item_):
        if index_ < 0 or index_ > self.__n:
            raise Exception("Index error")

        if self.__n == self.__size:
            self.__resize(2 * self.__size)

        for i in range(self.__n - 1, index_ - 1, -1):
            self.__arr[i + 1] = self.__arr[i]

        self.__arr[index_] = item_
        self.__n += 1

    def __delitem__(self, index_):
        if index_ < 0 or index_ > self.__n:
            raise Exception("Index error")

        if self.__n <= (self.__size / 2):
            self.__resize(self.__size / 2)

        for i in range(index_, self.__n - 1):
            self.__arr[i] = self.__arr[i + 1]

        self.__n -= 1

    def remove(self, item_):
        if self.__n <= (self.__size / 2):
            self.__resize(self.__size / 2)

        for i in range(self.__n):
            if self.__arr[i] == item_:
                for j in range(i, self.__n - 1):
                    self.__arr[j] = self.__arr[j + 1]
                self.__n -= 1
                break
        else:
            raise Exception(f"{item_} is not existed")

    def pop(self):
        temp = self.__n
        self.__n -= 1
        return temp

    def clear(self):
        self.__n = 0
        self.__size = 1

    def search(self, item_):
        for i in range(self.__n):
            if self.__arr[i] == item_:
                return i
        return -1

    def is_empty(self):
        return self.__n == 0

    def __contains__(self, item_):
        for i in range(self.__n):
            if self.__arr[i] == item_:
                return True
        return False


if __name__ == "__main__":
    arr = DynamicArray()
