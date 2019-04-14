#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# @file   greedy.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   14.04.2019
# =============================================================================
"""Implementation of greedy algorithms."""

from operator import itemgetter

from knapsack import Knapsack


class Greedy(Knapsack):
    """Greedy algorithm implementation."""

    def solve(self):
        """Solve greedy knapsac in a generic way."""
        value = 0
        weight = 0
        taken = [0] * self.n_items

        sorted_data = self.sort_data()

        for index, row in sorted_data.iterrows():
            if weight + row['weight'] <= self.capacity:
                taken[index] = 1
                value += row['value']
                weight += row['weight']

        return int(value), 0, taken

    def sort_data(self):
        """How should data be sorted to be greedy."""
        raise NotImplementedError


class GreedyValue(Greedy):
    """Take the most valuable items first."""

    def sort_data(self):
        """Solve taking items by value."""
        return self.items.sort_values(by=['value'], ascending=False)


class GreedySmall(Greedy):
    """Take smallest items first."""

    def sort_data(self):
        """Solve taking smallest items first."""
        return self.items.sort_values(by=['weight'])


class GreedyDensity(Greedy):
    """Take items with highest value density."""

    def sort_data(self):
        """Sort by value density."""
        self.items['density'] = self.items['value']/self.items['weight']
        return self.items.sort_values(by=['density'], ascending=False)


class GreedyBest(Knapsack):
    """Test all greedy algorithms and choose the best-performing one."""

    ALGOS = {'Value': GreedyValue,
             'SmallItems': GreedySmall,
             'ValueDensity': GreedyDensity}

    def __init__(self, input_data):
        """Initialize all algos."""
        self.algorithms = {name: algo(input_data) for name, algo in self.ALGOS.items()}

    def solve(self):
        """Run all greedy algorithms and choose the best."""
        results = {name: algo.solve() for name, algo in self.algorithms.items()}
        for name, res in results.items():
            print(name, res)
        return sorted(results.values(), key=itemgetter(0))[-1]


# EOF
