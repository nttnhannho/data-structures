# Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


if __name__ == "__main__":
    #  Counter: count the number of occurrences of an element in collection
    a = "aaaaabbbbccc"
    counter = Counter(a)
    print(counter)
    print(counter.keys())
    print(counter.values())
    print(counter.most_common(1)[0][0])
    print(list(counter.elements()))

    # namedtuple: define a lightweight class, for e.g, class Point has 2 properties x and y
    Point = namedtuple("Point", "x, y")
    pt = Point(1, -4)
    print(pt)
    print(pt.x)
    print(pt.y)

    # OrderedDict: dictionary which remember the order of items adding to it
    order_dict = OrderedDict()
    order_dict["a"] = 1
    order_dict["b"] = 2
    order_dict["c"] = 3
    order_dict["d"] = 4
    print(order_dict)

    # defaultdict: dictionary which will return the default value of passed type when accessing the key which
    # does not exist. E.g, return an empty list when accessing key "c", this key does not exist in the dictionary
    d = defaultdict(list)
    d["a"] = 1
    d["b"] = 2
    print(d)
    print(d["a"])
    print(d["b"])
    print(d["c"])

    # deque: double-ended queue, contains methods which support to add, delete, modify at both sides
    de = deque()
    de.append(1)
    de.append(2)
    print(de)
    de.appendleft(3)
    de.pop()
    print(de)
    de.extendleft([4, 5, 6])
    print(de)
    de.rotate(1)
    print(de)
    de.rotate(-1)
    print(de)
