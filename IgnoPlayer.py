import tkinter as tk
from tkinter import ttk

from MusicPlayer import MusicPlayer


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.style = ttk.Style()
        self.dark_mode = True
        self.player = MusicPlayer(self.window)
        self.Buttons = {
            "play_button": tk.Button(self.window, text = ' ▶ ', command = self.player.play),
            "stop_button": tk.Button(self.window, text = ' ⏹ ', command = self.player.stop),
            "pause_button": tk.Button(self.window, text = '⏸', command = self.player.pause),
            "prev_button": tk.Button(self.window, text = ' ⏮ ', command = self.player.previous_track),
            "next_button": tk.Button(self.window, text = ' ⏭ ', command = self.player.next_track),
            "select_folder_button": tk.Button(self.window, text = 'Select Folder', command = self.player.select_folder),
            "dark_mode_button": tk.Button(self.window, text = 'Dark Mode', command = self.toggle_dark_mode, bg = "#34495E", fg = "white"),
            "progress_bar": ttk.Progressbar(self.window, orient = 'horizontal', length = 700, mode = 'determinate', style = 'TProgressbar')
        }

    def update_progress_bar(self):
        if not self.player.is_playing and not self.player.is_paused and self.player.current_time < self.player.song_duration:
            self.Buttons['progress_bar']['value'] = self.player.current_time
            self.player.current_time += 1
            self.window.after(500, self.update_progress_bar)
        elif self.player.is_playing:
            self.Buttons['progress_bar']['value'] = 0
            self.player.is_playing = False

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.update_theme()

    def update_theme(self):
        if self.dark_mode:
            # Apply dark theme
            self.window.configure(bg = "#121212")
            self.Buttons['play_button'].configure(bg = "#008CBA", fg = "white")
            self.Buttons['stop_button'].configure(bg = "#F24D31", fg = "white")
            self.Buttons['pause_button'].configure(bg = "#FFA500", fg = "white")
            self.Buttons['prev_button'].configure(bg = "#34495E", fg = "white")
            self.Buttons['next_button'].configure(bg = "#34495E", fg = "white")
            self.Buttons['select_folder_button'].configure(bg = "#34495E", fg = "white")
            self.style.configure("TProgressbar", thickness = 10, troughcolor = "#121212", background = "#2ECC71")
        else:
            # Apply light theme
            self.window.configure(bg="#f0f0f0")
            self.Buttons['play_button'].configure(bg="#008CBA", fg="white")
            self.Buttons['stop_button'].configure(bg="#F24D31", fg="white")
            self.Buttons['pause_button'].configure(bg="#FFA500", fg="white")
            self.Buttons['prev_button'].configure(bg = "#34495E", fg = "white")
            self.Buttons['next_button'].configure(bg = "#34495E", fg = "white")
            self.Buttons['select_folder_button'].configure(bg = "#34495E", fg = "white")
            self.style.configure("TProgressbar", thickness = 10, troughcolor = "#f0f0f0", background = "#008CBA")

    def create_gui(self):
        self.window.title("IgnoPlayer")

        # Customize the appearance with some styling
        self.window.geometry("1000x700")  # Set window size
        self.window.configure(bg = "#f0f0f0")  # Set background color

        self.style.theme_use("clam")
        self.style.configure("TProgressbar", thickness = 10, troughcolor = "#f0f0f0", background = "#008CBA")

        # label = tk.Label(player.window, text="IgnoPlayer", bg="#f0f0f0", font=("Arial", 16))
        # label.pack(pady=10)

        self.Buttons['play_button'].pack(side = tk.LEFT, padx = 10)
        self.Buttons['stop_button'].pack(side = tk.LEFT, padx = 10)
        self.Buttons['pause_button'].pack(side = tk.LEFT, padx = 10)
        self.Buttons['prev_button'].pack(side = tk.LEFT, padx = 10)
        self.Buttons['next_button'].pack(side = tk.LEFT, padx = 10)
        self.Buttons['select_folder_button'].pack(side = tk.LEFT, padx = 10)
        self.Buttons['dark_mode_button'].pack(side=tk.LEFT, padx=10)
        self.Buttons['progress_bar'].pack(side=tk.BOTTOM, padx=20, pady=10)

        self.update_theme()

        self.window.mainloop()


if __name__ == "__main__":
    app_window = Window()

    # Create gui to open player and player window
    app_window.create_gui()
