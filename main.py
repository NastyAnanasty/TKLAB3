import random

import numpy as np

import lab2


# --------------3.1----------------
def all_word(r):
    result = np.zeros([2 ** r - 1, r])
    bin_arr = range(0, int(2 ** r))
    bin_arr = [bin(i)[2:] for i in bin_arr]
    max_len = len(max(bin_arr, key=len))
    bin_arr = [i.zfill(max_len) for i in bin_arr]
    for i in range(0, 2 ** r - 1):
        for j in range(0, r):
            result[i, j] = bin_arr[i + 1][j]
    i = 0
    while i < result.shape[0]:
        if np.sum(result[i, :]) == 1:
            result = np.delete(result, i, axis=0)
            i = i
        else:
            i += 1
    return result


def gen_matr(r):
    gen_matr = np.eye(all_word(r).shape[0])
    gen_matr = np.hstack((gen_matr, all_word(r)))
    # print(gen_matr)
    return gen_matr


def check_matr(r):
    check_matr = np.eye(r)
    check_matr = np.vstack((all_word(r), check_matr))
    # print(check_matr)
    return check_matr


def get_code_word(matrix, k):
    k_word = []
    for i in range(k):
        k_word.append(lab2.round_num(random.uniform(0, 1)))
    n_word = lab2.code_word_from_k_to_n(matrix, k_word) % 2
    return n_word


def get_syndrom(r):
    return check_matr(r)


# ----------------------------------

# --------------3.2, 3.4------------
def study(error_num, n, k, g_matrix, h_matrix, syndrom_matrix):
    n_word = get_code_word(g_matrix, k)
    n_word_with_mistake = []
    if error_num == 1:
        n_word_with_mistake = lab2.make_single_mistake_in_n_word(n_word) % 2
    if error_num == 2:
        n_word_with_mistake = lab2.make_double_mistake_in_n_word(n_word) % 2
    if error_num == 3:
        n_word_with_mistake = lab2.make_triple_mistake_in_n_word(n_word) % 2
    if error_num == 4:
        n_word_with_mistake = lab2.make_quadro_mistake_in_n_word(n_word) % 2

    syndrom = n_word_with_mistake @ h_matrix % 2
    row_num = lab2.row_index_in_matrix(syndrom, syndrom_matrix)
    if row_num == -1:
        print("Синдром не найден для r = " + str(r) + " и "
              + str(error_num) + " ошибки")
    else:
        errors_table = np.eye(n, dtype=int)
        error = errors_table[row_num]
        may_be_n_word = np.abs(n_word_with_mistake - error)
        if np.array_equiv(n_word, may_be_n_word):
            print("Ошибка исправлена")
        else:
            print("Ошибка не исправлена")


# ----------------------------------

# --------------3.3-----------------
def check_matr3_3(r):
    check3_3 = check_matr(r)
    on = np.ones([pow(2, r), 1])
    zer = np.zeros([1, r])
    check3_3 = np.vstack((check3_3, zer))
    check3_3 = np.hstack((check3_3, on))
    print(check3_3)
    return check3_3


def syndrom3_3(r):
    return check_matr3_3(r)


def gen_matr3_3(r):
    gen3_3 = gen_matr(r)
    col = np.zeros([pow(2, r) - r - 1, 1])
    gen_m3_3 = np.hstack((gen3_3, col))
    sum_rows = np.sum(gen3_3, axis=1)
    for i in range(0, pow(2, r) - r - 1):
        if (sum_rows[i]) % 2 == 1:
            gen_m3_3[i, pow(2, r) - 1] = 1
    print(gen_m3_3)
    return gen3_3


if __name__ == '__main__':
    # this is a print for 3.1 task
    # my = gen_matr(r)
    # my = check_matr(r)
    # ny = get_syndrom(r)
    # print(ny)

    # this is a print for 3.3 task
    # che = check_matr3_3(3)
    # gen = gen_matr3_3(3)

    #3.2
    for r in range(2, 4):
        # initial data
        n = 2 ** r - 1
        k = 2 ** r - r - 1
        g_matrix = gen_matr(r)
        h_matrix = check_matr(r)
        syndrom = get_syndrom(r)

        for error_num in range(1, 3):
            study(error_num, n, k, g_matrix, h_matrix, syndrom)

    #3.4
    for r in range(2, 4):
        # initial data
        n = 2 ** r
        k = 2 ** r - r - 1
        g_matrix3_3 = gen_matr3_3(r)
        h_matrix3_3 = check_matr3_3(r)
        syndrom3_3 = syndrom3_3(r)

        # this is a print for 3.4 task
        for err_num in range(2, 4):
            study(err_num, n, k, g_matrix3_3, h_matrix3_3, syndrom3_3)

