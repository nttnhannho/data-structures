class Node:
    def __init__(self, data_=None, next_=None):
        self.data = data_
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data_):
        node = Node(data_, self.head)
        self.head = node

    def insert_at_end(self, data_):
        if self.head is None:
            self.head = Node(data_, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data_, None)

    def insert_values(self, data_list_):
        self.head = None
        for data in data_list_:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index_):
        if index_ < 0 or index_ >= self.get_length():
            raise Exception("Invalid index")

        if index_ == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index_ - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index_, data_):
        if index_ < 0 or index_ >= self.get_length():
            raise Exception("Invalid index")

        if index_ == 0:
            self.insert_at_beginning(data_)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index_ - 1:
                node = Node(data_, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked list in empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(79)
    # ll.insert_at_end(1)
    # ll.insert_at_end(9876)
    ll.insert_values([1, 2, 3, 4, 5])
    print(ll.get_length())
    ll.remove_at(2)
    print(ll.get_length())
    ll.print()
    ll.insert_at(0, -1)
    ll.insert_at(4, 10)
    ll.print()
