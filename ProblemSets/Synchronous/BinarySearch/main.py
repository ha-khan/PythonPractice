from typing import List
import logging
from logging import DEBUG, INFO
from math import ceil, floor


class solution:
    def __init__(self, l: List, precision_func=floor, log_level=DEBUG):
        self.n = l
        logging.getLogger().setLevel(log_level)
        self.precision_func = precision_func

    def find(self, num: int) -> bool:
        low = 0
        high = len(self.n) - 1

        # low, high will change so we create a
        # conditional loop on the constraint that low < high always
        while low <= high:
            midpoint = self.precision_func((low + high) / 2)
            logging.debug(f'midpoint: {midpoint}, low: {low}, high: {high}')
            if self.n[midpoint] > num:
                high = midpoint - 1
            elif self.n[midpoint] < num:
                low = midpoint  + 1
            else:
                return True
        return False

def main():
    s = solution([x for x in range(15)], ceil, INFO)
    print(s.find(14))

if __name__ == '__main__':
    main()
