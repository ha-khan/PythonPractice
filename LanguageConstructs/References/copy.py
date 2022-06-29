
def main():

    l1 = [1, 2, 3, 4, [5, 6]]

    # creates deep copy, values are same but unique objs
    l2 = list(l1)
    assert l1 == l2
    assert l1 is not l2

    # creates a shallow copy, references are shared between both
    # saves memory, but issue around mutable objs
    l3 = l1[:]
    assert l3 == l1
    l3[4].append(7)
    assert l3 == l1
    assert l3 is not l1

    # a deep copy may be too deep in some cases. For example, objects may refer to
    # external resources or singletons that should not be copied. You can control the behavior
    # of both copy and deepcopy by implementing the __copy__() and __deepcopy__()
    # https://docs.python.org/3/library/copy.html


if __name__ == '__main__':
    main()