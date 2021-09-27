# clear
# copy
# fromkeys
# get
# items
# keys
# pop
# popitem
# setdefault
# update
# values


if __name__ == "__main__":
    dictionary = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    dictionary.clear()  # Removes all the elements from the dictionary => {}
    print(dictionary)
    dictionary = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    temp = dictionary.copy()  # Returns a copy of the dictionary => {'a': 1, 'b': 2, 'c': 3}
    print(temp)
    x = ("a", "b", "c")
    y = 0
    print(dict.fromkeys(x, y))  # Returns a dictionary with the specified keys and value => {'a': 0, 'b': 0, 'c': 0}
    print(dictionary.get("a"))  # Returns the value of the specified key => 1
    print(dictionary.items())  # Returns a list containing a tuple for each key value pair
    # => dict_items([('a', 1), ('b', 2), ('c', 3)])
    print(dictionary.keys())  # Returns a list containing the dictionary's keys => dict_keys(['a', 'b', 'c'])
    dictionary.pop("a")  # Removes the element with the specified key => {'b': 2, 'c': 3}
    print(dictionary)
    dictionary.popitem()  # Removes the last inserted key-value pair => {'b': 2}
    print(dictionary)
    dictionary.setdefault("d", 4)  # Returns the value of the specified key.
    # If the key does not exist: insert the key, with the specified value => {'b': 2, 'd': 4}
    print(dictionary)
    dictionary.update({"z": 100})  # Updates the dictionary with the specified key-value pairs
    # => {'b': 2, 'd': 4, 'z': 100}
    print(dictionary)
    print(dictionary.values())  # Returns a list of all the values in the dictionary => dict_values([2, 4, 100])
