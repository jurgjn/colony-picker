#!/usr/bin/env python

import itertools, string

# Dimensions from: https://www.perkinelmer.com/uk/lab-products-and-services/application-support-knowledgebase/microplates/plate-dimensions.html
#(nrows, ncols, out) = (4, 6, '24-well')
#(nrows, ncols, out) = (8, 12, '96-well')
#(nrows, ncols, out) = (16, 24, '384-well')
(nrows, ncols, out) = (32, 48, '1536-well')

rows = (list(string.ascii_uppercase) + [2*l for l in string.ascii_uppercase])[:nrows]
cols = range(1, ncols + 1)

for plate_count, (skip_row, skip_col) in enumerate(itertools.product(rows, cols), start=1):
    file_name = f'{out}_{plate_count}.csv'
    print(f'{file_name} skips {skip_row}{skip_col}')
    with open(file_name, 'w') as f:
        for (row, col) in itertools.product(rows, cols):
            if (row == skip_row) and (col == skip_col):
                continue
            print(f'{row}{col}', file=f)
