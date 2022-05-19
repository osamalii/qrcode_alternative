import math

import PySimpleGUI as sg
from tkinter import *


def convert_string(input_string):
    output = ""
    for e in input_string:
        bnr = cvbn(ord(e), 8)
        r = ["X"] * 12
        ii = 0
        for rr in range(len(r)):
            if rr != 4 and rr != 8 and rr != 10 and rr != 11:
                r[rr] = bnr[ii]
                ii = ii + 1
        output += set_control_bits("".join(r))
    return output


def set_control_bits(sqc):
    sqcrev = sqc[::-1]
    mat = []
    for j in range(len(sqcrev)):
        if sqcrev[j] == "1":
            mat.append(list(cvbn(j + 1, 4)))
    s = 0
    z = []
    listsq = list(sqc)
    for j in range(4):
        for i in range(len(mat)):
            s = s + int(mat[i][j])
        z.append(s % 2)
        s = 0
    listsq[4] = z[0]
    listsq[8] = z[1]
    listsq[10] = z[2]
    listsq[11] = z[3]
    listsq = map(lambda x: str(x), listsq)
    return "".join(listsq)


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
    window = Tk()
    canvas = Canvas(window, height=500, width=500)
    string = "leau"
    binarystring = convert_string(string)
    print(binarystring)

