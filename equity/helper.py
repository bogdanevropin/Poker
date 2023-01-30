"""
Helps to make solution
"""
import os
from PIL import Image
import random

from tools import card_to_nums, make_comb


def ask_hand():
	"""
	Asks and process player's hand
	:return: True, (current_hand_n, current_hand_str, currents_hand_s) or False, None
	"""
	hand = input("""Input your hand by value:
2 3 4 5 6 7 8 9 T J Q K A
and suit:
d for diamonds ♦
s for spades ♠
h for harts ♥
c for clubs ♣
2c4d
is 2♣4♦
JhQh
is J♥Q♥
Input your hand \n""")
	c1 = hand[0].upper() + hand[1].lower()
	c2 = hand[2].upper() + hand[3].lower()
	
	c1 = card_to_nums(c1)
	c2 = card_to_nums(c2)
	
	if hand[1] == hand[3]:
		s = 's'
	else:
		s = 'o'
	if c1 and c2:
		print('Normally card input')
	else:
		print('Invalid cards, restart algorithm. . .')
		return False, None
	if c1 == c2:
		print('Same cards, restart algorithm. . .')
		return False, None
	c1_nums, c1_str = c1
	c2_nums, c2_str = c2
	if c1_nums[0] > c2_nums[0]:
		c1_nums, c1_str = c2
		c2_nums, c2_str = c1
	current_hand_n = (c1_nums, c2_nums)
	current_hand_str = f'{c1_str}{c2_str}'
	currents_hand_s = f'{c1_str[0]}{c2_str[0]}' + s
	i = input(
		f'{current_hand_str} ({currents_hand_s}) - Is your hand? "Y" for Continue and "N" for type cards again\n')
	if i and i.upper():
		return True, (current_hand_n, current_hand_str, currents_hand_s)
	else:
		return False, None


def ask_num_players_and_pos():
	"""
	Asks number of players and info about positions
	:return: None, None, None or number_of_payers, y_p, active_players
	"""
	number_of_payers = input('How many players at table (max 6 min 2)\n')
	if not number_of_payers.isnumeric():
		print('Please input Integer num of players at table (max 6 min 2)')
		return None, None, None
	else:
		number_of_payers = float(number_of_payers)
		if not number_of_payers.is_integer():
			print('Please input Integer num of players at table (max 6 min 2)')
			return None, None, None
		else:
			number_of_payers = int(number_of_payers)
	
	def ask_pos(n_p):
		"""
		pos ask
		:param n_p: number of active players at table
		:return: number_of_payers, y_p, active_players or None, None, None
		"""
		all_positions = ['ep', 'mp', 'co', 'btn', 'sb', 'bb']
		active_players = all_positions[-n_p:]
		y_p = input(f'Your position: \n{active_players}\n')
		if y_p not in all_positions:
			return None, None, None
		else:
			return number_of_payers, y_p, active_players
	
	info = None
	while info is None:
		info = ask_pos(n_p=number_of_payers)
	
	return info


def ask_street_actions(info, active_p_i, board=None):
	street = None
	if board is None:
		street = 'preflop'
	elif len(board) == 3:
		street = 'flop'
	elif len(board) == 4:
		street = 'turn'
	elif len(board) == 5:
		street = 'river'
	new_active_p = []
	raises_amount = 0
	pot_status = 'or'
	current_bet = 0
	players_in_pot = []
	player_bets = {}
	prev_raisers = []
	
	active_p = active_p_i[0]
	your_pos = active_p_i[1]
	your_hand_i = info[0]
	curr_dir = os.getcwd()
	for p in active_p:
		bet = 'n'
		if p != your_pos:  # check prev moves
			while not bet.isnumeric() or 0 < int(bet) < current_bet:
				bet = input(f'Player {p} bets amount:')
			if bet != '0':
				bet = int(bet)
				if bet > current_bet:
					current_bet = bet
					raises_amount += 1
					prev_raisers.append(p)
				players_in_pot.append(p)
				player_bets[p] = [bet]
				new_active_p.append(p)
		else:  # your decision help chart
			if raises_amount == 0:
				im = Image.open(curr_dir + '\\pre_flop\\charts\\preflop or.jpg')
				colours = ['DEEP BLUE', 'LIGHT BLUE', 'DEEP PURPLE', 'LIGHT PURPLE', 'YELLOW', 'GREEN']
				poses = ['ep', 'mp', 'co', 'btn', 'sb']
				a = poses.index(p)
				need_colours = ''.join(f'{colour}, ' for colour in colours[:a+1])
				print(f'If your hand in {need_colours}\n'
				      f'And sometimes with {colours[a+1]} you are Recommended to make a 3bb (Big Blind) raise')
				r = random.randint(0, 100)
				if r > 49:
					print(f'Dice say {r} > 49 of 0-99, recommend to raise {colours[a+1]} too')
				else:
					print(f'Dice say {r} <= 49 of 0-99, NOT recommend to raise {colours[a+1]}...')
				im.show(title=f'Preflop open raise {p} (raise first) help chart')
			if raises_amount == 1:
				# pot_status = '3b'
				if p in ['mp', 'co', 'btn']:
					im = Image.open(curr_dir + '\\pre_flop\\charts\\mp or co or btn vs ep.jpg')
					print(f'Follow colour Instructions')
					im.show(title=f'Preflop {p} react to open raise (or) help chart')
				else:
					raiser = prev_raisers[0]
					print(f'Follow colour Instructions')
					im = Image.open(curr_dir + f'\\pre_flop\\charts\\{p}\\{p} vs {raiser},or.jpg')
					im.show(title=f'Preflop {p} react to open raise (or) help chart')
	return None


def check_combs(hand_info, boards):
	current_hand_nums, current_hand_string, currents_hand_suits = hand_info
	pocket_pair = False
	if current_hand_string[0] == current_hand_string[2]:
		pocket_pair = True
	board_len = len(boards[0])
	if board_len == 3:
		b = 'FLOPS'
	elif board_len == 4:
		b = 'TURNS'
	elif board_len == 5:
		b = 'RIVERS'
	else:
		raise Exception(f'Strange boards length {boards[0]}')
	high_card_combs = 0
	pair_combs = 0
	if pocket_pair:
		pair_pos = [0] * (board_len + 1)
	else:
		pair_pos = [0] * board_len
	two_pair_combs = 0
	if pocket_pair:
		two_pair_pos = [[0] * board_len] * board_len
	else:
		two_pair_pos = [[0] * board_len] * board_len
	set_flop = 0
	trips_combs = 0
	set_pos = None
	trips_pos = None
	if pocket_pair:
		set_pos = [0] * board_len
	else:
		trips_pos = [0] * board_len
	straight_combs = 0
	flash_combs = 0
	nut_flash = 0  # nuts flash
	l_flash = 0  # nuts flash
	# board_flash = 0
	full_house_combs = 0
	full_house_pos_set = None
	full_house_pos_pair = None
	full_house_pos_unp = None
	if pocket_pair:
		full_house_pos_set = [0] * (board_len - 2)  # 2 slots for pair
		full_house_pos_pair = [0] * (board_len - 1)  # 3 slots for trips + 1 underpair/over pair
	else:
		full_house_pos_unp = [0] * (board_len - 2)  # 2 slots for pair on board
	quads_combs = 0
	straight_flash_combs = 0
	all_combs = len(boards)
	for board in boards:
		board_sorted = sorted(board, key=lambda tup: tup[0], reverse=True)  # from upper to lower
		# sorted by card value flop
		comb_cards, board_comb = make_comb(hand=current_hand_nums, board=board_sorted)
		if board_comb == 'straight flash':
			straight_flash_combs += 1
		elif board_comb == 'quads':
			quads_combs += 1
		elif board_comb == 'full house':
			full_house_combs += 1
			if pocket_pair:
				if comb_cards[0][0][0] == current_hand_nums[0][0]:  # poket mair make 3 in full (2 card in sorted in 3)
					max_i = 0
					for c in board_sorted:
						if c in comb_cards[0]:
							break
						else:
							if c not in comb_cards[1]:
								max_i += 1
					full_house_pos_set[max_i] += 1
				else:
					max_i = 0
					card_v = current_hand_nums[0][0]
					for c in board_sorted:
						if c not in comb_cards[0]:  # not set part
							if card_v < c[0]:
								max_i += 1
							else:
								break
					if max_i > 2:
						print()
					full_house_pos_pair[max_i] += 1
			else:
				max_i = 0
				card_v = current_hand_nums[0]
				if card_v in comb_cards[0]:  # it is in set
					card_v = current_hand_nums[1][0]  # we need paired card value
				else:
					card_v = current_hand_nums[0][0]
				for c in board_sorted:
					if c not in comb_cards[0]:
						if card_v < c[0]:
							max_i += 1
							card_v = c[0]
						else:
							break
				full_house_pos_unp[max_i] += 1
		elif board_comb == 'flash':
			flash_combs += 1
			comb_cards = sorted(comb_cards, key=lambda tup: tup[0], reverse=True)
			max_i = 14
			# max_h_i = current_hand_nums[1]
			# if max_h_i in comb_cards:
			# 	max_h_i = current_hand_nums[1][0]
			# elif current_hand_nums[0] in comb_cards:
			# 	max_h_i = current_hand_nums[0][0]
			# else:
			# 	board_flash += 1
			flag = False
			for c in comb_cards:
				if c[0] == max_i:  # eah - 1
					max_i -= 1
					continue
				else:
					if current_hand_nums[0][0] == max_i+1 or\
						current_hand_nums[1][0] == max_i+1:
						flag = True
					break
			if flag:
				nut_flash += 1
			else:
				l_flash += 1
		elif board_comb == 'straight':
			straight_combs += 1
		elif board_comb == 'set trips':
			if pocket_pair:
				set_flop += 1
				max_i = 0
				card_v = current_hand_nums[0][0]
				for c in board_sorted:
					if card_v < c[0]:
						max_i += 1
					else:
						break
				set_pos[max_i] += 1
			else:
				trips_combs += 1
				flag = True
				if current_hand_nums[0] in comb_cards[0]:
					card_v = current_hand_nums[0][0]
				elif current_hand_nums[1] in comb_cards[0]:
					card_v = current_hand_nums[1][0]
				else:
					flag = False
					trips_pos[-1] += 1
					card_v = current_hand_nums[1][0]
				if flag:
					max_i = 0
					for c in board_sorted:
						if card_v < c[0]:
							max_i += 1
						else:
							break
					trips_pos[max_i] += 1
		elif board_comb == 'two pairs':
			two_pair_combs += 1
			if pocket_pair:
				pass
		elif board_comb == 'pair':
			pair_combs += 1
			if pocket_pair:
				max_i = 0
				for c in board_sorted:
					if comb_cards[0][0][0] < c[0]:
						max_i += 1
					else:
						break
				pair_pos[max_i] += 1
			else:
				max_i = 0
				for c in board_sorted:
					if comb_cards[0][0][0] < c[0]:
						max_i += 1
					else:
						break
				pair_pos[max_i] += 1
		else:  # 'high cards'
			high_card_combs += 1
	print(f'Preflop analysis:')
	print(f'All {b} generated: {all_combs} amount')
	print(f'STRAIGHT FLASH: {round((straight_flash_combs / all_combs) * 100, 5)} % '
	      f'({straight_flash_combs} combs / {all_combs})')
	print(f'QUADs ------- : {round((quads_combs / all_combs) * 100, 5)} % '
	      f'({quads_combs} combs / {all_combs})')
	print()
	print(f'FUll-HOUSE -- : {round((full_house_combs / all_combs) * 100, 5)} % '
	      f'({full_house_combs} combs / {all_combs})')
	if pocket_pair:
		for p, c in enumerate(full_house_pos_set):
			print(f'3-kind pos - {p+1}: {round((c / all_combs) * 100, 5)} % '
			      f'({round((c / full_house_combs) * 100, 5)} % ) ')
			if full_house_combs != 0:
				print(f'({c} combs / {full_house_combs})')
		for p, c in enumerate(full_house_pos_pair[:-1]):
			print(f'Pair pos --- {p + 1}: {round((c / all_combs) * 100, 5)} % '
			      f'({round((c / full_house_combs) * 100, 5)} %) ')
			if full_house_combs != 0:
				print(f'({c} combs / {full_house_combs})')
		print(f'Underpair --- : {round((full_house_pos_pair[-1] / all_combs) * 100, 5)} % ')
		if full_house_combs != 0:
			print(f'({round((full_house_pos_pair[-1] / full_house_combs) * 100, 5)} %) '
			      f'({full_house_pos_pair[-1]} combs / {full_house_combs})')
	else:
		for p, c in enumerate(full_house_pos_unp):
			print(f'Pair pos {p + 1} -- : {round((c / all_combs) * 100, 5)} % ')
			if full_house_combs != 0:
				print(f'({round((c / full_house_combs) * 100, 5)} %) '
				      f'({full_house_combs} combs / {all_combs})')
	print()
	print(f'FLASH ------- : {round((flash_combs / all_combs) * 100, 5)} % '
	      f'({flash_combs} combs / {all_combs})')
	if flash_combs != 0:
		print(f'Best Flash -- : {round((nut_flash / flash_combs) * 100, 5)} % '
		      f'({nut_flash} combs / {flash_combs})')
		print(f'Low Flash --- : {round((l_flash / flash_combs) * 100, 5)} % '
		      f'({l_flash} combs / {flash_combs})')
	print()
	print(f'STRAIGHT ---- : {round((straight_combs / all_combs) * 100, 5)} % '
	      f'({straight_combs} combs / {all_combs} {b})')
	print()
	if pocket_pair:
		sets_sum = sum(set_pos)
		print(f'SET --------- : {round((set_flop / all_combs) * 100, 5)} % '
		      f'({set_flop} combs / {all_combs} {b})\n')
		for p, c in enumerate(set_pos):
			if sets_sum != 0:
				print(f'SET pos --- {p+1} : {round((c / sets_sum) * 100, 5)} % '
				      f'({round((c / sets_sum) * 100, 5)} %)'
				      f'({set_flop} combs / {all_combs})')
	else:
		print(f'TRIPS ------- : {round((trips_combs / all_combs) * 100, 5)} % '
		      f'({trips_combs} combs / {all_combs})')
		trips_sum = sum(trips_pos)
		for p, c in enumerate(trips_pos[:-1]):
			if trips_sum != 0:
				print(f'TRIPS pos -- {p+1}: {round((c / all_combs) * 100, 5)} % '
				      f'({round((c / trips_sum) * 100, 5)} %) '
				      f'({trips_combs} combs / {all_combs})')
		if trips_sum != 0:
			print(f'TRIPS on board: {round((trips_pos[-1] / all_combs) * 100, 5)} % '
			      f'({round((trips_pos[-1] / trips_sum) * 100, 5)} %) '
			      f'({trips_pos[-1]} combs / {all_combs})')
	print()
	print(f'TWO PAIRS --- : {round((two_pair_combs / all_combs) * 100, 5)} % '
	      f'({two_pair_combs} combs / {all_combs})')
	print()
	if pocket_pair:
		print(f'{current_hand_string} PAIR --- : {round((pair_combs / all_combs) * 100, 5)} % '
		      f'({pair_combs} combs / {all_combs})')
		for p, pos in enumerate(pair_pos):
			print(f'{current_hand_string} Pair -- {p}: {round((pos / all_combs) * 100, 5)} % '
			      f'({pos} combs / {all_combs})')
	else:
		print(f'PAIR -------- : {round((pair_combs / all_combs) * 100, 5)} % '
		      f'({pair_combs} combs / {all_combs})')
		for p, pos in enumerate(pair_pos):
			print(f'{current_hand_string} Pair -- {p+1}: {round((pos / all_combs) * 100, 5)} % '
			      f'({pos} combs / {all_combs})')
	if pocket_pair:
		print(f"You can't have high card combo, you already have pocket pair: {current_hand_string}")
	else:
		print(f'high cards -- : {round((high_card_combs / all_combs) * 100, 5)} % '
		      f'({high_card_combs} combs / {all_combs})')
	print('#'*70)


def preflop_help(hand_info, pos_i):
	"""
	Help with pre-flop decision
	:param hand_info: current_hand_nums, current_hand_string, currents_hand_suits
	:param pos_i: active pos for street and players_pos
	"""
	from tools import gen_flop, gen_turn, gen_river
	current_hand_nums, current_hand_string, currents_hand_suits = hand_info
	
	def give_extra_info(h_i=hand_info):
		all_flops = gen_flop(dead_cards=current_hand_nums, all_=True)[2]
		check_combs(hand_info=h_i, boards=all_flops)
		all_turns = gen_turn(dead_cards=current_hand_nums, all_=True)[2]
		check_combs(hand_info=h_i, boards=all_turns)
		all_rivers = gen_river(dead_cards=current_hand_nums, all_=True)[2]
		check_combs(hand_info=h_i, boards=all_rivers)
	a = input('Do you need extra info (Y/N)?\n').upper()
	if not a or a == 'Y':
		give_extra_info()
	
	new_actions = ask_street_actions(info=(hand_info, []), active_p_i=pos_i)
	return None, None, None


# def flop_help(start_info):
# 	"""
# 	Help on flop
# 	:param start_info:
# 	"""
# 	pass


# def turn_help(start_info):
# 	"""
# 	Help on turn
# 	:param start_info:
# 	"""
# 	pass
#
#
# def river_help(start_info):
# 	"""
# 	Help on river
# 	:param start_info:
# 	"""
# 	pass


def run_help():
	"""
	One play help
	"""
	
	hand_made = False
	info = None
	while not hand_made or info is None:
		hand_made, info = ask_hand()
	current_hand_nums, current_hand_string, currents_hand_suits = info
	number_of_payers = None
	all_active_pos = None
	your_pos = None
	while number_of_payers is None or your_pos is None:
		number_of_payers, your_pos, all_active_pos = ask_num_players_and_pos()
	pos_info = (all_active_pos, your_pos)
	if current_hand_nums is None \
		or current_hand_string is None \
		or currents_hand_suits is None \
		or number_of_payers is None \
		or all_active_pos is None \
		or your_pos is None:
		print('Invalid Data')
		return
	else:
		# start_info = ((current_hand_nums, current_hand_string, currents_hand_suits),
		#               (number_of_payers, your_pos, all_active_pos))
		hand_info = current_hand_nums, current_hand_string, currents_hand_suits
		flop_pot, flop, info_before_flop = preflop_help(hand_info=hand_info, pos_i=pos_info)


# flop_info = flop_pot, flop, info_before_flop
# turn_pot, turn, info_before_turn = flop_help(flop_info)
# turn_info = turn_pot, turn, info_before_turn
# river_pot, river, info_before_river = turn_help(turn_info)
# river_info = river_pot, river, info_before_river
# river_help(river_info)


def main():
	"""
	Helping
	"""
	
	i = input('Press Enter for continue and "STOP" or "S" for stop helping\n')
	if i and i.upper() != 'S' or i.upper() != 'STOP':
		flag = True
	else:
		flag = False
	while flag:
		run_help()
		i = input('Press Enter for continue and "STOP" or "S" for stop helping')
		if i and i.upper() != 'S' or i.upper() != 'STOP':
			flag = True
		else:
			flag = False


if __name__ == '__main__':
	main()
