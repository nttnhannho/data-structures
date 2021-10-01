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
    def contains(self, item_):
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

    def contains(self, item_):
        for i in range(self.__n):
            if self.__arr[i] == item_:
                return True
        return False


if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(f"len: {len(arr)}")
    print(f"arr: {arr}")
    print(arr.is_empty())

    print(f"arr[0]: {arr[0]}")
    print(f"arr[1]: {arr[1]}")
    print(f"arr[2]: {arr[2]}")

    arr[0] = 200
    print(arr)

    arr.insert(1, 100)
    print(f"len: {len(arr)}")
    print(f"arr: {arr}")

    del arr[1]
    print(f"del arr[1]: {arr}")

    arr.remove(3)
    print(f"arr.remove(3): {arr}")

    print(f"arr.pop(): {arr.pop()}")
    print(f"array after pop: {arr}")

    print(f"arr.search(2): {arr.search(2)}")
    print(f"arr.search(100): {arr.search(100)}")

    print(f"arr.contains(2): {arr.contains(2)}")
    print(f"arr.contains(100): {arr.contains(100)}")

    arr.clear()
    print(f"array after clear: {arr}")
    print(arr.is_empty())
