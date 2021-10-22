import numpy as np


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
    print(gen_matr)
    return gen_matr


def check_matr(r):
    check_matr = np.eye(r)
    check_matr = np.vstack((all_word(r), check_matr))
    print(check_matr)
    return check_matr


def syndrom(r):
    return check_matr(r).transpose()


if __name__ == '__main__':
    r = 4
    my = gen_matr(r)
    my = check_matr(r)
