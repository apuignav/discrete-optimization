#!/usr/bin/python
# -*- coding: utf-8 -*-

from operator import itemgetter

from knapsack import Knapsack, KnapsackError

from greedy import GreedyBest
from dp import DynamicProgramming


class Best(Knapsack):
    """Test all algorithms and choose the best-performing one."""

    ALGOS = {'Greedy': GreedyBest,
             'DP': DynamicProgramming}

    def __init__(self, input_data):
        """Initialize all algos."""
        self.algorithms = {name: algo(input_data) for name, algo in self.ALGOS.items()}

    def solve(self):
        """Run all greedy algorithms and choose the best."""
        results = {}
        for name, algo in self.algorithms.items():
            try:
                results[name] = algo.solve()
                print(f"{name} -> {results[name]}")
            except KnapsackError:
                print(f"Couldn't use algo {name}")
        return sorted(results.values(), key=itemgetter(0))[-1]


def get_solver(input_data):
    """Get the most appropriate solver for each input data."""
    return Best(input_data)


def solve_it(input_data):
    solver = get_solver(input_data)
    value, is_optimal, taken = solver.solve()

    # prepare the solution in the specified output format
    output_data = f'{value} {is_optimal}\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        print(solve_it(file_location))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

