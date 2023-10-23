import os

import pygame
import tkinter as tk
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.queue = []
        self.current_index = 0
        self.folder_path = ""
        self.paused = False
        self.mixer = pygame.mixer
        self.listbox = None

        if not self.mixer.get_init():
            self.mixer.init()

    def play(self):
        if not self.queue:
            return

        if self.paused:
            self.mixer.music.unpause()
            self.paused = False
        else:
            self.mixer.music.load(self.queue[self.current_index])
            self.mixer.music.play()

    def stop(self):
        self.mixer.music.stop()
        self.paused = False

    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True

    def next_track(self):
        if self.queue:
            self.current_index = (self.current_index + 1) % len(self.queue)
            self.play()
        else:
            self.paused = False

    def previous_track(self):
        if self.queue:
            self.current_index = (self.current_index - 1) % len(self.queue)
            self.play()
        else:
            self.paused = False

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            selected_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith(('.mp3', '.wav', '.flac'))]
            selected_files = [os.path.join(self.folder_path, file) for file in selected_files]

            if selected_files:
                self.queue = selected_files
                file_names = [os.path.basename(file) for file in selected_files]

                if self.listbox:
                    self.listbox.destroy()  # Destroy the old Listbox if it exists

                listbox = tk.Listbox(self.window, selectbackground = "#008CBA", font = ("Arial", 12))
                listbox.pack(fill = tk.BOTH, expand = True, padx = 20, pady = 10)

                for name in file_names:
                    listbox.insert(tk.END, name)


if __name__ == "__main__":
    print('This file is not supposed to be called by itself, but you are free to do whatever you want ;)')
