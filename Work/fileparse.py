# fileparse.py
#
# Exercise 3.9

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if has_headers:
            headers = next(rows)

        if select:
            indices = [headers.index(col_name) for col_name in select]
            headers = select
        else:
            indices = [] 

        records = []
        for i, row in enumerate(rows, start=1):
            if not row:
                continue

            if indices:
                row = [row[index] for index in indices]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f'Row {i}: Reason {e}')
                    continue

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

