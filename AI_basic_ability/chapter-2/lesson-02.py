"""
Cutting Problem
how to cut the timber, we can get the max-prices?

All the dynamic programming:
1. sub-problems
2. Overlapping sub-problems
3. parse solution
"""

from collections import defaultdict
from functools import lru_cache
# least recent used

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]
complete_price = defaultdict(int)
for i, p in enumerate(prices): complete_price[i+1] = p

solution = {}

cache = {}
#<- if when n .... is huge. size(cache)
# keep most important information.


@lru_cache(maxsize=2**10)
def r(n):
    # a very classical dynamic programming problem
    # if n in cache: return cache[n]

    candidates = [(complete_price[n], (n, 0))] + \
                 [(r(i) + r(n-i), (i, n - i)) for i in range(1, n)]

    print(candidates)
    print()

    optimal_price, split = max(candidates)

    solution[n] = split

    # cache[n] = optimal_price

    return optimal_price


def parse_solution(n, cut_solution):
    left, right = cut_solution[n]

    if left == 0 or right == 0: return [left+right, ]
    else:
        return parse_solution(left, cut_solution) + parse_solution(right, cut_solution)


if __name__ == '__main__':
    print(r(19))
    print(solution)
    print(parse_solution(19, solution))