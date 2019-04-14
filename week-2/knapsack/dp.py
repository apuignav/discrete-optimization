#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# @file   dp.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   14.04.2019
# =============================================================================
"""Dynamic programming."""

import numpy as np

from knapsack import Knapsack, KnapsackError


class DynamicProgramming(Knapsack):
    """Apply dynamic programming to Knapsack problem."""

    def __init__(self, input_data, max_items=100):
        super().__init__(input_data)
        self.items['item_num'] = range(1, self.n_items + 1)
        self.items = self.items.set_index('item_num')
        self.table = np.empty((self.capacity+1, self.n_items+1))
        self.table.fill(np.nan)
        self.table[:, 0] = 0
        self.too_many_items = (self.capacity * self.n_items) > max_items

    def optimal_value(self, k, j):
        if np.isnan(self.table[k][j]):
            if self.items.loc[j]['weight'] <= k:
                self.table[k][j] = max(self.optimal_value(k, j-1),
                                       self.items.loc[j]['value'] + self.optimal_value(k-self.items.loc[j]['weight'], j-1))
            else:
                self.table[k][j] = self.optimal_value(k, j-1)
        return self.table[k][j]

    def solve(self):
        """Build table, solve."""
        if self.too_many_items:
            raise KnapsackError("Exceeded max number of items for DP -> {}"
                                .format(self.capacity * self.n_items))
        optimal_value = self.optimal_value(self.capacity, self.n_items)
        k = self.capacity
        j = self.n_items - 1
        val = optimal_value
        taken = [0] * self.n_items
        while j > 0:
            new_val = self.optimal_value(k, j-1)
            if new_val != val:
                k =- self.items.loc[j]['weight']
                taken[j] = 1
            val = new_val
            j =- 1
        return int(optimal_value), 1, taken


# EOF
