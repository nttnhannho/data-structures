# add
# clear
# copy
# difference
# difference_update
# discard
# intersection
# intersection_update
# isdisjoint
# issubset
# issuperset
# pop
# remove
# symmetric_difference
# symmetric_difference_update
# update


if __name__ == "__main__":
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    set_a.add(10)  # Adds an element to the set => {1, 2, 3, 4, 5, 10}
    print(set_a)
    set_a.clear()  # Removes all the elements from the set => set()
    print(set_a)
    set_a = {1, 2, 3, 4, 5}
    temp = set_a.copy()  # Returns a copy of the set => {1, 2, 3, 4, 5}
    print(temp)
    print(set_a.difference(set_b))  # Returns a set containing the difference between two or more sets => {1, 2, 3}
    set_a = {1, 2, 3, 4, 5}
    set_a.difference_update(set_b)  # Removes the items in this set that are also included in another, specified set
    # => {1, 2, 3}
    print(set_a)
    set_a = {1, 2, 3, 4, 5}
    set_a.discard(1)  # Remove the specified item => {2, 3, 4, 5}
    print(set_a)
    print(set_a.intersection(set_b))  # Returns a set, that is the intersection of two or more sets => {4, 5}
    set_a.intersection_update(set_b)  # Removes the items in this set that are not present in other, specified set(s)
    # => {4, 5}
    print(set_a)
    set_a = {1, 2, 3}
    print(set_a.isdisjoint(set_b))  # Returns whether two sets have a intersection or not => True
    set_a = {4, 5}
    print(set_a.issubset(set_b))  # Returns whether another set contains this set or not => True
    print(set_b.issuperset(set_a))  # Returns whether this set contains another set or not => True
    set_a.pop()  # Removes an element from the set => {5}
    print(set_a)
    set_a = {1, 2, 3, 4, 5}
    set_a.remove(1)  # Removes the specified element => {2, 3, 4, 5}
    print(set_a)
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print(set_a.symmetric_difference(set_b))  # Returns a set with the symmetric differences of two sets
    # => {1, 2, 3, 6, 7, 8}
    set_a.symmetric_difference_update(set_b)  # Inserts the symmetric differences from this set and another
    # => {1, 2, 3, 6, 7, 8}
    print(set_a)
    print(set_a.union(set_b))  # Return a set containing the union of sets => {1, 2, 3, 4, 5, 6, 7, 8}
    set_a.update({100, 200, 300})  # Update the set with another set, or any other iterable
    # => {1, 2, 3, 100, 6, 7, 8, 200, 300}
    print(set_a)
