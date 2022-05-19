import math
import struct

import numpy as np
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


def create_matrix(sqc):
    listsqc = list(sqc)
    k = 0
    matrix_size = math.floor(math.sqrt(len(listsqc))) + 2
    print("matrix size", matrix_size)
    matrix = np.zeros((matrix_size, matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            if j == 0 or j == matrix_size - 1:
                matrix[i][j] = 0
            if i == 0 or i == matrix_size - 1:
                matrix[i][j] = 0
        matrix[0][0] = 1
    for i in range(1, matrix_size - 1, 1):
        for j in range(1, matrix_size - 1, 1):
            if k <= len(listsqc):
                matrix[i][j] = listsqc[k]
                k = k + 1
            else:
                break

    return matrix


def draw_matrix(matrix, can):
    cell_size = calculate_cell_size(500, len(matrix))
    print(cell_size)
    lgx, lgy, cx, cy = 0, 0, 0, 0
    for lg in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[lg][c] == 1:
                can.create_rectangle(lg * cell_size, c * cell_size, (lg + 1) * cell_size, (c + 1) * cell_size,
                                     fill="black", width=5)
            # elif matrix[lg][c] == 0:
            #   can.create_line(lg * cell_size, c * cell_size, (lg+1)*cell_size, (c+1)*cell_size, fill="white", width=5)


def cvbn(a, nbit):
    # this will print a in binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < nbit:
        x += '0'
    bnr = x[::-1]
    return bnr

def float_to_bin(num):
    bits, = struct.unpack('!I', struct.pack('!f', num))
    return "{:032b}".format(bits)


# cell size => convert to binary
# msg length => convert size to binary
# first bit position => i = head size / matrix size, j = head size % matrix size

def create_head(input_message):
    l_head = 32 + 8 + 8 + 8
    l = len(input_message)
    cell_size = calculate_cell_size(500, l+l_head)
    cell_sise_bnr = float_to_bin(cell_size) #32 bits
    msg_length_bnr = cvbn(l, 8)             #8 bits
    matrix_size = math.floor(math.sqrt(l+l_head)) + 2
    print("matrix size", matrix_size)
    fst_bit_position_x, fst_bit_position_y = l_head // matrix_size , l_head % matrix_size #8 bits + 8 bits
    print("cell_sise_bnr", cell_sise_bnr)
    print("msg_length_bnr", msg_length_bnr)
    print("fst_bit_position_x", (fst_bit_position_x, 8))
    print("fst_bit_position_y", (fst_bit_position_y, 8))
    return cell_sise_bnr + msg_length_bnr + cvbn(fst_bit_position_x, 8) + cvbn(fst_bit_position_y, 8)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    canvas = Canvas(window, height=500, width=500)
    string: str = "b"


    binarystring = convert_string(string)
    head = create_head(binarystring)
    print(binarystring)

    matrix = create_matrix(binarystring+head)
    print(matrix)

    draw_matrix(matrix, canvas)
    canvas.pack()
    window.mainloop()
