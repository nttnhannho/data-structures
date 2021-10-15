from abc import ABC, abstractmethod


class EmptyLinkedListError(Exception):
    def __init__(self, msg_):
        self.__msg = msg_

    def __str__(self):
        return f"{self.__msg}"


class NodeNotFoundError(Exception):
    def __init__(self, msg_):
        self.__msg = msg_

    def __str__(self):
        return f"{self.__msg}"


class Node:
    def __init__(self, data_):
        self.data = data_
        self.next = None
        self.prev = None


class LinkedListADT(ABC):
    @abstractmethod
    def __str__(self):
        """
        Print linked list
        """
        pass

    @abstractmethod
    def __setitem__(self, index_, node_):
        """
        Set node by index
        """
        pass

    @abstractmethod
    def __getitem__(self, index_):
        """
        Fetch node by index
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        Length of linked list
        """
        pass

    @abstractmethod
    def __contains__(self, node_):
        """
        Check if linked list contains given node
        """
        pass

    @abstractmethod
    def push(self, node_):
        """
        Push node to first
        """
        pass

    @abstractmethod
    def append(self, node_):
        """
        Append node to last
        """
        pass

    @abstractmethod
    def append_all(self, nodes_):
        """
        Append list of nodes to last
        """
        pass

    @abstractmethod
    def add_after(self, node_, target_node_):
        """
        Add node after target node
        """
        pass

    @abstractmethod
    def add_before(self, node_, target_node_):
        """
        Add node before target node
        """
        pass

    @abstractmethod
    def insert_at(self, index_, node_):
        """
        Insert node at index
        """
        pass

    @abstractmethod
    def peek_first(self):
        """
        Peek first node
        """
        pass

    @abstractmethod
    def peek_last(self):
        """
        Peek last node
        """
        pass

    @abstractmethod
    def peek(self, node_):
        """
        Peek node
        """
        pass

    @abstractmethod
    def peek_at(self, index_):
        """
        Peek node at index
        """
        pass

    @abstractmethod
    def search(self, node_):
        """
        Search index of node
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Check if linked list is empty
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear linked list
        """
        pass

    @abstractmethod
    def from_backward(self):
        """
        Print the linked list from backward
        """
        pass


class DoublyLinkedList(LinkedListADT):
    def __init__(self):
        self.__head = None

    def __str__(self):
        chain = ""
        current = self.__head
        while current:
            chain += str(current.data) + "->"
            current = current.next
        return chain

    def __setitem__(self, index_, node_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        if not self.__is_valid_index(index_):
            raise IndexError("Index error")

        index = 0
        current = self.__head
        while current:
            if index == index_:
                current.data = node_
            index += 1
            current = current.next

    def __getitem__(self, index_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        if not self.__is_valid_index(index_):
            raise IndexError("Index error")

        index = 0
        current = self.__head
        while current:
            if index == index_:
                return current.data
            index += 1
            current = current.next

    def __len__(self):
        if self.__head is None:
            return 0

        count = 0
        current = self.__head
        while current:
            count += 1
            current = current.next
        return count

    def __contains__(self, node_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        current = self.__head
        while current:
            if current.data == node_:
                return True
            current = current.next
        return False

    def push(self, node_):
        new_node = Node(node_)

        if self.__head is None:
            self.__head = new_node
            return

        new_node.next = self.__head
        self.__head.prev = new_node
        self.__head = new_node

    def append(self, node_):
        new_node = Node(node_)

        if self.__head is None:
            self.__head = new_node
            return

        current = self.__head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def append_all(self, nodes_):
        for node in nodes_:
            self.append(node)

    def add_after(self, node_, target_node_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        current = self.__head
        while current:
            if current.data == target_node_:
                new_node = Node(node_)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                break
            current = current.next
        else:
            raise NodeNotFoundError(f"{target_node_} is not existed")

    def add_before(self, node_, target_node_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        current = self.__head
        while current:
            if current.data == target_node_:
                new_node = Node(node_)
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.__head = new_node
                current.prev = new_node
                break
            current = current.next
        else:
            raise NodeNotFoundError(f"{target_node_} is not existed")

    def insert_at(self, index_, node_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        if not self.__is_valid_index(index_):
            raise IndexError("Index error")

        if index_ == 0:
            self.push(node_)
            return

        index = 0
        current = self.__head
        while current:
            if index == index_ - 1:
                new_node = Node(node_)
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                break
            index += 1
            current = current.next

    def peek_first(self):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        self.__peek_node_at_first()

    def peek_last(self):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        if self.__head.next is None:
            self.__head = None
            return

        current = self.__head
        while current.next:
            current = current.next
        current.prev.next = None

    def peek(self, node_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        if self.__head.next is None:
            if self.__head.data == node_:
                self.__head = None
                return
            else:
                raise NodeNotFoundError(f"{node_} is not existed")

        if self.__head.data == node_:
            self.__head = self.__head.next
            self.__head.prev = None
            return

        current = self.__head
        while current.next:
            if current.data == node_:
                current.next.prev = current.prev
                current.prev.next = current.next
                break
            current = current.next
        else:
            if current.data == node_:
                current.prev.next = None
            else:
                raise NodeNotFoundError(f"{node_} is not existed")

    def peek_at(self, index_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        if not self.__is_valid_index(index_):
            raise IndexError("Index error")

        if index_ == 0:
            self.__peek_node_at_first()
            return

        if index_ == len(self) - 1:
            self.__peek_node_at_last()
            return

        index = 0
        current = self.__head
        while current.next:
            if index == index_:
                current.next.prev = current.prev
                current.prev.next = current.next
            index += 1
            current = current.next

    def search(self, node_):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        index = 0
        current = self.__head
        while current:
            if current.data == node_:
                return index
            index += 1
            current = current.next
        return -1

    def is_empty(self):
        return self.__head is None

    def clear(self):
        self.__head = None

    def from_backward(self):
        if self.is_empty():
            raise EmptyLinkedListError("Linked list is empty")

        chain = ""
        current = self.__head
        while current.next:
            current = current.next
        while current:
            chain += str(current.data) + "->"
            current = current.prev
        return chain

    def __is_valid_index(self, index_):
        return 0 <= index_ < len(self)

    def __peek_node_at_first(self):
        if self.__head.next is None:
            self.__head = None
            return

        self.__head = self.__head.next
        self.__head.prev = None

    def __peek_node_at_last(self):
        if self.__head.next is None:
            self.__head = None
            return

        current = self.__head
        while current.next:
            current = current.next
        current.prev.next = None


if __name__ == "__main__":
    dll = DoublyLinkedList()
