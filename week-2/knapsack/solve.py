#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# @file   solve.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   13.04.2019
# =============================================================================
"""Solver."""

from operator import itemgetter

import pandas as pd


class Knapsack:
    def init(self, input_data):
        with open(input_data, 'r') as f_:
            first_line = f_.readline().rstrip('\n')
        self.item_count, self.capacity = map(int, first_line.split())
        self.data = pd.read_table(input_data, sep=' ',
                                  names=['value', 'weight'],
                                  skiprows=1)
        return self

    def solve(self):
        raise NotImplementedError


class Greedy(Knapsack):
    """Greedy algorithm implementation."""
    def solve(self):
        value = 0
        weight = 0
        taken = [0]*self.item_count

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
        return self.data.sort_values(by=['value'], ascending=False)


class GreedySmall(Greedy):
    """Take smallest items first."""

    def sort_data(self):
        """Solve taking smallest items first."""
        return self.data.sort_values(by=['weight'])


class GreedyDensity(Greedy):
    """Take items with highest value density."""

    def sort_data(self):
        """Sort by value density."""
        self.data['density'] = self.data['value']/self.data['weight']
        return self.data.sort_values(by=['density'], ascending=False)


class GreedyBest(Knapsack):
    """Test all greedy algorithms and choose the best-performing one."""

    ALGOS = {'Value': GreedyValue,
             'SmallItems': GreedySmall,
             'ValueDensity': GreedyDensity}

    def init(self, input_data):
        """Initialize all algos."""
        self.algorithms = {name: algo().init(input_data) for name, algo in self.ALGOS.items()}
        return self

    def solve(self):
        """Run all greedy algorithms and choose the best."""
        results = {name: algo.solve() for name, algo in self.algorithms.items()}
        for name, res in results.items():
            print(name, res)
        return sorted(results.values(), key=itemgetter(0))[-1]


def get_solver(input_data):
    """Get the most appropriate solver for each input data."""
    return GreedyBest().init(input_data)


# EOF
