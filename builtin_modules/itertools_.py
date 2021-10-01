# product, permutations, combinations, accumulate, groupby, count, cycle, repeat, zip_longest
# starmap, chain, islice, compress, filterfalse, dropwhile, takewhile, tee
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, \
    groupby, count, cycle, repeat, zip_longest, starmap, chain, islice, compress, filterfalse, dropwhile, \
    takewhile, tee
import operator


def smaller_than_3(input_):
    return input_ < 3


if __name__ == "__main__":
    # product
    a = [1, 2]
    b = [3, 4]
    b2 = [3]
    prod = product(a, b)
    print(list(prod))
    prod2 = product(a, b2, repeat=2)
    print(list(prod2))

    # permutations
    p = [1, 2, 3, 4]
    per = permutations(p)
    print(list(per))
    per2 = permutations(p, 2)
    print(list(per2))

    # combinations
    c = [1, 2, 3, 4]
    comb = combinations(c, 2)
    print(list(comb))
    comb_wr = combinations_with_replacement(c, 2)
    print(list(comb_wr))

    # accumulate
    ac = [1, 2, 5, 3, 4]
    accum = accumulate(ac)
    print(list(accum))
    accum2 = accumulate(ac, func=max)
    print(list(accum2))
    accum3 = accumulate(ac, func=operator.mul)
    print(list(accum3))

    # groupby
    gb = [1, 2, 3, 4]
    group_obj = groupby(gb, key=smaller_than_3)
    for k, v in group_obj:
        print(k, list(v))

    # count
    for i in count(10):
        print(i)
        if i == 15:
            break
    data = [100, 200, 300]
    print(list(zip(count(), data)))

    # cycle
    cyc = [1, 2, 3]
    for i in cycle(cyc):
        print(i)

    # repeat
    for i in repeat(1):
        print(i)
    for i in repeat(1, 4):
        print(i)

    # zip_longest
    data = [100, 200, 300, 400]
    daily_data = list(zip_longest(range(10), data))
    print(daily_data)

    # starmap
    squares = starmap(pow, [(0, 2), (1, 2), (2, 2)])
    print(list(squares))

    # chain
    letters = ["a", "b", "c", "d"]
    numbers = [1, 2, 3, 4]
    chained = chain(letters, numbers)
    print(list(chained))

    # islice
    result = islice(range(10), 1, 5)
    print(list(result))

    # compress
    letters = ["a", "b", "c", "d"]
    selectors = [True, True, False, True]
    res = compress(letters, selectors)
    print(list(res))

    # filterfalse
    numbers = [1, 2, 3, 4]
    res = filterfalse(lambda x: x % 2 == 0, numbers)
    print(list(res))

    # dropwhile
    numbers = [0, 1, 2, 3, 4, 1, 2]
    res = dropwhile(lambda x: x <= 2, numbers)
    print(list(res))

    # takewhile
    numbers = [0, 1, 5, 2, 3, 4, 1, 2]
    res = takewhile(lambda x: x <= 2, numbers)
    print(list(res))

    # tee
    numbers = [0, 1, 5, 2, 3, 4, 1, 2]
    iterator = tee(numbers, 2)
    for itr in iterator:
        print(list(itr))
