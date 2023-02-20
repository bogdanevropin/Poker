"""
Tools
"""
# import pprint
import random
# import os
import csv


# import numpy as np


def save_to_csv(data, file_path='D:\\Bogdan\\Programming\\Poker\\equity\\pre_flop\\eq.csv'):
	"""
	Save to csv file
	:param data:
	:param file_path:
	"""
	with open(file_path, 'w', newline='') as csv_file:
		csv_out = csv.writer(csv_file)
		csv_out.writerow(
			('hand1', 'hand2', 'percent_wins1', 'percent_wins2', 'percent_split', 'eq1', 'eq2', 'h1_wins', 'h2_wins',
			 'splits', 'compares'))
		for row in data:
			csv_out.writerow(row)


def card_to_nums(card):
	"""
	Converting card to str readable format
	:param card: card str
	"""
	if card is None:
		raise Exception('No card')
	v = card[0]
	s = card[1]
	str_suits = ['h', 's', 'd', 'c']
	suits = ['♥', '♠', '♦', '♣']  # Harts Spades Clubs Diamonds
	cards = [0, 1, '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	try:
		vi = cards.index(v)
		si = str_suits.index(s)
		return (vi, si), card[0] + suits[si]
	except ValueError:
		return


def card_to_str(card: tuple):
	"""
	Converting card to str readable format
	:param card: card tuple
	"""
	if card is None:
		raise Exception('No card')
	suits = ['♥', '♠', '♦', '♣']  # Harts Spades Clubs Diamonds
	cards = [0, 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	# 11 Jack 12 Queen 13 King 14 or 1 Ace
	v = card[0]
	s = card[1]
	prt = ''
	if 1 <= v <= 15:
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
	straight_flash = None
	
	cards_for_comb = list(board)
	cards_for_comb.append(hand[0])
	cards_for_comb.append(hand[1])
	
	sort = sorted(cards_for_comb, key=lambda tup: tup[0])  # sort cards by values
	high_cards = sort[-5:]  # Highest cards
	suited = sorted(cards_for_comb, key=lambda tup: tup[1])  # sort cards by suits
	
	l_flash = len(suited) - 5  # num of 5 same suit cards
	for index in range(l_flash + 1):  # flash check
		curr = suited[index: index + 5]
		if len(set([card[1] for card in curr])) == 1:  # 1 type of suit for all 5 cards
			flash = curr
	
	straighted = sort
	for card in sort:
		if card[0] == 14:  # add ace same as 1:
			straighted.append((1, card[1]))  # ace with that suit
	l_straight = len(straighted) - 5  # num of 5 in row cards
	straighted = sorted(straighted, key=lambda tup: tup[0])
	for index in range(l_straight + 1):
		curr = straighted[index: index + 5]
		for n in range(4):  # except last
			card = curr[n]
			next_card = curr[n + 1]
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
			else:
				straight_flash = curr
	# else:  # checked all straights
	if straight_flash:
		return straight_flash, 'straight flash'  # best combo
	
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
			for card in sort:
				if card not in quads:
					h_cards = card
					return [quads, h_cards], 'quads'  # don't have straight flash and have quads
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
			high_pair = low_set_trips[:2]
			return [high_set_trips, high_pair], 'full house'
		elif high_pair:  # strange
			if high_pair:
				return [high_set_trips, high_pair], 'full house'
		elif flash:
			return flash, 'flash'
		elif straight:
			return straight, 'straight'
		else:
			h_cards = []
			for card in sort:
				if card not in high_set_trips:
					h_cards.append(card)
					if len(h_cards) == 2:
						break
			return [high_set_trips, h_cards], 'set trips'
	elif high_pair is not None and low_pair is not None:
		for card in sort:
			if card not in high_pair and card not in low_pair:
				h_cards = card
				two_pairs = [high_pair, low_pair, h_cards]
	elif high_pair is not None:
		pair = high_pair
		h_cards = []
		for card in sort:
			if card not in high_pair:
				h_cards.append(card)
				if len(h_cards) == 3:
					pair = [pair, h_cards]
					break
	if quads:
		raise Exception('Strange situation quads')
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
	             'full house', 'quads', 'straight flash')
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
		elif name1 == 'pair':
			p1 = combs1[0][0]
			h1 = combs1[1]
			p2 = combs2[0][0]
			h2 = combs2[1]
			if p1[0] > p2[0]:  # pair card compare
				return 'win'
			elif p1[0] < p2[0]:
				return 'lose'
			else:  # check high cards
				for n, card in enumerate(h1):
					if card[0] > h2[n][0]:  # card values
						return 'win'
					elif card[0] < h2[n][0]:
						return 'lose'
				else:
					raise Exception('Strange split ')
		elif name1 == 'two pairs':  # two pairs compare (parts)
			p11 = combs1[0][0]
			p12 = combs1[1][0]
			h1 = combs1[2]
			
			p21 = combs2[0][0]
			p22 = combs2[1][0]
			h2 = combs2[2]
			
			if p11[0] > p21[0]:  # high pair compare
				return 'win'
			elif p11[0] < p21[0]:
				return 'lose'
			else:  # low pair compare
				if p12[0] > p22[0]:  # low pair compare
					return 'win'
				elif p12[0] < p22[0]:
					return 'lose'
				else:
					if h1[0] > h2[0]:
						return 'win'
					elif h1[0] < h2[0]:
						return 'lose'
					else:
						raise Exception('Strange split')
		elif name1 == 'set trips':  # set or trips compare
			s1 = combs1[0][0]
			h1 = combs1[1]
			s2 = combs2[0][0]
			h2 = combs2[1]
			if s1[0] > s2[0]:  # any card compare
				return 'win'
			elif s1[0] < s2[0]:
				return 'lose'
			else:
				for n, card in enumerate(h1):
					if card[0] > h2[n][0]:  # card values
						return 'win'
					elif card[0] < h2[n][0]:
						return 'lose'
				else:
					raise Exception('Strange split ')
		elif name1 == 'straight flash' or name1 == 'flash' or name1 == 'straight' or name1 == 'high cards':
			# straight type compare by max card
			for i in range(4, -1, -1):
				if combs1[i][0] > combs2[i][0]:
					return 'win'
				elif combs1[i][0] < combs2[i][0]:
					return 'lose'
			else:
				return 'split'
		elif name1 == 'full house':
			s1 = combs1[0][0]
			p1 = combs1[1][0]
			s2 = combs2[0][0]
			p2 = combs2[1][0]
			if s1[0] > s2[0]:  # low pair compare
				return 'win'
			elif s1[0] < s2[0]:
				return 'lose'
			else:
				if p1[0] > p2[0]:  # low pair compare
					return 'win'
				elif p1[0] < p2[0]:
					return 'lose'
				else:
					raise Exception('Strange split')
		elif name1 == 'quads':  # pair compare
			q1 = combs1[0][0]
			h1 = combs1[1]
			
			q2 = combs2[0][0]
			h2 = combs2[1]
			
			if q1[0] > q1[0]:  # any card compare
				return 'win'
			elif q1[0] < q2[0]:
				return 'lose'
			else:
				if h1[0] > h2[0]:  # card values
					return 'win'
				elif h1[0] < h2[0]:
					return 'lose'
				else:
					raise Exception('Strange split')
		else:
			raise Exception(f'Unknown name {name1}')


def make_range(start_set=None, dead_cards_set=None):
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
		for f1 in range(cards_indexes - 2):
			for f2 in range(f1 + 1, cards_indexes - 1):
				for f3 in range(f2 + 1, cards_indexes):
					all_flops.append([all_cards[f1], all_cards[f2], all_cards[f3]])
		# print(len(all_flops))
		return flop, all_cards, all_flops
	else:
		return flop, all_cards


def gen_turn(dead_cards: set, all_=False):
	"""
	Generating turn
	:param all_: gen all flops or not
	:param dead_cards: dead cards (player or players and board)
	:return: range and list of 3 cards
	"""
	all_cards = list(make_range(dead_cards_set=dead_cards))
	turn = random.sample(all_cards, 4)
	if all_:
		# print(len(all_cards))
		all_turns = []
		cards_indexes = len(all_cards)
		for f1 in range(cards_indexes - 3):
			for f2 in range(f1 + 1, cards_indexes - 2):
				for f3 in range(f2 + 1, cards_indexes - 1):
					for f4 in range(f3 + 1, cards_indexes):
						all_turns.append([all_cards[f1], all_cards[f2], all_cards[f3], all_cards[f4]])
		# print(len(all_flops))
		return turn, all_cards, all_turns
	else:
		return turn, all_cards


def gen_river(dead_cards: set, all_=False):
	"""
	Generating river
	:param all_: gen all flops or not
	:param dead_cards: dead cards (player or players and board)
	:return: range and list of 3 cards
	"""
	all_cards = list(make_range(dead_cards_set=dead_cards))
	river = random.sample(all_cards, 4)
	if all_:
		# print(len(all_cards))
		all_rivers = []
		cards_indexes = len(all_cards)
		for f1 in range(cards_indexes - 4):
			for f2 in range(f1 + 1, cards_indexes - 3):
				for f3 in range(f2 + 1, cards_indexes - 2):
					for f4 in range(f3 + 1, cards_indexes - 1):
						for f5 in range(f4 + 1, cards_indexes):
							all_rivers.append([all_cards[f1], all_cards[f2], all_cards[f3], all_cards[f4], all_cards[f5]])
		return river, all_cards, all_rivers
	else:
		return river, all_cards


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
		return prev, all_cards, all_next
	else:
		prev = prev + [n]
		return prev, all_cards


def is_suited(hand):
	card1 = hand[0]
	card2 = hand[1]
	return card1[1] == card2[1]


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
		all_boards = []
		cards_indexes = len(all_cards)
		for f1 in range(cards_indexes - 4):
			for f2 in range(f1 + 1, cards_indexes - 3):
				for f3 in range(f2 + 1, cards_indexes - 2):
					for t in range(f3 + 1, cards_indexes - 1):
						for r in range(t + 1, cards_indexes):
							all_boards.append([all_cards[f1], all_cards[f2], all_cards[f3],
							                   all_cards[t], all_cards[r]])
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
		all_boards = gen_board(dead_cards=dead_cards, all_=True)[2]
		for n, board in enumerate(all_boards):
			print(n)
			result = h_vs_h_result(hand1=hand1, hand2=hand2, curr_board=board)
			compares += 1
			if result == 'win':
				h1_wins += 1
			elif result == 'lose':
				h2_wins += 1
			else:
				splits += 1
		percent_wins1 = h1_wins / compares
		percent_wins2 = h2_wins / compares
		percent_split = splits / compares
		eq1 = (h1_wins * 2 + splits) / (compares * 2)
		eq2 = (h2_wins * 2 + splits) / (compares * 2)
		return hand1, hand2, percent_wins1, percent_wins2, percent_split, eq1, eq2, h1_wins, h2_wins, splits, compares


def make_2_hands():
	all_cards = list(make_range())
	all_hands = []
	for c1, card1 in enumerate(all_cards[:-3]):
		for c2, card2 in enumerate(all_cards[c1:-2]):
			for c3, card3 in enumerate(all_cards[c2:-1]):
				for c4, card4 in enumerate(all_cards[c3:]):
					all_hands.append(((card1, card2), (card3, card4)))
	return all_hands


def main():
	"""
	Simulations
	"""
	# hand_1 = [(5, 3), (11, 1)]
	# hand_2 = [(9, 3), (12, 1)]
	# data = [hand_equity(hand1=hand_1, hand2=hand_2)]
	# save_to_csv(data)
	# pprint.pprint(make_2_hands())
	# print(len(make_2_hands()))
	hand_2 = ((10, 2), (14, 1))
	board = ((11, 2), (8, 2), (7, 2), (9, 2))
	print(make_comb(hand=hand_2, board=board))


if __name__ == '__main__':
	main()
