from abc import ABC, abstractmethod


class StackADT(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def push(self, item_):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class Stack(StackADT):
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return f"{[item for item in self.__stack]}"

    def __len__(self):
        return len(self.__stack)

    def push(self, item_):
        self.__stack.append(item_)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0


if __name__ == "__main__":
    s = Stack()
