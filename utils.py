import math
from collections import namedtuple


Page = namedtuple('Page', ['start', 'end', 'lines'])


def sliceinator(total_set, slice_size):
    total_count = len(total_set)
    if slice_size >= total_count:
        yield Page(start=100, end=99 + total_count, lines=total_set)
    else:
        yield Page(start=100, end=99+slice_size, lines=total_set[:slice_size])

        current_start = slice_size
        current_end = current_start + slice_size
        run = True

        while run:
            yield Page(
                start=current_start+100,
                end=current_end+99,
                lines=total_set[current_start:current_end]
            )
            current_start = current_end
            current_end += slice_size
            if current_end > total_count:
                run = False


class LogTableLine:
    def __init__(self, base, digits):
        self.base = base
        self.digits = digits

        base = str(base)

        sub_lines = self.get_sub_lines(base)
        values, means = self.flatten_sublines(sub_lines)

        self.values = [
            str(value).rjust(digits, '0')
            for value in values
        ]
        self.means = means

    def flatten_sublines(self, sub_lines):
        means = []

        values = [sub_line[0] for sub_line in sub_lines]
        for i in range(1, 10):
            diff_sum = 0
            for line in sub_lines:
                diff_sum += line[i] - line[0]
            means.append(round(diff_sum / 10))

        return values, means

    def get_sub_lines(self, base):
        sub_lines = []
        for x in range(10):
            sub_line = []
            for y in range(10):
                log_in = int(f'{base}{x}{y}')
                sub_line.append(self.log_mantissa(log_in))
            sub_lines.append(sub_line)

        return sub_lines

    def log_mantissa(self, log_in):
        while log_in >= 10:
            log_in /= 10
        return round(math.log10(log_in) * 10 ** self.digits)


class LogTable:
    def __init__(self, start, end, digits, per_page):
        self.digits = digits
        self.lines = [
            LogTableLine(base, digits)
            for base in range(start, end)
        ]
        self.pages = sliceinator(self.lines, per_page)
