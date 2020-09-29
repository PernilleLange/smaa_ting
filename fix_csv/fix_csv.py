import sys
import argparse

def pipe2comma(delimiter, line):
    line_out = ''
    for cell in line.split(delimiter):
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


def fix_csv(delimiter,read_file, write_file):
    with open(read_file, 'rt') as f_read, open(write_file, 'wt') as f_write:
        for row in f_read.readlines():
            f_write.write(pipe2comma(delimiter,row))

if len(sys.argv) > 3:
    raise BaseException





