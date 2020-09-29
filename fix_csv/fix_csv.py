import sys

def pipe2comma(line):
    line_out = ''
    for cell in line.split('|'):
        contains_comma = False
        prelim_cell = ''
        for char in cell:
            if char == '\n':
                continue
            prelim_cell += char
            if char == ',':
                contains_comma = True
            elif char == '"':
                prelim_cell += '"'
        if contains_comma:
            line_out += '"' + prelim_cell + '",'
        else:
            line_out += prelim_cell + ","
    return line_out[:-1] + '\n'


def fix_csv(read_file, write_file):
    with open(read_file, 'rt') as f_read, open(write_file, 'wt') as f_write:
        for row in f_read.readlines():
            f_write.write(pipe2comma(row))

if len(sys.argv) > 3:
    raise BaseException





