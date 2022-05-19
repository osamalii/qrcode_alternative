import math

import PySimpleGUI as sg
from tkinter import *


def convert_string(string):
    for e in string:
        bnr = cvbn(ord(e), 8)
        print(bnr)
        r = ["X"] * 12
        ii = 0
        for rr in range(len(r)):
            if rr != 4 and rr != 8 and rr != 10 and rr != 11:
                r[rr] = bnr[ii]
                ii = ii + 1
        print("".join(r))


def set_control_bits(sqc):
    print(sqc)
    sqcrev = sqc[::-1]
    mat = []
    for j in range(len(sqcrev)):
        if sqcrev[j] == "1":
            print(list(cvbn(j+1, 4)))
            mat.append(list(cvbn(j+1, 4)))
    s = 0
    print(mat)
    z = []
    for j in range(4):
        for i in range(len(mat)):
            s = s + int(mat[i][j])
        z.append(s%2)
        s = 0
    print(z)





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


def cvbn(a, nbit):
    # this will print a in binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < nbit:
        x += '0'
    bnr = x[::-1]
    return bnr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    window = Tk()
    canvas = Canvas(window, height=500, width=500)
    string = "leau"
    convert_string(string)
    print(cvbn(12, 4))
    set_control_bits("1101X000X1XX")

# String length
