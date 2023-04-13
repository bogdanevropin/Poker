"""
Game interface
"""
import os

from PIL import Image
import pygame


def main():
	"""
	Run game
	"""
	pygame.init()
	curr_dir = os.getcwd()
	table = pygame.image.load(curr_dir + '\\images\\table.png')
	table_image = Image.open(curr_dir + '\\images\\table.png')
	table_size = table_image.size
	table_w, table_h = table_size
	table_win = pygame.display.set_mode(table_size)
	pygame.display.set_caption('Poker')
	# bet = 0
	
	run = True
	while run:
		pygame.time.delay(100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		table_win.blit(table, (0, 0))
		pygame.display.update()
	pygame.quit()


if __name__ == '__main__':
	main()
