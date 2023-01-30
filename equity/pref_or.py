"""
Matrix charts for actions
0 - no chance 1 - all hands
[[AAo, AKs, AQs, AJs, ATs, A9s, A8s, A7s, A6s, A5s, A4s, A3s, A2s],
 [AKo, KKo, KQs, KJs, KTs, K9s, K8s, K7s, K6s, K5s, K4s, K3s, K2s],
 [AQo, KQo, QQo, KJs, KTs, K9s, Q8s, Q7s, Q6s, Q5s, Q4s, K3s, Q2s],
 [AJo, KJo, QJo, JJo, JTs, J9s, J8s, J7s, J6s, J5s, J4s, K3s, J2s],
 [ATo, KTo, QTo, JTo, TTo, T9s, T8s, T7s, T6s, T5s, T4s, K3s, T2s],
 [A9o, K9o, Q9o, J9o, T9o, 99o, 97s, 97s, 96s, 95s, 94s, K3s, 92s],
 [A8o, K8o, Q8o, J8o, T8o, 98o, 88o, 87s, 86s, 85s, 84s, K3s, 82s],
 [A7o, K7o, Q7o, J7o, T7o, 97o, 87o, 77o, 76s, 75s, 74s, K3s, 72s],
 [A6o, K6o, Q6o, J6o, T6o, 96o, 86o, 76o, 66o, 65o, 64s, K3s, 62s],
 [A5o, K5o, Q5o, J5o, T5o, 95o, 85o, 75o, 65o, 55o, 54s, K3s, 52s],
 [A4o, K4o, Q4o, J4o, T4o, 94o, 84o, 74o, 64o, 54o, 44o, 43s, 42s],
 [A3o, K3o, Q3o, J3o, T3o, 93o, 83o, 73o, 63o, K5o, 43o, 33o, 32s],
 [A2o, K2o, Q2o, J2o, T2o, 92o, 82o, 72o, 62o, K5o, 42o, 32o, 22o]]
"""
import os
from PIL import Image
import numpy as np


def pref_or(pos):
    if pos == 'ep':
        ep_matrix = [[1,   1,   1,   1,   1,   0,   0,   0,   0,   0.8, 0.7, 0.3, 0.2],
                     [1,   1,   1,   1,   0.9, 0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   1,   1,   1,   0.9, 0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   0.5, 0,   1,   0.7, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   1,   0.9, 0.3, 0.1, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   1,   0.7, 0.2, 0.1, 0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   1,   0.5, 0.1, 0.1, 0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0.9, 1,   0.3, 0.1, 0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0.7, 0.3, 0.2, 0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0.4, 0.2, 0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.3, 0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.2, 0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.1]]
        range_percent = sum([sum(ep_matrix[i]) for i in range(len(ep_matrix))]) / (
            len(ep_matrix) * len(ep_matrix[0])) * 100
        print(f'   EP: {round(range_percent, 2)} % range')
        return ep_matrix, range_percent
    elif pos == 'mp':
        mp_matrix = [[1,   1,   1,   1,   1,   0.8, 0.7, 0.6, 0.5, 1, 0.4, 0.5, 0.7],
                     [1,   1,   1,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   1,   1,   1,   1,   0.1, 0,   0,   0,   0,   0,   0,   0],
                     [1,   1,   1,   1,   1,   0.5, 0.2, 0,   0,   0,   0,   0,   0],
                     [1,   0,   0,   0,   1,   1,   0.5, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   1,   0.5, 0.3, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   1,   0.4, 0.4, 0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   1,   1,   0.2, 0.1, 0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0.8, 0.3, 0.1, 0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0.5, 0.2, 0.1, 0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.2, 0.1, 0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.2, 0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.2]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
            len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'   MP: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    elif pos == 'co':
        co_matrix = [[1,   1,   1,   1,   1,   1,   0.9, 0.9, 0.9, 1,   0.5, 0.5, 0.5],
                     [1,   1,   1,   1,   1,   0.8, 0,   0,   0,   0,   0,   0,   0],
                     [1,   1,   1,   1,   1,   0.8, 0.8, 0,   0,   0,   0,   0,   0],
                     [1,   1,   1,   1,   1,   0.8, 0.8, 0,   0,   0,   0,   0,   0],
                     [1,   1,   1,   1,   1,   1,   1,   0,   0,   0,   0,   0,   0],
                     [0.7, 0.3, 0.4, 0.2, 0.1, 1,   0.2, 0.1, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   1,   0.7, 0.8, 0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   1,   0.9, 0.5, 0.1, 0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   1,   0.8, 0.1, 0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0.6, 0.1, 0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0.5, 0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.8, 0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.6]]
        range_percent = sum([sum(co_matrix[i]) for i in range(len(co_matrix))]) / (
                len(co_matrix) * len(co_matrix[0])) * 100
        print(f'   CO: {round(range_percent, 2)} % range')
        return co_matrix, range_percent
    elif pos == 'btn':
        btn_matrix = [[1,  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1],
                      [1,  1,   1,   1,   1,   1,   1,   0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
                      [1,  1,   1,   1,   1,   1,   1,   0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
                      [1,  1,   1,   1,   1,   1,   1,   0.2, 0,   0,   0,   0,   0],
                      [1,  1,   1,   1,   1,   1,   1,   1,   0.1, 0,   0,   0,   0],
                      [1,  0.9, 0.8, 0.6, 0.4, 1,   1,   1,   0.2, 0,   0,   0,   0],
                      [1,  0.6, 0.5, 0.4, 0.3, 0.1, 1,   1,   1,   0.2, 0,   0,   0],
                      [1,  0,   0,   0,   0,   0,   0,   1,   1,   0.4, 0.2, 0,   0],
                      [1,  0,   0,   0,   0,   0,   0,   0,   1,   1,   0.4, 0,   0],
                      [1,  0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   0.2, 0],
                      [1,  0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0.4, 0],
                      [1,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0],
                      [1,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1]]
        range_percent = sum([sum(btn_matrix[i]) for i in range(len(btn_matrix))]) / (
                len(btn_matrix) * len(btn_matrix[0])) * 100
        print(f'  BTN: {round(range_percent, 2)} % range')
        return btn_matrix, range_percent
    elif pos == 'sb':
        sb_raise_matrix = [[0.1, 0.8, 0.8, 0.8, 0.7, 0.5, 0.1, 0.1, 0.1, 0.3, 0.3, 0.3, 0.3],
                           [0.3, 0.2, 0.8, 0.8, 0.8, 0.2, 0,   0,   0,   0,   0,   0,   0],
                           [0.5, 0.9, 0.3, 0.7, 0.4, 0.8, 0,   0,   0,   0,   0,   0,   0],
                           [0.3, 0.8, 0.8, 0.4, 1,   0.5, 0.8, 0,   0,   0,   0,   0,   0],
                           [0.1, 0,   0,   0,   1,   0.8, 0.7, 0,   0,   0,   0,   0,   0],
                           [0,   0,   0,   0,   0,   1,   0.9, 0.1, 0,   0,   0,   0,   0],
                           [0,   0,   0,   0,   0,   0,   1,   0.7, 0.2, 0,   0,   0,   0],
                           [0,   0,   0,   0,   0,   0,   0,   0.8, 0.9, 0.6, 0.8, 0,   0],
                           [0,   0,   0,   0,   0,   0,   0,   0,   0.6, 0.8, 0.6, 0,   0],
                           [0,   0,   0,   0,   0,   0,   0,   0,   0,   0.2, 0.5, 0,   0],
                           [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.2, 0.1, 0],
                           [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.2, 0],
                           [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]]
        
        sb_limp_matrix = [[0.9, 0.2, 0.2, 0.2, 0.3, 0.2, 0.9, 0.9, 0.9, 0.2, 0.7, 0.7, 0.7],
                          [0.7, 0.8, 0.2, 0.2, 0.2, 0.8, 1,   1,   1,   1,   1,   1,   1],
                          [0.5, 0.1, 0.7, 0.3, 0.6, 0.2, 1,   1,   1,   1,   1,   1,   1],
                          [0.7, 0.2, 0.2, 0.6, 0,   0.5, 0.2, 1,   1,   1,   1,   1,   1],
                          [0.9, 1,   1,   1,   0,   0.2, 0.3, 1,   1,   1,   0.7, 0,   0],
                          [1,   1,   1,   1,   1,   0,   0.1, 0.9, 0.8, 0.5, 0.6, 0,   0],
                          [1,   1,   1,   1,   1,   1,   0, 0.3, 0.1, 1,   0,   0,   0],
                          [1,   1,   1,   1,   0,   0,   1,   0.2, 0.1, 0.4, 0.2, 0,   0],
                          [1,   1,   1,   0,   0,   0,   0,   1,   0.4, 0.2, 0.4, 0,   0],
                          [1,   0.8, 0.7, 0,   0,   0,   0,   0,   1,   0.8, 0.5, 0,   0],
                          [1,   0.2, 0,   0,   0,   0,   0,   0,   0,   1,   0.8, 0.9, 0],
                          [1,   0.2, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0.8, 1],
                          [1,   0.2, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1]]
        raise_percent = sum([sum(sb_raise_matrix[i]) for i in range(len(sb_raise_matrix))]) / (
                len(sb_raise_matrix) * len(sb_raise_matrix[0])) * 100
        limp_percent = sum([sum(sb_limp_matrix[i]) for i in range(len(sb_limp_matrix))]) / (
                len(sb_limp_matrix) * len(sb_limp_matrix[0])) * 100
        for r, row in enumerate(sb_limp_matrix):
            for i, el in enumerate(row):
                if sb_limp_matrix[r][i] + sb_raise_matrix[r][i] > 1:
                    print(f'Error (p>1) prob with element {r=} {i=}')
        range_percent = raise_percent + limp_percent
        print(f'   SB: {round(range_percent, 2)} % range')
        print(f'Limp : {round(limp_percent, 2)} % range')
        print(f'Raise: {round(raise_percent, 2)} % range')
        return sb_raise_matrix, range_percent, sb_limp_matrix
    elif pos == 'bb':
        """
        Raise limper sb
        """
        bb_raise_matrix = [[1,   1,   1,   1,   1,   1,   1,   0.3, 0.3, 0.6, 0.3, 0.3, 0.3],
                           [1,   1,   1,   1,   1,   0.4, 0.2, 0,   0,   0,   0,   0,   0],
                           [1,   1,   1,   1,   1,   0.8, 0.3, 0,   0,   0,   0,   0,   0],
                           [1,   1,   1,   1,   1,   0.2, 0.1, 0,   0,   0,   0,   0,   0],
                           [1,   1,   1,   1,   1,   1,   1,   0,   0,   0,   0,   0,   0],
                           [0.9, 0.8, 0.7, 0.6, 0,   1,   1,   0.3, 0.1, 0,   0,   0,   0],
                           [0.5, 0.4, 0,   0,   0,   0,   1,   1,   0.4, 0,   0,   0,   0],
                           [0.3, 0,   0,   0,   0,   0,   0,   1,   1,   0.6, 0.8, 0,   0],
                           [0.7, 0,   0,   0,   0,   0,   0,   0,   0.9, 0.8, 0.6, 0,   0],
                           [0.9, 0,   0,   0,   0,   0,   0,   0,   0,   0.8, 0.5, 0.3, 0],
                           [0.7, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0.7, 0.4, 0],
                           [0.7, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.6, 0.2],
                           [0.7, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0.5]]
        range_percent = sum([sum(bb_raise_matrix[i]) for i in range(len(bb_raise_matrix))]) / (
            len(bb_raise_matrix) * len(bb_raise_matrix[0])) * 100
        print(f'   BB: {round(range_percent, 2)} % range')
        return bb_raise_matrix, range_percent
    else:
        raise Exception(f'Unknown pos {pos}')


def visualise_matrix(chart_matrix, name):
    curr_dir = os.getcwd()
    pixels = Image.open(curr_dir + '\\pre_flop\\charts\\white_grid.jpg')
    w, h = pixels.size
    step_h = h // 13
    # ho = h % 13
    step_w = w // 13
    # wo = w % 13
    pix = list(pixels.getdata())
    pixels = np.array([pix[i * w:(i + 1) * w] for i in range(1, h-1)])
    from copy import deepcopy
    im_new = deepcopy(pixels)
    for y, r in enumerate(chart_matrix):
        for x, v in enumerate(r):
            if v > 0:
                colour = (round(255*(1-v)), 255, round(255*(1-v)))
                cells = pixels[y * step_h:(y + 1) * step_h, x * step_w: (x + 1) * step_w]

                for y_c, row in enumerate(cells):
                    for x_c, cell in enumerate(row):
                        if sum(cell) > 115 * 3 or v == 0:  # white cell
                            im_new[y * step_h + y_c][x * step_w + x_c] = colour
                        else:  # black cell
                            im_new[y * step_h + y_c][x * step_w + x_c] = cell
            else:
                c = np.zeros((step_h, step_w, 3), dtype=int)
                im_new[y * step_h + 1:(y + 1) * step_h + 1, x * step_w + 1: (x + 1) * step_w + 1] = c

    im2 = Image.fromarray(np.uint8(im_new))
    im2.show(title=name)
    # input('Press Enter. . .')


def test_all_visualise():
    for pos in ['ep', 'mp', 'co', 'btn', 'bb']:
        matrix = pref_or(pos=pos)[0]
        visualise_matrix(chart_matrix=matrix, name=pos)
        os.system('cls')
    print('Raise SB')
    visualise_matrix(chart_matrix=pref_or('sb')[0], name='sb raise')
    os.system('cls')
    print('Limp SB')
    visualise_matrix(chart_matrix=pref_or('sb')[2], name='sb limp')
    os.system('cls')


def main():
    test_all_visualise()


if __name__ == '__main__':
    main()
