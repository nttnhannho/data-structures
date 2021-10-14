from abc import ABC, abstractmethod


class EmptyBSTError(Exception):
    def __init__(self, msg_):
        self.__msg = msg_

    def __str__(self):
        return f"{self.__msg}"


class NodeNotFoundError(Exception):
    def __init__(self, msg_):
        self.__msg = msg_

    def __str__(self):
        return f"{self.__msg}"


class BinarySearchTreeADT(ABC):
    @abstractmethod
    def search(self, data_):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def insert(self, data_):
        pass

    @abstractmethod
    def pre_order(self):
        pass

    @abstractmethod
    def in_order(self):
        pass

    @abstractmethod
    def post_order(self):
        pass

    @abstractmethod
    def remove(self, data_):
        pass

    @abstractmethod
    def get_min(self):
        pass

    @abstractmethod
    def get_max(self):
        pass


class BST(BinarySearchTreeADT):
    def __init__(self, data_):
        self.__data = data_
        self.__left = None
        self.__right = None

    def search(self, data_):
        if self.is_empty():
            raise EmptyBSTError("BST is empty")

        return self.__search(data_)

    def is_empty(self):
        return self.__data is None

    def insert(self, data_):
        if self.is_empty():
            self.__data = data_
            return

        if self.__data == data_:
            return

        if data_ < self.__data:
            if self.__left:
                self.__left.insert(data_)
            else:
                self.__left = BST(data_)
        else:
            if self.__right:
                self.__right.insert(data_)
            else:
                self.__right = BST(data_)

    def pre_order(self):
        elements = list()

        elements.append(self.__data)
        if self.__left:
            elements += self.__left.pre_order()
        if self.__right:
            elements += self.__right.pre_order()

        return elements

    def in_order(self):
        elements = []

        if self.__left:
            elements += self.__left.in_order()
        elements.append(self.__data)
        if self.__right:
            elements += self.__right.in_order()

        return elements

    def post_order(self):
        elements = []

        if self.__left:
            elements += self.__left.post_order()
        if self.__right:
            elements += self.__right.post_order()
        elements.append(self.__data)

        return elements

    def remove(self, data_):
        if self.is_empty():
            raise EmptyBSTError("BST is empty")

        self.__remove(data_)

    def get_min(self):
        if self.__left is None:
            return self.__data
        return self.__left.get_min()

    def get_max(self):
        if self.__right is None:
            return self.__data
        return self.__right.get_max()

    def __search(self, data_):
        if self.__data == data_:
            return True

        if data_ < self.__data:
            if self.__left:
                return self.__left.__search(data_)
            else:
                return False
        else:
            if self.__right:
                return self.__right.__search(data_)
            else:
                return False

    def __remove(self, data_):
        if data_ < self.__data:
            if self.__left:
                self.__left = self.__left.__remove(data_)
            else:
                raise NodeNotFoundError(f"{data_} is not existed")
        elif data_ > self.__data:
            if self.__right:
                self.__right = self.__right.__remove(data_)
            else:
                raise NodeNotFoundError(f"{data_} is not existed")
        else:
            if self.__left is None:
                temp = self.__right
                del self
                return temp
            if self.__right is None:
                temp = self.__left
                del self
                return temp

            node = self.__right
            while node.__left:
                node = node.__left
            self.__data = node.__data
            self.__right = self.__right.__remove(node.__data)

        return self


if __name__ == "__main__":
    root = BST(10)
