# fileparse.py
#
# Exercise 3.17

import csv

def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    if type(file) == str:
        raise RuntimeError('file argument should not be a string')
        
    rows = csv.reader(file, delimiter=delimiter)

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
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f'Row {i}: Reason {e}')
                continue

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records

