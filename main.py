import math

import PySimpleGUI as sg
from tkinter import *


def convert_string(string):
    for e in string:
        a = ord(e)
        bnr = bin(a).replace('0b', '')
        x = bnr[::-1]
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        print(bnr)
        r = ["X"] * 12
        ii = 0
        for rr in range(len(r)):
            if rr != 4 and rr != 8 and rr != 10 and rr != 11:
                r[rr] = bnr[ii]
                ii = ii + 1
        print("".join(r))


def set_cnrtl_bits(sqc):

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def calculate_cell_size(l, strl):
    return l / strl


def create_matrix(string_length):
    matrix_size = math.floor(math.sqrt(string_length * 12)) + 2
    cell_size = calculate_cell_size(500, string_length)
    print(matrix_size)
    matrix = []
    for i in range(matrix_size):
        matrix[i] = []
        for j in range(matrix_size):
            matrix[i][j] = 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    window = Tk()
    canvas = Canvas(window, height=500, width=500)
    string = "leau"
    convert_string(string)

# String length
