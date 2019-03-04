'''
Given an array of numbers. Print all unique pairs with equal sum.

Output of the code below:
1 2 3 1 4
Pair(s) having a sum of 2: [(1, 1)]
Pair(s) having a sum of 3: [(1, 2), (2, 1)]
Pair(s) having a sum of 4: [(1, 3), (3, 1)]
Pair(s) having a sum of 5: [(1, 4), (2, 3)]
Pair(s) having a sum of 6: [(2, 4)]
Pair(s) having a sum of 7: [(3, 4)]
'''

from itertools import combinations

array = [int(i) for i in input().split()]

# Map of pair and its sum
pair_sum = {pair: sum(pair) for pair in combinations(array, 2)}

# Set of all unique sums possible
sum_set = set(pair_sum.values())

for sum in sum_set:
    print(f'Pair(s) having a sum of {sum}:', 
        [pair for pair, value in pair_sum.items() if value == sum])
