# Exercise 4.7

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def rows(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        htmlrow = '<tr>'
        for h in headers:
            htmlrow += f'<th>{h}</th>'
        htmlrow += '</tr>'
        print(htmlrow)

    def row(self, rowdata):
        htmlrow = '<tr>'
        for d in rowdata:
            htmlrow += f'<td>{d}</td>'
        htmlrow += '</tr>'
        print(htmlrow)