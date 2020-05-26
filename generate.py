import sys
from jinja2 import Template

from utils import LogTable


class TableRenderer:
    def __init__(self, table):
        self.table = table

    def render(self, output_name):
        with open('log_template.tex') as inf:
            template = Template(inf.read())
        with open(output_name, 'w') as outf:
            outf.write(template.render(table=self.table))


if __name__ == '__main__':
    precision = int(sys.argv[1])
    digits = int(sys.argv[2])
    per_page = int(sys.argv[3])
    output_filename = sys.argv[4]

    start = 10 ** (precision - 1)
    end = start * 10

    table = LogTable(start, end, digits, per_page)
    renderer = TableRenderer(table)
    renderer.render(output_filename)
