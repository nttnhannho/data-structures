from abc import ABC, abstractmethod


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
        self.__queue = []

    def __len__(self):
        return len(self.__queue)

    def __str__(self):
        return f"{[item for item in self.__queue]}"

    def enqueue(self, item_):
        self.__queue.append(item_)

    def dequeue(self):
        return self.__queue.pop(0)

    def peek(self):
        return self.__queue[0]

    def is_empty(self):
        return len(self.__queue) == 0


if __name__ == "__main__":
    q = Queue()
