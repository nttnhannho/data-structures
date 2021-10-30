from abc import ABC, abstractmethod
import ctypes


class EmptyArrayError(Exception):
    def __init__(self, msg_):
        self.__msg = msg_

    def __str__(self):
        return f"{self.__msg}"


class ElementNotFoundError(Exception):
    def __init__(self, msg_):
        self.__msg = msg_

    def __str__(self):
        return f"{self.__msg}"


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
    def __delitem__(self, index_):
        """
        Remove item at index
        """
        pass

    @abstractmethod
    def __contains__(self, item_):
        """
        Check if array contains given item
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
    def remove(self, item_):
        """
        Remove item
        """
        pass

    @abstractmethod
    def remove_at(self, index_):
        """
        Remove item at index
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


class DynamicArray(DynamicArrayADT):
    @staticmethod
    def __make_array(capacity_):
        return (capacity_ * ctypes.py_object)()

    def __init__(self):
        self.__size = 0
        self.__capacity = 1
        self.__arr = DynamicArray.__make_array(self.__capacity)

    @property
    def capacity(self):
        return self.__capacity

    def __len__(self):
        return self.__size

    def __str__(self):
        return f"{[self.__arr[i] for i in range(self.__size)]}"

    def __setitem__(self, index_, item_):
        if not self.__is_valid_index(index_):
            raise IndexError("Index error")
        self.__arr[index_] = item_

    def __getitem__(self, index_):
        if not self.__is_valid_index(index_):
            raise IndexError("Index error")
        return self.__arr[index_]

    def __delitem__(self, index_):
        if not self.__is_valid_index(index_):
            raise IndexError("Index error")

        self.__decrease_size()

        for i in range(index_, self.__size - 1):
            self.__arr[i] = self.__arr[i + 1]

        self.__size -= 1

    def __contains__(self, item_):
        for i in range(self.__size):
            if self.__arr[i] == item_:
                return True
        return False

    def append(self, item_):
        self.__increase_size()

        self.__arr[self.__size] = item_
        self.__size += 1

    def insert(self, index_, item_):
        if not self.__is_valid_index(index_):
            raise IndexError("Index error")

        self.__increase_size()

        for i in range(self.__size - 1, index_ - 1, -1):
            self.__arr[i + 1] = self.__arr[i]

        self.__arr[index_] = item_
        self.__size += 1

    def remove(self, item_):
        index = self.search(item_)
        if index == -1:
            raise ElementNotFoundError(f"{item_} is not existed")
        self.remove_at(index)

    def remove_at(self, index_):
        self.__delitem__(index_)

    def pop(self):
        if self.is_empty():
            raise EmptyArrayError("Array is empty")

        self.__decrease_size()

        temp = self.__size
        self.__size -= 1
        return temp

    def clear(self):
        self.__size = 0
        self.__capacity = 1

    def search(self, item_):
        for i in range(self.__size):
            if self.__arr[i] == item_:
                return i
        return -1

    def is_empty(self):
        return self.__size == 0

    def __is_valid_index(self, index_):
        return 0 <= index_ < self.__size

    def __increase_size(self):
        if self.__size == self.__capacity:
            self.__resize(2 * self.__capacity)

    def __decrease_size(self):
        half_capacity = self.__capacity // 2
        if self.__size <= half_capacity:
            self.__resize(half_capacity)

    def __resize(self, new_capacity_):
        new_arr = DynamicArray.__make_array(new_capacity_)
        self.__capacity = new_capacity_

        for i in range(self.__size):
            new_arr[i] = self.__arr[i]

        self.__arr = new_arr


if __name__ == "__main__":
    arr = DynamicArray()
