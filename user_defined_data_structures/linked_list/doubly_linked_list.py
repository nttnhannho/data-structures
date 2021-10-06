from abc import ABC, abstractmethod


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
    def __contains__(self, node_):
        """
        Check if linked list contains given node
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
        self.__check_empty()
        self.__check_valid_index(index_)

        index = 0
        current = self.__head
        while current:
            if index == index_:
                current.data = node_
            index += 1
            current = current.next

    def __getitem__(self, index_):
        self.__check_empty()
        self.__check_valid_index(index_)

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
        self.__check_empty()

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
            raise Exception(f"{target_node_} is not existed")

    def add_before(self, node_, target_node_):
        self.__check_empty()

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
            raise Exception(f"{target_node_} is not existed")

    def insert_at(self, index_, node_):
        self.__check_empty()
        self.__check_valid_index(index_)

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
        self.__check_empty()

        if self.__head.next is None:
            self.__head = None
            return

        self.__head = self.__head.next
        self.__head.prev = None

    def peek_last(self):
        self.__check_empty()

        if self.__head.next is None:
            self.__head = None
            return

        current = self.__head
        while current.next:
            current = current.next
        current.prev.next = None

    def peek(self, node_):
        self.__check_empty()

        if self.__head.next is None:
            if self.__head.data == node_:
                self.__head = None
                return
            else:
                raise Exception(f"{node_} is not existed")

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
                raise Exception(f"{node_} is not existed")

    def peek_at(self, index_):
        self.__check_empty()
        self.__check_valid_index(index_)

        if index_ == 0:
            self.peek_first()
            return

        if index_ == len(self) - 1:
            self.peek_last()
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
        self.__check_empty()

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

    def __contains__(self, node_):
        self.__check_empty()

        current = self.__head
        while current:
            if current.data == node_:
                return True
            current = current.next
        return False

    def clear(self):
        self.__head = None

    def from_backward(self):
        self.__check_empty()

        chain = ""
        current = self.__head
        while current.next:
            current = current.next
        while current:
            chain += str(current.data) + "->"
            current = current.prev
        return chain

    def __check_valid_index(self, index_):
        if index_ < 0 or index_ >= len(self):
            raise Exception("Index error")

    def __check_empty(self):
        if self.__head is None:
            raise Exception("Linked list is empty")


if __name__ == "__main__":
    dll = DoublyLinkedList()
