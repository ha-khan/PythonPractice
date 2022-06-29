from sys import stdin, stderr, stdout 


def main():

    with open('logs.txt') as l:
        for line in l:
            stdout.write(line)
            ## will insert a newline \n, logs already have a \n
            # print(line)

    buffer = "" 
    for rune in input():
        buffer += rune
    print(buffer)

    for runes in stdin:
        if runes.strip('\n') == 'quit':
            break
        stdout.write(runes)

if __name__ == '__main__':
    main()
