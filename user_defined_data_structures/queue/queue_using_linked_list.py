from abc import ABC, abstractmethod
from user_defined_data_structures.linked_list.singly_linked_list import SinglyLinkedList


class QueueADT(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def enqueue(self, item_):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class Queue(QueueADT):
    def __init__(self):
        self.__queue = SinglyLinkedList()

    def __len__(self):
        return len(self.__queue)

    def __str__(self):
        return f"[{', '.join(str(self.__queue).strip('->').split('->'))}]"

    def enqueue(self, item_):
        self.__queue.append(item_)

    def dequeue(self):
        self.__queue.peek_first()

    def peek(self):
        return self.__queue[0]

    def is_empty(self):
        return len(self.__queue) == 0


if __name__ == "__main__":
    q = Queue()
