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
    def __getitem__(self, index_):
        """
        Fetch an item by index
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
        Remove an item
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
        Search index of an item
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

    def __getitem__(self, index_):
        if index_ < 0 or index_ > self.__n:
            return "IndexError"
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
            return "IndexError"
        if self.__n == self.__size:
            self.__resize(2 * self.__size)
        for i in range(self.__n - 1, index_ - 1, -1):
            self.__arr[i + 1] = self.__arr[i]
        self.__arr[index_] = item_
        self.__n += 1

    def __delitem__(self, index_):
        if self.__n <= (self.__size / 2):
            self.__resize(self.__size / 2)

        if self.__n > index_:
            if index_ < 0:
                for i in range(index_ + self.__n, self.__n - 1):
                    self.__arr[i] = self.__arr[i + 1]
                self.__n -= 1
            else:
                for i in range(index_, self.__n - 1):
                    self.__arr[i] = self.__arr[i + 1]
                self.__n -= 1
        else:
            print("IndexError")

    def remove(self, item_):
        for i in range(self.__n):
            if self.__arr[i] == item_:
                for j in range(i, self.__n - 1):
                    self.__arr[j] = self.__arr[j + 1]
                self.__n -= 1
                break
        else:
            print("Not Found")
            return -1

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
        else:
            print("Not Found")
            return -1


if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(f"len: {len(arr)}")
    print(f"arr: {arr}")

    print(f"arr[0]: {arr[0]}")
    print(f"arr[1]: {arr[1]}")
    print(f"arr[2]: {arr[2]}")

    arr.insert(1, 100)
    print(f"len: {len(arr)}")
    print(f"arr: {arr}")

    del arr[1]
    print(f"del arr[1]: {arr}")
    print(f"del arr[100]:")
    del arr[100]

    arr.remove(1)
    print(f"arr.remove(1): {arr}")
    print("arr.remove(100):")
    arr.remove(100)

    print(f"arr.pop(): {arr.pop()}")
    print(f"array after pop: {arr}")

    print(f"arr.search(2): {arr.search(2)}")
    print(f"arr.search(100): {arr.search(100)}")

    arr.clear()
    print(f"array after clear: {arr}")