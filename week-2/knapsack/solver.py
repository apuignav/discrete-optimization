#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

from solve import get_solver

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

