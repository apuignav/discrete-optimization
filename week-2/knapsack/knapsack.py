#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# @file   knapsack.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   13.04.2019
# =============================================================================
"""Base Knapsack class."""

import pandas as pd


class Knapsack:
    def __init__(self, input_data):
        with open(input_data, 'r') as f_:
            first_line = f_.readline().rstrip('\n')
        self.n_items, self.capacity = map(int, first_line.split())
        self.items = pd.read_table(input_data, sep=' ',
                                   names=['value', 'weight'],
                                   skiprows=1)

    def solve(self):
        raise NotImplementedError


class KnapsackError(Exception):
    """Knapsack error."""



# EOF
