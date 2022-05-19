import math
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


def create_matrix(string_length, sqc):
    listsqc = list(sqc)
    print(listsqc)
    k = 0
    matrix_size = math.floor(math.sqrt(string_length * 12)) + 2
    print(matrix_size)
    matrix = np.zeros((matrix_size, matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            if j == 0 or j == matrix_size - 1:
                matrix[i][j] = 0
            if i == 0 or i == matrix_size - 1:
                matrix[i][j] = 0
        matrix[0][0] = 1
    for i in range(1, matrix_size-1,1):
        for j in range(1, matrix_size-1,1):
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
                can.create_rectangle(lg * cell_size, c * cell_size, (lg+1)*cell_size, (c+1)*cell_size, fill="black")
            elif matrix[lg][c] == 0:
                can.create_rectangle(lg * cell_size, c * cell_size, (lg+1)*cell_size, (c+1)*cell_size, fill="white")



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
    string = "oussama"
    binarystring = convert_string(string)
    print(binarystring)
    matrix = create_matrix(len(string), binarystring)
    print(matrix)
    draw_matrix(matrix, canvas)
    canvas.pack()
    window.mainloop()

