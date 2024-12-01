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
        self.seen = True    

class Playlist:
    def __init__(self, name, descaption, rating, videos):
        self.name = name
        self.descaption = descaption
        self.rating = rating
        self.videos = videos

    def save_to_file(self, file):
        file.write(self.name + "\n")
        file.write(self.descaption + "\n")
        file.write(self.rating + "\n")
        file.write(str(len(self.videos)) + "\n")
        for video in self.videos:
            file.write(video.title + "\n")
            file.write(video.link + "\n")

    @staticmethod
    def load_from_file(file):
        name = file.readline().strip()
        descaption = file.readline().strip()
        rating = file.readline().strip()
        video_count = int(file.readline().strip())
        videos = []
        for _ in range(video_count):
            title = file.readline().strip()
            link = file.readline().strip()
            videos.append(Video(title, link))
        return Playlist(name, descaption, rating, videos)

# GUI và các chức năng liên quan
class PlaylistApp:
    def __init__(self):
        # Khởi tạo pygame và pygame_gui
        pygame.init()
        self.window_size = (800, 600)
        self.screen = pygame.display.set_mode(self.window_size)
        self.manager = pygame_gui.UIManager(self.window_size)
        self.clock = pygame.time.Clock()

        # Khởi tạo các nút giao diện
        self.playlist_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 50), (200, 50)),
                                                            text="Tạo Playlist", manager=self.manager)
        self.show_playlist_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 50)),
                                                                 text="Hiển thị Playlist", manager=self.manager)
        self.play_video_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 250), (200, 50)),
                                                              text="Chơi Video", manager=self.manager)
        self.add_video_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 350), (200, 50)),
                                                             text="Thêm Video", manager=self.manager)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 450), (200, 50)),
                                                         text="Thoát", manager=self.manager)

        # Các thành phần nhập liệu cho Playlist và Video
        self.playlist_name_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 120), (200, 30)),
                                                                      manager=self.manager)
        self.playlist_descaption_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 160), (200, 30)),
                                                                            manager=self.manager)
        self.playlist_rating_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 200), (200, 30)),
                                                                        manager=self.manager)

        self.video_title_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 290), (200, 30)),
                                                                     manager=self.manager)
        self.video_link_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 320), (200, 30)),
                                                                    manager=self.manager)

        self.playlist = None  # Playlist ban đầu

    def read_video(self):
        title = self.video_title_input.get_text()
        link = self.video_link_input.get_text()
        return Video(title, link)

    def read_playlist(self):
        playlist_name = self.playlist_name_input.get_text()
        playlist_descaption = self.playlist_descaption_input.get_text()
        playlist_rating = self.playlist_rating_input.get_text()
        playlist_videos = []
        video_title = self.video_title_input.get_text()
        video_link = self.video_link_input.get_text()
        if video_title and video_link:
            video = Video(video_title, video_link)
            playlist_videos.append(video)
        return Playlist(playlist_name, playlist_descaption, playlist_rating, playlist_videos)

    def show_playlist(self):
        if not self.playlist:
            print("Chưa có playlist!")
            return
        print(f"Playlist: {self.playlist.name}")
        print(f"Mô tả: {self.playlist.descaption}")
        print(f"Đánh giá: {self.playlist.rating}")
        for video in self.playlist.videos:
            print(f"Video: {video.title} - {video.link}")

    def play_video(self):
        if not self.playlist:
            print("Chưa có playlist!")
            return
        for i, video in enumerate(self.playlist.videos):
            print(f"{i + 1}. {video.title}")
        choice = int(input(f"Chọn video để mở (1-{len(self.playlist.videos)}): ")) - 1
        if 0 <= choice < len(self.playlist.videos):
            video = self.playlist.videos[choice]
            print(f"Mở video: {video.title} - {video.link}")
            video.open()

    def add_video(self):
        if not self.playlist:
            print("Chưa có playlist!")
            return
        print("Thêm video mới:")
        new_video = self.read_video()
        self.playlist.videos.append(new_video)
        print("Video đã được thêm!")

    def save_playlist(self, filename="playlist.txt"):
        if self.playlist:
            with open(filename, "w") as file:
                self.playlist.save_to_file(file)
            print("Playlist đã được lưu vào file!")

    def load_playlist(self, filename="playlist.txt"):
        try:
            with open(filename, "r") as file:
                self.playlist = Playlist.load_from_file(file)
            print("Playlist đã được tải từ file!")
        except FileNotFoundError:
            print("Không tìm thấy file playlist!")

    def run(self):
        # Vòng lặp chính của giao diện
        running = True
        while running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.manager.process_events(event)

            # Cập nhật giao diện
            self.manager.update(time_delta)

            # Kiểm tra các nút được nhấn
            if self.playlist_button.check_pressed():
                self.playlist = self.read_playlist()
                print("Playlist đã được tạo!")
            if self.show_playlist_button.check_pressed():
                self.show_playlist()
            if self.play_video_button.check_pressed():
                self.play_video()
            if self.add_video_button.check_pressed():
                self.add_video()
            if self.quit_button.check_pressed():
                self.save_playlist()  # Lưu playlist vào file khi thoát
                running = False

            # Vẽ màn hình
            self.screen.fill((255, 255, 255))
            self.manager.draw_ui(self.screen)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    app = PlaylistApp()
    app.load_playlist()  # Tải playlist từ file nếu có
    app.run()
