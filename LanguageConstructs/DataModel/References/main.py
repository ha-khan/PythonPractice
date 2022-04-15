
# variable declaration at module level scope, global
state = 'NONE'

def modify_state():
    global state
    state = 'STARTING'

def main():
    global state 

    modify_state()
    print(state)

    # "references" or alias for state
    state_2 = state

    # calls __eq__() .. compares value
    assert state_2 == state 

    # compares 'identity' 
    # CPython that implies memory location
    assert state_2 is state
    print(id(state_2))
    print(id(state))

    # reassign state_2 to a new string value, (not in place change)
    # as strings are immutable in python
    state_2 = 'STOPPING'

    assert state_2 != state
    assert state_2 is not state

    # Both reference the same dict() object by ref
    # which is mutable
    val_1 = {}
    val_2 = val_1
    val_2[1] = 2
    print(val_1 == val_2)
    print(val_1 is val_2)

    # removing all references to the underlying dict() 
    # object will allow the GC to free the allocated memory
    del val_1
    del val_2



if __name__ == '__main__':
    main()
