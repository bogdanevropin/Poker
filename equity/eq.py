"""
Finds equity
"""
import random
# import numpy as np


def card_to_str(card: tuple):
    """
    Converting card to str readable format
    :param card: card tuple
    """
    if card is None:
        raise Exception('No card')
    suits = ['♥', '♠', '♦', '♣']  # Harts Spades Clubs Diamonds
    cards = [0, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    # 11 Jack 12 Queen 13 King 14 or 1 Ace
    v = card[0]
    s = card[1]
    prt = ''
    # if 2 <= v <= 10:
    #     prt += str(v)
    # elif v == 11:
    #     prt += 'J'
    # elif v == 12:
    #     prt += 'J'
    # elif v == 13:
    #     prt += 'J'
    # elif v == 1 or v == 14:
    #     prt += 'A'
    if v <= 15:
        prt += cards[v]
    else:
        raise Exception(f'Strange card {card} value {v}')
    prt += suits[s]
    return prt


def prt_cards(cards):
    """
    Print list of cards
    :param cards: list or tuple of cards
    """
    prt = ''
    prt = prt.join(f'{card_to_str(crd)} ' for crd in cards)
    return prt


def prt_combo(comb):
    """
    Print combination
    :param comb:
    """
    best_comb = f'Best combination {comb[1]}: '
    elements = comb[0]
    if type(elements) is tuple and type(elements[0]) is int:
        stop = True
    elif type(elements[0]) is tuple and type(elements[0][0]) is int:
        stop = True
    else:
        stop = False
    while not stop:
        all_el = []
        for e2 in elements:
            for e in e2:
                all_el.append(e)
        elements = all_el
        if type(elements) is tuple and type(elements[0]) is int:
            stop = True
        elif type(elements[0]) is tuple and type(elements[0][0]) is int:
            stop = True
    c = prt_cards(elements)
    best_comb += c
    return best_comb
    # for el in comb[0]:
    #     if el is tuple or el[0] is int:
    #         c += prt_cards(el)
    #     else:
    #         for el2 in el:
    #             if el2 is tuple or el[0] is int:
    #                 c += prt_cards(el2)
    # return c


def make_comb(hand: list, board: list):
    """
    Make final player combination
    :param hand: players hand cards (list of 2 tuples)
    :param board: board after river (list of 2 tuples)
    :return:
    """
    if not board:
        raise Exception('No board')
    if not hand:
        raise Exception('No hand')
    if len(hand) != 2:
        raise Exception(f'Hand size {len(hand)}')
    if not 3 <= len(board) <= 5:
        raise Exception(f'Board size {len(board)}')
    pair = None
    two_pairs = None
    set_trips = None
    straight = None
    flash = None
    full_house = None
    quads = None
    straight_flush = None
    
    cards_for_comb = list(board)
    cards_for_comb.append(hand[0])
    cards_for_comb.append(hand[1])
    
    sort = sorted(cards_for_comb, key=lambda tup: tup[0])  # sort cards by values
    high_cards = sort[-5:]  # Highest cards
    suited = sorted(cards_for_comb, key=lambda tup: tup[1])  # sort cards by suits

    l_flash = len(suited) - 5  # num of 5 same suit cards
    for index in range(l_flash):  # flash check
        curr = suited[index: index+5]
        if len(set([card[1] for card in curr])) == 1:  # 1 type of suit for all 5 cards
            flash = curr
    
    straighted = sort
    for card in sort:
        if card[0] == 14:  # add ace same as 1:
            straighted.append((1, card[1]))  # ace with that suit
    l_straight = len(straighted) - 5  # num of 5 in row cards
    straighted = sorted(straighted, key=lambda tup: tup[0])
    for index in range(l_straight):
        curr = straighted[index: index+5]
        for n in range(4):  # except last
            card = curr[n]
            next_card = curr[n+1]
            if card[0] + 1 != next_card[0]:  # card value +1 equals to next card
                break
        else:
            straight = curr
            suite = None
            for card in straight:
                if suite is not None:  # have suit for current straight and check
                    if card[1] != suite:
                        break  # not same suit
                else:  # don't have suit for current straight
                    suite = card[1]  # set suit for straight flash
    else:  # checked all straights
        if straight_flush:
            return straight_flush, 'straight flush'  # best combo
    
    same_values = {}  # dict of card values and amount of cards with this value
    for card in sort:
        value = card[0]
        if value not in same_values:
            same_values[value] = [card]
        else:
            same_values[value].append(card)

    high_pair = None
    low_pair = None
    
    high_set_trips = None
    low_set_trips = None
    
    for value in same_values:
        same = same_values[value]
        if len(same) == 4:  # quads
            quads = same
            # can't be more than 1 quads comb by player
            return quads, 'quads'  # don't have straight flash and have quads
        elif len(same) == 3:  # trips/set
            if high_set_trips is None:  # no high pair
                high_set_trips = same
            elif low_set_trips is None:  # no pairs
                low_set_trips = same
            v = same[0][0]  # same card value
            if high_set_trips is not None and v > high_set_trips[0][0]:  # sets/trips and value bigger
                low_set_trips = high_set_trips
                high_set_trips = same
            elif low_set_trips is not None and v > low_set_trips[0][0]:  # have both sets/trips and value bigger
                low_set_trips = same
        elif len(same) == 2:  # pair
            if high_pair is None:  # no high pair
                high_pair = same
            elif low_pair is None:  # no pairs
                low_pair = same
            v = same[0][0]  # same card value extra changing shuffle for best pair
            if high_pair is not None and v > high_pair[0][0]:
                low_pair = high_pair
                high_pair = same
            elif low_pair is not None and v > low_pair[0][0]:
                low_pair = same
    if high_set_trips:
        if low_set_trips:  # have both sets
            # hp = None
            # if high_pair:
            #     hp = high_pair
            # elif low_pair:
            #     hp = low_pair
            # if hp and low_set_trips[0][0] > hp[0][0]:
            high_pair = low_set_trips[:2]
            return (high_set_trips, high_pair), 'full house'
        elif high_pair:  # strange
            if high_pair:
                return (high_set_trips, high_pair), 'full house'
            # elif low_pair:  # extra check
            #     return [high_set_trips, high_pair], 'full house'
        elif flash:
            return flash, 'flash'
        elif straight:
            return straight, 'straight'
        else:
            return high_set_trips, 'set trips'
    elif high_pair is not None and low_pair is not None:
        two_pairs = high_pair, low_pair
    elif high_pair is not None:
        pair = high_pair
    if quads:
        return quads, 'quads'
    elif full_house:
        return full_house, 'full house'
    elif flash:  # !!!
        return flash, 'flash'
    elif straight:  # !!!
        return straight, 'straight'
    elif set_trips:
        return set_trips, 'set trips'
    elif two_pairs:
        return two_pairs, 'two pairs'
    elif pair:
        return pair, 'pair'
    else:  # !!!
        return high_cards, 'high cards'


def compare_combinations(comb1: tuple, comb2: tuple):
    """
    Compare 2 player's combinations
    :param comb1: tuple of Comb and str name pl1
    :param comb2: tuple of Comb and str name pl2
    """
    comb_rang = ('high cards', 'pair', 'two pairs',
                 'set trips', 'straight', 'flash',
                 'full house', 'quads', 'straight flush')
    combs1, combs2 = comb1[0], comb2[0]
    name1, name2 = comb1[1], comb2[1]
    
    r1 = comb_rang.index(name1)
    r2 = comb_rang.index(name2)
    if r1 < r2:
        return 'lose'  # lose the pot
    elif r1 > r2:
        return 'win'  # win the pot
    elif combs1 == combs2:
        return 'split'  # split the pot
    else:
        if name1 != name2:
            raise Exception(f'Index1 {r1}, Index2 {r2}\n'
                            f'{combs1}, {combs2}\n'
                            f'{name1}, {name2}')
        elif name1 == 'pair' or name1 == 'quads':  # pair compare
            if combs1[0][0] > combs2[0][0]:  # pair card compare
                return 'win'
            elif combs1[0][0] < combs2[0][0]:
                return 'lose'
            else:
                return 'split'
        elif name1 == 'two pairs' or name1 == 'full house':  # two pairs compare (parts)
            if combs1[0][0][0] > combs2[0][0][0]:  # high pair compare
                return 'win'
            elif combs1[0][0][0] < combs2[0][0][0]:
                return 'lose'
            else:  # low pair compare
                if combs1[1][0][0] > combs2[1][0][0]:  # low pair compare
                    return 'win'
                elif combs1[1][0][0] < combs2[1][0][0]:
                    return 'lose'
                else:
                    return 'split'
        elif name1 == 'set trips':  # set or trips compare
            if combs1[0][0][0] > combs2[0][0][0]:  # any card compare
                return 'win'
            elif combs1[0][0][0] < combs2[0][0][0]:
                return 'lose'
            else:
                return 'split'
        elif name1 == 'straight flash' or name1 == 'flash' or name1 == 'straight' or name1 == 'high cards':
            # straight type compare by max card
            for i in range(4, -1, -1):
                if combs1[i][0] > combs2[i][0]:
                    return 'win'
                elif combs1[i][0] < combs2[i][0]:
                    return 'lose'
            else:
                return 'split'
        else:
            raise Exception(f'Unknown name {name1}')


def make_range(start_set: set or None = None, dead_cards_set: list or None = None):
    """
    Create range after deleting from it dead cards
    :param start_set: None for full range by default or list of range before dead card
    :param dead_cards_set: list of dead cards , None for no dead cards
    :return: set of current range after extracting dead cards from it
    """
    if not start_set:
        start_set = set()
        for c1 in range(2, 15):
            for s in range(4):
                start_set.add((c1, s))
    if dead_cards_set:
        start_set = start_set.difference(dead_cards_set)
    return start_set


def h_vs_h_result(hand1: list, hand2: list, curr_board: list):
    """
    Compare hands
    :param hand1: 2 cards list
    :param hand2: 2 cards list
    :param curr_board: 3-5 size list of cards board
    :return: 'win', 'lose', 'split'
    """
    c1 = make_comb(hand=hand1, board=curr_board)
    c2 = make_comb(hand=hand2, board=curr_board)
    return compare_combinations(comb1=c1, comb2=c2)


def gen_flop(dead_cards: set, all_=False):
    """
    Generating flop
    :param all_: gen all flops or not
    :param dead_cards: dead cards (player or players and board)
    :return: range and list of 3 cards
    """
    all_cards = list(make_range(dead_cards_set=dead_cards))
    flop = random.sample(all_cards, 3)
    if all_:
        # print(len(all_cards))
        all_flops = []
        cards_indexes = len(all_cards)
        for f1 in range(cards_indexes-2):
            for f2 in range(f1+1, cards_indexes-1):
                for f3 in range(f2+1, cards_indexes):
                    all_flops.append([all_cards[f1], all_cards[f2], all_cards[f3]])
        # print(len(all_flops))
        return flop, all_cards, all_flops
    else:
        return flop, all_cards


def gen_next_card(prev: list, dead_cards: set, all_=False):
    """
    Generating next card
    :param all_: all type of next card situation
    :param prev: flop or turn as list
    :param dead_cards: players and board cards
    :return:
    """
    all_cards = list(make_range(dead_cards_set=dead_cards))
    n = random.choice(all_cards)
    if all_:
        all_next = []
        for c in all_cards:
            new = prev + [c]
            all_next.append(new)
        print(len(all_next))
        return prev, all_cards, all_next
    else:
        prev = prev + [n]
        return prev, all_cards


def gen_board(dead_cards: set, all_=False):
    """
    Generate board
    :param dead_cards: players dead cards
    :param all_: all types of board
    :return:
    """
    all_cards = list(make_range(dead_cards_set=dead_cards))  # available for generating
    board = random.sample(all_cards, 5)
    if all_:
        # print(len(all_cards))
        all_boards = []
        cards_indexes = len(all_cards)
        for f1 in range(cards_indexes - 4):
            for f2 in range(f1 + 1, cards_indexes - 3):
                for f3 in range(f2 + 1, cards_indexes - 2):
                    for t in range(f3 + 1, cards_indexes - 1):
                        for r in range(t, cards_indexes):
                            all_boards.append([all_cards[f1], all_cards[f2], all_cards[f3],
                                               all_cards[t], all_cards[r]])
        # print(len(all_next))
        return board, all_cards, all_boards
    return board, all_cards


def hand_equity(hand1, hand2, curr_board=None):
    """
    Finds hands equity vs hand
    :param hand1: player 1 cards
    :param hand2: player 2 cards
    :param curr_board:   current board
    """
    dead_cards = set(hand1 + hand2)
    h1_wins = 0
    h2_wins = 0
    splits = 0
    compares = 0
    if not curr_board:  # pre flop
        # all_flops = gen_flop(dead_cards=dead_cards, all_=True)[2]
        # for flop in all_flops:  # all flops
        #     dead_cards = set(hand1 + hand2 + flop)
        #     curr_all_turns = list(gen_next_card(prev=list(flop), dead_cards=set(dead_cards), all_=True)[2])
        #     for turn in curr_all_turns:
        #         dead_cards = set(hand1 + hand2 + turn)
        #         curr_all_rivers = list(gen_next_card(prev=list(flop), dead_cards=set(dead_cards), all_=True)[2])
        #         for river in curr_all_rivers:
        #             result = h_vs_h_result(hand1=hand1, hand2=hand2, curr_board=river)
        #             compares += 1
        #             if result == 'win':
        #                 h1_wins += 1
        #             elif result == 'lose':
        #                 h2_wins += 1
        #             else:
        #                 splits += 1
        all_boards = gen_board(dead_cards=dead_cards, all_=True)[2]
        for board in all_boards:
            result = h_vs_h_result(hand1=hand1, hand2=hand2, curr_board=board)
            compares += 1
            if result == 'win':
                h1_wins += 1
            elif result == 'lose':
                h2_wins += 1
            else:
                splits += 1
        score1 = (h1_wins*2 + splits) / (compares * 2)
        score2 = (h2_wins*2 + splits) / (compares * 2)
        return score1, score2, h1_wins, h2_wins, splits


def main():
    """
    Simulations
    """
    hand_1 = [(5, 3), (11, 1)]
    hand_2 = [(9, 3), (12, 1)]
    # dead_cards = set(hand_1 + hand_2)
    print(hand_equity(hand1=hand_1, hand2=hand_2))
    # for i in range(100):
    #     print()
    #     flop = gen_flop(dead_cards=dead_cards, all=True)[0]
    #     dead_cards = list(dead_cards)
    #     turn = list(gen_next_card(prev=list(flop), dead_cards=set(flop+dead_cards))[0])
    #     river = list(gen_next_card(prev=list(turn), dead_cards=set(turn+dead_cards))[0])
    #     print(f'Deal №: {i+1}')
    #     print('River: ' + prt_cards(river))
    #     print('Player 1: ' + prt_cards(hand_1))
    #     print('Player 2: ' + prt_cards(hand_2))
    #     print(prt_combo(make_comb(hand=hand_1, board=river)))
    #     print(prt_combo(make_comb(hand=hand_2, board=river)))
    #     print(h_vs_h_result(hand1=hand_1, hand2=hand_2, curr_board=river))


if __name__ == '__main__':
    main()
