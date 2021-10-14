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

        half_capacity = int(self.__capacity / 2)
        if self.__is_size_le(half_capacity):
            self.__resize(half_capacity)

        for i in range(index_, self.__size - 1):
            self.__arr[i] = self.__arr[i + 1]

        self.__size -= 1

    def __contains__(self, item_):
        for i in range(self.__size):
            if self.__arr[i] == item_:
                return True
        return False

    def append(self, item_):
        if self.__is_size_equal(self.__capacity):
            self.__resize(2 * self.__capacity)

        self.__arr[self.__size] = item_
        self.__size += 1

    def insert(self, index_, item_):
        if not self.__is_valid_index(index_):
            raise IndexError("Index error")

        if self.__is_size_equal(self.__capacity):
            self.__resize(2 * self.__capacity)

        for i in range(self.__size - 1, index_ - 1, -1):
            self.__arr[i + 1] = self.__arr[i]

        self.__arr[index_] = item_
        self.__size += 1

    def remove(self, item_):
        half_capacity = int(self.__capacity / 2)
        if self.__is_size_le(half_capacity):
            self.__resize(half_capacity)

        for i in range(self.__size):
            if self.__arr[i] == item_:
                for j in range(i, self.__size - 1):
                    self.__arr[j] = self.__arr[j + 1]
                self.__size -= 1
                break
        else:
            raise Exception(f"{item_} is not existed")

    def remove_at(self, index_):
        self.__delitem__(index_)

    def pop(self):
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

    def __is_size_le(self, half_capacity):
        return self.__size <= half_capacity

    def __is_size_equal(self, half_capacity):
        return self.__size == half_capacity

    def __resize(self, new_capacity_):
        new_arr = DynamicArray.__make_array(new_capacity_)
        self.__capacity = new_capacity_

        for i in range(self.__size):
            new_arr[i] = self.__arr[i]

        self.__arr = new_arr


if __name__ == "__main__":
    arr = DynamicArray()
