from abc import ABC, abstractmethod


class Node:
    def __init__(self, data_):
        self.data = data_
        self.next = None


class LinkedListADT(ABC):
    @abstractmethod
    def __str__(self):
        """
        Print linked list
        """
        pass

    @abstractmethod
    def __setitem__(self, index_, item_):
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
    def contains(self, node_):
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


class SinglyLinkedList(LinkedListADT):
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Linked list is empty"

        current = self.head
        chain = ""
        while current:
            chain += str(current.data) + "->"
            current = current.next
        return chain

    def __setitem__(self, index_, item_):
        if index_ < 0 or index_ >= len(self):
            raise Exception("Index error")

        count = 0
        current = self.head
        while current:
            if count == index_:
                current.data = item_
            count += 1
            current = current.next

    def __getitem__(self, index_):
        if index_ < 0 or index_ >= len(self):
            raise Exception("Index error")

        count = 0
        current = self.head
        while current:
            if count == index_:
                return current.data
            count += 1
            current = current.next

    def __len__(self):
        if self.head is None:
            return 0

        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def push(self, node_):
        new_node = Node(node_)
        new_node.next = self.head
        self.head = new_node

    def append(self, node_):
        new_node = Node(node_)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def append_all(self, nodes_):
        for node in nodes_:
            self.append(node)

    def insert_at(self, index_, node_):
        if index_ < 0 or index_ >= len(self):
            raise Exception("Index error")

        if index_ == 0:
            self.push(node_)
            return

        count = 0
        current = self.head
        while current:
            if count == index_ - 1:
                new_node = Node(node_)
                new_node.next = current.next
                current.next = new_node
                break
            count += 1
            current = current.next

    def peek_first(self):
        if self.head is None:
            raise Exception("Linked list is empty")

        self.head = self.head.next

    def peek_last(self):
        if self.head is None:
            raise Exception("Linked list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def peek(self, node_):
        if self.head is None:
            raise Exception("Linked list is empty")

        if self.head.data == node_:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == node_:
                    current.next = current.next.next
                    break
                current = current.next
            else:
                raise Exception(f"{node_} is not existed")

    def peek_at(self, index_):
        if index_ < 0 or index_ >= len(self):
            raise Exception("Invalid index")

        if index_ == 0:
            self.head = self.head.next
            return

        count = 0
        current = self.head
        while current:
            if count == index_ - 1:
                current.next = current.next.next
                break
            current = current.next
            count += 1

    def search(self, node_):
        if self.head is Node:
            return -1

        count = 0
        current = self.head
        while current:
            if current.data == node_:
                return count
            count += 1
            current = current.next
        return -1

    def is_empty(self):
        return self.head is None

    def contains(self, node_):
        if self.head is None:
            return False

        current = self.head
        while current:
            if current.data == node_:
                return True
            current = current.next
        return False

    def clear(self):
        self.head = None


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.push(2)
    sll.push(3)
    print(sll)
    sll.append(4)
    print(sll)
    sll.append_all([7, 8, 9])
    print(sll)
    sll.insert_at(3, 100)
    print(sll)
    print(sll[3])
    sll[4] = 200
    print(sll)
    sll.peek_at(4)
    print(sll)
    sll.peek_first()
    print(sll)
    sll.peek_last()
    print(sll)
    sll.peek(8)
    print(sll)
    sll.clear()
    print(sll)
    print(len(sll))
