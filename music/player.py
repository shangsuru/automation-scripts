"""
Can read and write songs in the format
"[index];[link];[description]" to a specified
text file and delete them.

Opens the selected song in a new browser window.
"""

from random import randint
import webbrowser


class MusicPlayer:
    def __init__(self, path):
        self.path = path
        self.songs = []

        # Copy every song from file into songs list
        with open(path) as musicFile:
            lines = musicFile.readlines()
            for line in lines:
                self.songs.append(tuple(line.split(";")))

    def play(self, index=None):
        if not index:
            index = randint(0, len(self.songs) - 1)
        elif index >= len(self.songs):
            return

        songToPlay = self.songs[index]
        url = songToPlay[1].replace("\\", "")
        webbrowser.open_new(url)

    def store(self, link, description):
        index = len(self.songs)
        link.replace(";", "")
        description.replace(";", ".")

        self.songs.append((index, link, description))
        with open(self.path, "a") as musicFile:
            musicFile.write(f"{index};{link};{description}")
            musicFile.write("\n")

    def remove(self, indexes):
        for index in sorted(indexes, reverse=True):
            if index >= len(self.songs):
                continue
            del self.songs[index]

        with open(self.path, "w") as musicFile:
            for newIndex, song in enumerate(self.songs):
                link, description = song[1:]
                musicFile.write(f"{newIndex};{link};{description}")

    def show(self):
        return self.songs
