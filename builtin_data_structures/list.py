# append
# clear
# copy
# count
# extend
# index
# insert
# pop
# remove
# reverse
# sort


if __name__ == "__main__":
    lst = [1, 2, 3, 1, 1, 2, 2]
    print(lst)
    lst.clear()  # Removes all the elements from the list => []
    print(lst)
    lst = [1, 2, 3, 1, 1, 2]
    temp = lst.copy()  # Returns a copy of the list => [1, 2, 3, 1, 1, 2]
    print(temp)
    print(lst.count(1))  # Returns the number of elements with the specified value => 3
    lst.extend([4, 4, 4])  # Add the elements of a list (or any iterable), to the end of the current list
    # => [1, 2, 3, 1, 1, 2, 4, 4, 4]
    print(lst)
    print(lst.index(3))  # Returns the index of the first element with the specified value => 2
    lst.insert(2, 1)  # Adds an element at the specified position => [1, 2, 1, 3, 1, 1, 2, 4, 4, 4]
    print(lst)
    lst.pop(2)  # Removes the element at the specified position => [1, 2, 3, 1, 1, 2, 4, 4, 4]
    print(lst)
    lst.remove(4)  # Removes the first item with the specified value => [1, 2, 3, 1, 1, 2, 4, 4]
    print(lst)
    lst.reverse()  # Reverses the order of the list => [4, 4, 2, 1, 1, 3, 2, 1]
    print(lst)
    lst.sort()  # Sorts the list => [1, 1, 1, 2, 2, 3, 4, 4]
    print(lst)
