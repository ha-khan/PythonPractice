
class LongestPalindromicSubstring:
    """
        Longest Palindromic Substring is a Class that creates instances objects 
        that can compute whether a given str has a substr that is palindromic, and
        if yes, then it will compute what the longest substr in the str 

        Fun fact, the set of all languages that are palindromic are not regular
        meaning no DFA exists that accepts palindromic strings and since no DFA, 
        then no regular expression, which would use used to match substr within a str 
    """
    def __init__(self, input: str) -> None:
        import math

        self.input = input
        self.longest = 0
        self.math = math

    def compute_slow_iteration(self) -> int:
        """
            Brute-Force approach of checking all possible substrings from the given string
            a lot of work is duplicated, so this approach is very suboptimal, and will not scale well
        """
        for idx, _ in enumerate(self.input):
            for idy in range(idx, len(self.input)+1):
                if self.is_palindromic(self.input[idx:idy]):
                    if len(self.input[idx:idy]) > self.longest:
                        self.longest = len(self.input[idx:idy])
        return self.longest

    def compute_slow_recursion(self) -> int:
        """
            Recursively "iterate"
            Brute-Force approach of checking all possible substrings from the given string
            a lot of work is duplicate,  
        """
        size = len(self.input)
        def recurse(left_ptr: int, right_ptr: int):
            if left_ptr > size or right_ptr > size:
                return
            
            if self.is_palindromic(self.input[left_ptr:right_ptr]):
                if len(self.input[left_ptr:right_ptr]) > self.longest:
                    self.longest = len(self.input[left_ptr:right_ptr])

            # recurse right_ptr quickly 
            recurse(left_ptr, right_ptr + 1)
            recurse(left_ptr + 1, right_ptr + 1)
        recurse(0, 1)    
        return self.longest

    def compute_fast_memory(self) -> int:
        return 0

    def compute_fast_no_memory(self) -> int:
        return 0 

    def is_palindromic(self, input: str) -> bool:
        """
            computes whether a given string input is palindromic
        """
        size = len(input)
        if size % 2 == 0:
            substr = int(size/ 2)
            return input[:substr] == input[substr:size+1][::-1]
        
        mid = self.math.floor(size/2)
        return input[:mid] == input[mid+1:][::-1]


def main():
    print("Running Main")
    l = LongestPalindromicSubstring("bcab")
    #print(l.compute_slow_iteration())
    print(l.is_palindromic("bcab"))
    # print(l.compute_slow_recursion())


if __name__ == '__main__':
    main()

