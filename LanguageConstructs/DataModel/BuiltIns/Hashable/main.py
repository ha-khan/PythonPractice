# set
# frozenset
# dict

def main():
    l = [1, 2]

    # immutable tuple datatype implements __hash__
    # and can be used as a dict key
    ll = (1, 2) 
    mp = dict()
    try:
        mp[l] = 12
    except:
        mp[ll] = 12

    pass

if __name__ == '__main__':
    main()