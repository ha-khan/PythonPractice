from logging import DEBUG, INFO
import logging 

class ContainsSubString:
    def __init__(self, s: str, log_level=INFO):
        self.string = s
        logging.getLogger().setLevel(log_level)

    def __call__(self, substring: str) -> bool:
        """
            Solution is to use two pointers/iterators.

            One moves across the "parent" string

            If we find a rune/char that matches the 0th index of the substring, 
            we create another pointer/iterator that checks each rune/char in the substring

            and compares it with whatever value is given by the outer pointer's index

            time ~ O(n) ~ where n = len(s)
            space ~ O(1) ~ ignoring space taken up by s, and substring we only allocate two ref for the pointers
        """
        string_cursor = 0
        while string_cursor < len(self.string):
            if self.string[string_cursor] == substring[0]:
                substring_cursor = 0
                while substring_cursor < len(substring):
                    try:
                        rune_from_string = self.string[string_cursor]
                    except IndexError:
                        logging.debug(f'Reached end of string {self.string}!')
                        return False
                    if substring[substring_cursor] != rune_from_string:
                        string_cursor += 1
                        break
                    substring_cursor +=1
                    string_cursor +=1
                else:
                    logging.info(f'Found substring: {substring}, in string: {self.string}')
                    return True
            string_cursor += 1
        logging.debug(f'Unable to find substring: {substring}, in string: {self.string}')
        return False


def main():
    c = ContainsSubString('hello world! how are you, hello dude!', DEBUG)
    assert c('hello dude?') 


if __name__ == '__main__':
    main()
