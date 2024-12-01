import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		self.seen = True	

class Playlist:
	def __init__(self, name, descaption, ratting, videos):
		self.name = name
		self.descaption = descaption
		self.ratting = ratting
		self.videos = videos

def read_video():
	title = input("Enter title video: ") + "\n"
	link = input("Enter link video: ") + "\n"
	video = Video(title, link)
	return video

def print_video(video):
	print("Video title: ", video.title, end = "")
	print("Video link: ", video.link, end = "")

def read_videos():
	videos = []
	total_video = int(input("Enter how many videos: "))
	for i in range(total_video):
		print("------")
		print("Video " + str(i + 1))
		vid = read_video()
		videos.append(vid)
	return videos

def print_videos(videos):
	print("...............")
	for i in range(len(videos)):
		print("Video " + str(i + 1) + ":")
		print_video(videos[i])

def write_video_to_txt(videos, file):
	file.write(videos.title)
	file.write(videos.link)

def write_videos_to_txt(videos, file):
	file.write(str(len(videos)) + "\n")
	for i in range(len(videos)):
		write_video_to_txt(videos[i], file)

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

def read_playlist():
	playlist_name = input("Enter name playlist: ") + "\n"
	playlist_descaption = input("Enter descaption playlist: ") + "\n"
	playlist_ratting = input("Enter ratting playlist (1 - 5): ") + "\n"
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_descaption, playlist_ratting, playlist_videos)
	return playlist

def write_playlist_to_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.descaption)
		file.write(playlist.ratting)
		write_videos_to_txt(playlist.videos, file)

def read_playlist_to_txt():
	with open("data.txt", "r") as file:
		playlist_name = file.readline()
		playlist_descaption = file.readline()
		playlist_ratting = file.readline()
		playlist_videos = read_videos_to_txt(file)
		playlist = Playlist(playlist_name, playlist_descaption, playlist_ratting, playlist_videos)
	return playlist

def print_playlist(playlist):
	print("_____")
	print("Playlist name: " + playlist.name, end = "")
	print("Playlist descaption: " + playlist.descaption, end = "")
	print("Playlist ratting: " + playlist.ratting, end = "")
	print_videos(playlist.videos)

def show_menu():
	print("           | MAIN MENU |           ")
	print("-----------------------------------")
	print("| Option 1: Creative to playlist. |")
	print("| Option 2: Show playlist.        |")
	print("| Option 3: Play Videos.          |")
	print("| Option 4: Add Video.            |")
	print("| Option 5: Update playlist.      |")
	print("| Option 6: Delete Video.         |")
	print("| Option 7: Save to Exit.         |")
	print("-----------------------------------")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)

	choice = int(choice)
	return choice

def play_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)

	choice = select_in_range("Select a video (1, " + str(total) + "): " , 1 ,total)
	print("Open video: " + playlist.videos[choice - 1].title + "-" + playlist.videos[choice - 1].link, end = "")
	playlist.videos[choice - 1].open()

def add_videos(playlist):
	print("-----|Enter Add Your Video|-----")

	new_video_title = input("Add new video title: ") + "\n"
	new_video_link = input("Add new video link: ") + "\n"
	
	new_video =Video(new_video_title, new_video_link)
	playlist.videos.append(new_video)

	return playlist

def update_playlist(playlist):
	print("-----|Update Playlist?|-----")
	print("| 1. Name                  |")
	print("| 2. Descaption            |")
	print("| 3. Ratting               |")
	print("----------------------------")

	choice = select_in_range("Select an option (1 - 3): ", 1, 3)
	if choice == 1:
		new_playlist_name = input("Enter new name for playlist: ") + "\n"
		playlist.name = new_playlist_name
		print("Updated Successfully !!!")
		return playlist
	if choice == 2:
		new_playlist_descaption = input("Enter new descaption for playlist: ") + "\n"
		playlist.descaption = new_playlist_descaption
		print("Updated Successfully !!!")
		return playlist
	if choice == 3:
		new_playlist_ratting = str(select_in_range("Enter new ratting for playlist(1 - 5): ", 1, 5)) + "\n"
		playlist.ratting = new_playlist_ratting
		print("Updated Successfully !!!")
		return playlist	

def delete_playlist(playlist):
	print_playlist(playlist)
	choice = select_in_range("Enter a delete video (1 - " + str(len(playlist.videos)) + "): ", 1 , int(len(playlist.videos)))
	new_videos_list = []
	for i in range(len(playlist.videos)):
		if i == choice - 1:
			continue
		
		new_videos_list.append(playlist.videos[i])

	playlist.videos = new_videos_list
	print("Remove Successfully !!!")
	
	return playlist

def main():
	
	try:
		playlist = read_playlist_to_txt()
		print("Loadinggg...........")
	except:
		print("Welcome, first user!!")

	while True:
		show_menu()
		choice = select_in_range("Select an option (1 - 7): ", 1, 7)
		if choice == 1:
			playlist = read_playlist()
			input("\nPress Enter to continue.\n")
		elif choice == 2:
			print_playlist(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 3:
			play_video(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 4:
			playlist = add_videos(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 5:
			playlist = update_playlist(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 6:
			playlist = delete_playlist(playlist)
			input("\nPress Enter to continue.\n")		
		elif choice == 7:
			write_playlist_to_txt(playlist)
			print("Save Data Successfully !!!! ")
			input("\nPress Enter to continue.\n")
			break

main()