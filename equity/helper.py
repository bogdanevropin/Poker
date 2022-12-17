"""
Helps to make solution
"""

from tools import card_to_nums


def ask_hand():
	"""
	Asks and process player's hand
	:return: True, (current_hand_n, current_hand_str, currents_hand_s) or False, None
	"""
	hand = input("""
		Input your hand by value:
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
	c1 = hand[:2]
	c2 = hand[2:4]
	
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
	c1_nums, c1_str = c1
	c2_nums, c2_str = c2
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


def preflop_help(start_info):
	"""
	Help with pre-flop decision
	:param start_info: current_hand_nums, current_hand_string, currents_hand_suits
	"""
	from tools import gen_flop
	current_hand_nums, current_hand_string, currents_hand_suits = start_info
	pocket_pair = False
	if current_hand_string[0] == current_hand_string[2]:
		pocket_pair = True
	all_flops = gen_flop(dead_cards=current_hand_nums, all_=True)[2]
	from tools import make_comb
	high_card_combs = 0
	pair_combs = 0
	two_pair_combs = 0
	trips_combs = 0
	set_combs = 0
	straight_combs = 0
	straight_1_dro = 0
	straight_2_dro = 0
	flash_combs = 0
	full_houses_combs = 0
	quads_combs = 0
	straight_flash_combs = 0
	all_combs = len(all_flops)
	for flop in all_flops:
		# if flop[0][1] == flop[1][1] == flop[2][1] == 2:
		# 		print()
		# 		print()
		comb_cards, flop_comb = make_comb(hand=current_hand_nums, board=flop)
		if flop_comb == 'straight flash':
			straight_flash_combs += 1
		elif flop_comb == 'quads':
			quads_combs += 1
		elif flop_comb == 'full house':
			full_houses_combs += 1
		elif flop_comb == 'flash':
			flash_combs += 1
		elif flop_comb == 'straight':
			straight_combs += 1
		elif flop_comb == 'set trips':
			if pocket_pair:
				set_combs += 1
			else:
				trips_combs += 1
		elif flop_comb == 'two pairs':
			two_pair_combs += 1
		elif flop_comb == 'pair':
			pair_combs += 1
		else:  # 'high cards'
			high_card_combs += 1
	print(f'Preflop analysis:')
	print(f'All flops generated: {all_combs} amount')
	print(f'STRAIGHT FLASH: {round((straight_flash_combs/all_combs)*100, 5)} % on flop '
	      f'({straight_flash_combs} combs / {all_combs} flops)')
	print(f'QUADs ------- : {round((quads_combs / all_combs) * 100, 5)} % on flop '
	      f'({quads_combs} combs / {all_combs} flops)')
	print(f'FUll-HOUSE -- : {round((full_houses_combs / all_combs) * 100, 5)} % on flop '
	      f'({full_houses_combs} combs / {all_combs} flops)')
	print(f'FLASH ------- : {round((flash_combs / all_combs) * 100, 5)} % on flop '
	      f'({flash_combs} combs / {all_combs} flops)')
	print(f'STRAIGHT ---- : {round((straight_combs / all_combs) * 100, 5)} % on flop '
	      f'({straight_combs} combs / {all_combs} flops)')
	print()
	if pocket_pair:
	print(f'3-of-kind --- : {round(((set_combs+trips_combs) / all_combs) * 100, 5)} % on flop '
	      f'({set_combs+trips_combs} combs / {all_combs} flops)\n'
	      f'SET --------- : {round((set_combs / all_combs) * 100, 5)} % on flop '
	      f'({set_combs} combs / {all_combs} flops)\n'
	      f'TRIPS ------- : {round((trips_combs / all_combs) * 100, 5)} % on flop '
	      f'({trips_combs} combs / {all_combs} flops)')
	print(f'TWO PAIRS --- : {round((two_pair_combs / all_combs) * 100, 5)} % on flop '
	      f'({two_pair_combs} combs / {all_combs} flops)')
	print(f'PAIR -------- : {round((pair_combs / all_combs) * 100, 5)} % on flop '
	      f'({pair_combs} combs / {all_combs} flops)')
	print(f'high cards -- : {round((high_card_combs / all_combs) * 100, 5)} % on flop '
	      f'({high_card_combs} combs / {all_combs} flops)')
	input()
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
		start_info = current_hand_nums, current_hand_string, currents_hand_suits
		flop_pot, flop, info_before_flop = preflop_help(start_info)
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
