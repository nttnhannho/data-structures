from abc import ABC, abstractmethod
from user_defined_data_structures.linked_list.singly_linked_list import SinglyLinkedList


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
        self.__stack = SinglyLinkedList()

    def __str__(self):
        return f"[{', '.join(str(self.__stack).strip('->').split('->'))}]"

    def __len__(self):
        return len(self.__stack)

    def push(self, item_):
        self.__stack.append(item_)

    def pop(self):
        self.__stack.peek_last()

    def peek(self):
        return self.__stack[len(self.__stack) - 1]

    def is_empty(self):
        return len(self.__stack) == 0


if __name__ == "__main__":
    s = Stack()
