
def main():
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for idx, rune in enumerate(l):
        print(f'idx: {idx}, rune: {rune}')

    ll = [y for y in map(lambda x: x*2, l)]
    print(ll)

    lll = [z for z in filter(lambda x: x in ['aa', 'cc', 'ee', 'gg'], ll)]
    print(lll)

    l.append('h')
    llll = [a for a in zip(l, ll)]
    print(llll)

if __name__ == '__main__':
    main()
