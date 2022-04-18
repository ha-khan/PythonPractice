# set
# frozenset
# dict

def main():
    l = [1, 2]

    # immutable sequence instances implements __hash__
    # and can be used in dict, set, frozenset 
    ll = (1, 2) 
    mp = dict()
    try:
        mp[l] = 12
    except:
        mp[ll] = 12

    pass

if __name__ == '__main__':
    main()