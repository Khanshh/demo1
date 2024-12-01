import pygame
import pygame_gui
import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		print("Open " + self.title)
		self.seen = True	

class Playlist:
	def __init__(self, name, descaption, ratting, videos):
		self.name = name
		self.descaption = descaption
		self.ratting = ratting
		self.videos = videos



class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def draw(self):
		font = pygame.font.Font('ShadeBlue-2OozX.ttf', 35)
		text_render = font.render(self.text, True, (255, 255, 255))
		self.text_box = text_render.get_rect()	

		if self.is_mouse_on_text():
			text_render = font.render(self.text, True, (255, 0, 0))
			pygame.draw.line(screen, (255, 0, 0), (self.position[0], self.position[1] + self.text_box[3]), (self.position[0] + self.text_box[2], self.position[1] + self.text_box[3]))
		else:
			text_render = font.render(self.text, True, (255, 255, 255))

		screen.blit(text_render, self.position)	
	
	def is_key_on_text(self):
		pass		


	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x > self.position[0] and mouse_x < self.position[0] + self.text_box[2] and mouse_y > self.position[1] and mouse_y < self.position[1] + self.text_box[3]:
			return True
		return False	

def read_video_to_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_to_txt(file):
	videos = []
	total = file.readline()
	for i in range(int(total)):
		video = read_video_to_txt(file)
		videos.append(video)
	return videos

def read_playlist_to_txt(file):
	playlist_name = file.readline()
	playlist_descaption = file.readline()
	playlist_ratting = file.readline()
	playlist_videos = read_videos_to_txt(file)
	playlist = Playlist(playlist_name, playlist_descaption, playlist_ratting, playlist_videos)
	return playlist	

def read_playlists_to_txt():
	playlists = []
	with open("data.txt", "r") as file:
		total = file.readline()
		for i in range(int(total)):
			playlist = read_playlist_to_txt(file)
			playlists.append(playlist)
	return playlists		


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Playlist App')
manager = pygame_gui.UIManager((600, 400))
running = True
BLACK = (0,0,0)
clock = pygame.time.Clock()
backgroud_image = pygame.image.load("Playlist.jpg") 
backgroud_image = pygame.transform.scale(backgroud_image, (600, 400))

# Load data
playlists = read_playlists_to_txt()

playlists_btn_list = []
margin = 50 
for i in range(len(playlists)):
	playlists_btn = TextButton(playlists[i].name.rstrip(), (3, 3 + margin*i))
	playlists_btn_list.append(playlists_btn)

videos_btn_list = []


while running:		
	clock.tick(60)
	screen.fill(BLACK)
	screen.blit(backgroud_image, (0, 0))

	for i in range(len(playlists_btn_list)):
		playlists_btn_list[i].draw()

	for i in range(len(videos_btn_list)):
		videos_btn_list[i].draw()

	for event in pygame.event.get():
		if event.type ==pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in range(len(playlists_btn_list)):
					if playlists_btn_list[i].is_mouse_on_text():
						playlist_choice = i
						margin = 50
						videos_btn_list = [] 
						for j in range(len(playlists[i].videos)):
							videos_btn = TextButton(str(j + 1) + ". " + playlists[i].videos[j].title.rstrip(), (300, 3 + margin*j))
							videos_btn_list.append(videos_btn)
				
				if playlist_choice != None:
					for i in range(len(videos_btn_list)):
						if videos_btn_list[i].is_mouse_on_text():
							playlists[playlist_choice].videos[i].open()
						
		if event.type == pygame.QUIT:
			running = False	
				
	pygame.display.flip()

pygame.quit()