"""
Helps to make solution
"""

from tools import card_to_nums
import PIL


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
	if c1 == c2:
		print('Same cards, restart algorithm. . .')
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


def check_boards_combos(hand, hand_str, pocket_pair, boards):
	"""
	Check board combos
	:param hand: ((v1, s1), (v2, s2))
	:param hand_str: string hand
	:param pocket_pair: True or false
	:param boards: flop turn or river board list
	"""
	from tools import make_comb
	high_card_combs = 0
	pair_combs = 0
	over_pair = 0
	top_pair = 0
	second_pair = 0
	third_pair = 0
	under_pair = 0
	pair_board = 0
	two_pair_combs = 0
	two_pair_over_pair = 0
	two_pair_second_pair = 0
	two_pair_under_pair = 0
	two_pairs12 = 0
	two_pairs13 = 0
	two_pairs23 = 0
	two_pair1 = 0
	two_pair2 = 0
	trips_combs = 0
	set_combs = 0
	top_set = 0
	second_set = 0
	third_set = 0
	straight_combs = 0
	straight_1_dro = 0
	straight_2_dro = 0
	flash_combs = 0
	full_houses_combs = 0
	quads_combs = 0
	straight_flash_combs = 0
	all_combs = len(boards)
	for board in boards:
		board_sorted = sorted(board, key=lambda tup: tup[0])  # sorted by card value flop
		flop_v = [c[0] for c in board_sorted]
		comb_cards, flop_comb = make_comb(hand=hand, board=board)
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
				if board_sorted[-1][0] == hand[0][0]:
					top_set += 1
				elif board_sorted[-2][0] == hand[0][0]:
					second_set += 1
				else:
					third_set += 1
			else:
				trips_combs += 1
		elif flop_comb == 'two pairs':
			two_pair_combs += 1
			if pocket_pair:
				if board_sorted[-1][0] < hand[0][0]:
					two_pair_over_pair += 1
				elif board_sorted[-3][0] < hand[0][0]:
					two_pair_second_pair += 1
				else:
					two_pair_under_pair += 1
			else:
				if hand[1][0] in flop_v:
					p1_n = flop_v.index(hand[1][0])
					if hand[0][0] in flop_v:
						p2_n = flop_v.index(hand[0][0])
						if p1_n == 2 and p2_n == 1:
							two_pairs12 += 1
						elif p1_n == 2 and p2_n == 0:
							two_pairs13 += 1
						elif p1_n == 1 and p2_n == 0:
							two_pairs23 += 1
						else:
							raise Exception("Unknown 2 pair indexes error")
					else:
						if flop_v[1] > hand[1][0]:
							two_pair2 += 1
						else:
							two_pair1 += 1
				else:
					if flop_v[1] > hand[0][0]:
						two_pair2 += 1
					else:
						two_pair1 += 1
		elif flop_comb == 'pair':
			pair_combs += 1
			if pocket_pair:
				if board_sorted[-1][0] < hand[0][0]:
					over_pair += 1
				elif board_sorted[-2][0] < hand[0][0]:
					second_pair += 1
				elif board_sorted[-3][0] < hand[0][0]:
					third_pair += 1
				elif board_sorted[-3][0] > hand[0][0]:
					under_pair += 1
				else:
					raise Exception("Unknown 2 pair error")
			else:
				if board_sorted[-1][0] == hand[1][0] or \
					board_sorted[-1][0] == hand[0][0]:
					top_pair += 1
				elif board_sorted[-2][0] == hand[1][0] or \
					board_sorted[-2][0] == hand[0][0]:
					second_pair += 1
				elif board_sorted[-3][0] == hand[1][0] or \
					board_sorted[-3][0] == hand[0][0]:
					third_pair += 1
				elif board_sorted[-1][0] == board_sorted[-2][0] or \
					board_sorted[-2][0] == board_sorted[-3][0]:
					pair_board += 1
				else:
					raise Exception("Unknown pair error")
		else:  # 'high cards'
			high_card_combs += 1
	street = None
	if len(boards[0]) == 3:
		street = 'Flops'
	elif len(boards[0]) == 4:
		street = 'Turns'
	elif len(boards[0]) == 5:
		street = 'Rivers'
	print(f'Preflop analysis:')
	print(f'All {street} generated: {all_combs} amount')
	print(f'STRAIGHT FLASH: {round((straight_flash_combs / all_combs) * 100, 5)} % on {street} '
	      f'({straight_flash_combs} combs / {all_combs} {street})')
	print(f'QUADs ------- : {round((quads_combs / all_combs) * 100, 5)} % on {street} '
	      f'({quads_combs} combs / {all_combs} {street})')
	print(f'FUll-HOUSE -- : {round((full_houses_combs / all_combs) * 100, 5)} % on {street} '
	      f'({full_houses_combs} combs / {all_combs} {street})')
	print(f'FLASH ------- : {round((flash_combs / all_combs) * 100, 5)} % on {street} '
	      f'({flash_combs} combs / {all_combs} {street})')
	print(f'STRAIGHT ---- : {round((straight_combs / all_combs) * 100, 5)} % on {street} '
	      f'({straight_combs} combs / {all_combs} {street})')
	print()
	if pocket_pair:
		print(f'---- SET ---- : {round((set_combs / all_combs) * 100, 5)} % on {street} '
		      f'({set_combs} combs / {all_combs} {street})')
		print(f'    |  TOP SET: {round((top_set / all_combs) * 100, 5)} % on {street} '
		      f'({top_set} combs / {all_combs} {street})')
		print(f'    | 2-nd SET: {round((second_set / all_combs) * 100, 5)} % on {street} '
		      f'({second_set} combs / {all_combs} {street})')
		print(f'    | 3-rd SET: {round((third_set / all_combs) * 100, 5)} % on {street} '
		      f'({third_set} combs / {all_combs} {street})')
		print()
		print(f'- TWO PAIRS - : {round((two_pair_combs / all_combs) * 100, 5)} % on {street} '
		      f'({two_pair_combs} combs / {all_combs} {street})')
		print(f'  2p OVER pair: {round((two_pair_over_pair / all_combs) * 100, 5)} % on {street} '
		      f'({two_pair_over_pair} combs / {all_combs} {street})')
		print(f'  2p 2-nd pair: {round((two_pair_second_pair / all_combs) * 100, 5)} % on {street} '
		      f'({two_pair_second_pair} combs / {all_combs} {street})')
		print(f'  2p Underpair: {round((two_pair_under_pair / all_combs) * 100, 5)} % on {street} '
		      f'({two_pair_under_pair} combs / {all_combs} {street})')
		print()
		print(f'- {hand_str} PAIR - : {round((pair_combs / all_combs) * 100, 5)} % on {street} '
		      f'({pair_combs} combs / {all_combs} {street})')
		print(f'  |  OVER Pair: {round((over_pair / all_combs) * 100, 5)} % on {street} '
		      f'({over_pair} combs / {all_combs} {street})')
		print(f'  |  2-nd Pair: {round((second_pair / all_combs) * 100, 5)} % on {street} '
		      f'({second_pair} combs / {all_combs} {street})')
		print(f'  |  3-rd Pair: {round((third_pair / all_combs) * 100, 5)} % on {street} '
		      f'({third_pair} combs / {all_combs} {street})')
		print(f'  | Under Pair: {round((under_pair / all_combs) * 100, 5)} % on {street} '
		      f'({under_pair} combs / {all_combs} {street})')
		print(f"You can't have high card combo, you already have pocket pair: {hand_str}")
	else:
		print(f'--- TRIPS --- : {round((trips_combs / all_combs) * 100, 5)} % on {street} '
		      f'({trips_combs} combs / {all_combs} flops)')
		print()
		print(f'- TWO PAIRS - : {round((two_pair_combs / all_combs) * 100, 5)} % on {street} '
		      f'({two_pair_combs} combs / {all_combs} {street})')
		print(f'board p  & TOP: {round((two_pair1 / all_combs) * 100, 5)} % on {street} '
		      f'({two_pair1} combs / {all_combs} {street})')
		print(f'board & Second: {round((two_pair2 / all_combs) * 100, 5)} % on {street} '
		      f'({two_pair2} combs / {all_combs} {street})')
		print(f'TOP and Second: {round((two_pairs12 / all_combs) * 100, 5)} % on {street} '
		      f'({two_pairs12} combs / {all_combs} {street})')
		print(f' Top and third: {round((two_pairs13 / all_combs) * 100, 5)} % on {street} '
		      f'({two_pairs13} combs / {all_combs} {street})')
		print(f'Second & third: {round((two_pairs23 / all_combs) * 100, 5)} % on {street} '
		      f'({two_pairs23} combs / {all_combs} {street})')
		print()
		print(f' --- PAIR --- : {round((pair_combs / all_combs) * 100, 5)} % on {street} '
		      f'({pair_combs} combs / {all_combs} {street})')
		print(f' |    TOP pair: {round((top_pair / all_combs) * 100, 5)} % on {street} '
		      f'({top_pair} combs / {all_combs} {street})')
		print(f' | Second pair: {round((second_pair / all_combs) * 100, 5)} % on {street} '
		      f'({second_pair} combs / {all_combs} {street})')
		print(f' |  Third pair: {round((third_pair / all_combs) * 100, 5)} % on {street} '
		      f'({third_pair} combs / {all_combs} {street})')
		print(f' |  Board pair: {round((pair_board / all_combs) * 100, 5)} % on {street} '
		      f'({pair_board} combs / {all_combs} {street})')
		print()
		print(f' |  High cards: {round((high_card_combs / all_combs) * 100, 5)} % on {street} '
		      f'({high_card_combs} combs / {all_combs} {street})')


def preflop_help(start_info):
	"""
	Help with pre-flop decision
	:param start_info: current_hand_nums, current_hand_string, currents_hand_suits
	"""
	from tools import gen_flop
	current_hand_nums, current_hand_string, currents_hand_suits = start_info
	current_hand_nums = list(sorted(current_hand_nums, key=lambda card: card[0]))
	pocket_pair = False
	if current_hand_string[0] == current_hand_string[2]:
		pocket_pair = True
	all_flops = gen_flop(dead_cards=set(current_hand_nums), all_=True)[2]
	check_boards_combos(hand=current_hand_nums, hand_str=current_hand_string, pocket_pair=pocket_pair, boards=all_flops)
	from tools import gen_next_card
	all_turns = []
	for t, flop in enumerate(all_flops):
		dead_cards = set(current_hand_nums + flop)
		next_turns = gen_next_card(prev=flop, dead_cards=dead_cards, all_=True)[2]
		all_turns = all_turns + next_turns
		# print(t)
	check_boards_combos(hand=current_hand_nums, hand_str=current_hand_string, pocket_pair=pocket_pair, boards=all_turns)
	for r, turn in enumerate(all_turns):
		dead_cards = set(current_hand_nums + turn)
		next_turns = gen_next_card(prev=turn, dead_cards=dead_cards, all_=True)[2]
		all_turns = all_turns + next_turns
		# print(r)
	check_boards_combos(hand=current_hand_nums, hand_str=current_hand_string, pocket_pair=pocket_pair, boards=all_turns)
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
