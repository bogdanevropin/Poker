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


def pref_3b(y_pos: str, opp_pos: str):
    """
    
    :param y_pos: your position
    :param opp_pos: opponent position
    :return:
    """
    if y_pos == 'mp' and opp_pos == 'ep':
        mp_matrix = [[1,   1, 0.2, 0, 0, 0, 0, 0,   0,   0.5, 0.1, 0.1, 0.1],
                     [1,   1, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0.3, 0, 0.7, 0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0.3, 0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0.4, 0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0, 0, 0, 0, 0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'co' and opp_pos == 'ep':
        mp_matrix = [[1,   1, 0.2, 0.1, 0, 0, 0, 0,   0,   0.9, 0.1, 0.1, 0.1],
                     [1,   1, 0.3, 0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0.5, 0, 0.9, 0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0.5, 0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0.4, 0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0.9, 0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'btn' and opp_pos == 'ep':
        mp_matrix = [[1,   1,   0.5, 0.3, 0,   0,   0, 0,   0,   0.7, 0.1, 0.1, 0.1],
                     [1,   1,   0.4, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0.7, 0,   0.7, 0,   0.1, 0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0.2, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0.3, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0,   0.9, 0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'sb' and opp_pos == 'ep':
        mp_matrix = [[1,   1, 0.5, 0.1, 0,   0, 0, 0,   0,   0.9, 0.1, 0.1, 0.1],
                     [1,   1, 0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0.7, 0, 0.8, 0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0.5, 0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0.1, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0, 0.3, 0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0, 0,   0.9, 0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'bb' and opp_pos == 'ep':
        mp_matrix = [[1,   1, 1,   0.1, 0,   0, 0,   0,   0,   0.7, 0.1, 0.1, 0.1],
                     [1,   1, 0.1, 0,   0,   0, 0,   0,   0,   0,   0,   0,   0],
                     [0.7, 0, 1,   0,   0,   0, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0.3, 0,   0, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0.1, 0, 0.1, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0,   0.4, 0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0,   0,   0.5, 0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'co' and opp_pos == 'mp':
        mp_matrix = [[1,   1, 1,   0.5, 0, 0, 0, 0,   0,   0.5, 0.1, 0.1, 0.1],
                     [1,   1, 0.4, 0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [1,   0, 0.7, 0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0.3, 0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0.4, 0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0.4, 0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0, 0, 0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'btn' and opp_pos == 'mp':
        mp_matrix = [[1,   1,   1,   1,   0.5, 0,   0,   0,   0,   1, 0.2, 0.2, 0.2],
                     [1,   1,   0.8, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   0.3, 1,   0.1, 0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   0,   0,   1,   0.3, 0.5, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0.5, 0.1, 0.4, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0.4, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0.9, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0.9, 0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'sb' and opp_pos == 'mp':
        mp_matrix = [[1,   1, 1,   0.4, 0,   0,   0, 0,   0,   0.8, 0.2, 0.2, 0.2],
                     [1,   1, 0.3, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0.8, 0, 0.7, 0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0.5, 0.2, 0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0.3, 0.2, 0.7, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0, 0.5, 0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0, 0,   0.9, 0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0, 0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'bb' and opp_pos == 'mp':
        mp_matrix = [[1,   1, 1,   1,   0,   0,   0,   0,   0,   0.5, 0.1, 0.1, 0.1],
                     [1,   1, 1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0.7, 0, 1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0.5, 0,   0.2, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0.2, 0,   0.2, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0.2, 0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'btn' and opp_pos == 'co':
        mp_matrix = [[1,   1, 1,   1,   1,   0.3, 0.3, 0.3, 0.3, 1, 0.7, 0.7, 0.7],
                     [1,   1, 1,   0.2, 0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   1, 1,   0.4, 0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   0, 0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   1,   1,   0.2, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0.7, 0.7, 0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0.2, 0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'sb' and opp_pos == 'co':
        mp_matrix = [[1,   1,   1,   1,   0.5, 0.1, 0.1, 0.1, 0.1, 1, 0.3, 0.3, 0.3],
                     [1,   1,   0.5, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0.7, 0.5, 1,   0.2, 0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0.7, 0.4, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0.3, 0.4, 0.7, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0.7, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]]
        
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'bb' and opp_pos == 'co':
        mp_matrix = [[1,   1,   1,   0.9, 0,   0, 0, 0,   0,   0.5, 0.1, 0.1, 0.1],
                     [1,   1,   1,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [1,   0.8, 1,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   1,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0.5, 0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0, 0, 0.4, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0, 0, 0,   0.4, 0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0, 0, 0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'sb' and opp_pos == 'btn':
        mp_matrix = [[1,   1,   1,   1,   0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.7, 0.7, 0.7],
                     [1,   1,   0.9, 0.3, 0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   0.9, 0.9, 0.3, 0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0.8, 0.2, 0,   0.9, 0.1, 0.2, 0.1, 0,   0,   0,   0,   0,   0],
                     [0.5, 0,   0,   0,   0.9, 0.3, 0.5, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0.7, 0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0.6, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'bb' and opp_pos == 'btn':
        mp_matrix = [[1,   1,   1,   1,   1,   0.5, 0.4, 0.3, 0.3, 1,   0.4, 0.4, 0.4],
                     [1,   1,   1,   0.6, 0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   1,   1,   0.6, 0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [1,   0.3, 0.2, 1,   0.1, 0.1, 0,   0,   0,   0,   0,   0,   0],
                     [0.5, 0,   0,   0,   0.9, 1,   0.5, 0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0.7, 1,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0.9, 0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent
    
    if y_pos == 'bb' and opp_pos == 'sb':
        mp_matrix = [[1,   1, 1,   1,   1, 0.6, 0.5, 0.3, 0.3, 1, 0.4, 0.4, 0.4],
                     [1,   1, 1,   0.7, 0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0.7, 0, 0.7, 0.7, 0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   1,   0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   1,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   0,   1,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 0,   0,   0, 0,   0,   0,   0,   0,   0,   0,   0]]
        range_percent = sum([sum(mp_matrix[i]) for i in range(len(mp_matrix))]) / (
                len(mp_matrix) * len(mp_matrix[0])) * 100
        print(f'{y_pos} vs {opp_pos}: {round(range_percent, 2)} % range')
        return mp_matrix, range_percent


def test_visualise():
    from preflop_or import visualise_matrix
    you = 'bb'
    opp = 'sb'
    matrix = pref_3b(y_pos=you, opp_pos=opp)[0]
    visualise_matrix(chart_matrix=matrix, name=f'{you} vs {opp}')
    os.system('cls')


def test_all_visualise():
    from preflop_or import visualise_matrix
    avg_3b = 0
    sit = 0
    for p, you in enumerate(['mp', 'co', 'btn', 'sb', 'bb']):
        for opp in ['ep', 'mp', 'co', 'btn', 'sb'][:p+1]:
            sit += 1
            matrix, r_p = pref_3b(y_pos=you, opp_pos=opp)
            avg_3b += r_p
            visualise_matrix(chart_matrix=matrix, name=f'{you} vs {opp}')
            os.system('cls')
    avg_3b /= sit
    print(f'Average 3b {avg_3b}')


def main():
    """
    Test all
    """
    test_all_visualise()


if __name__ == '__main__':
    main()
