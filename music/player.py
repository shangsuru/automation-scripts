"""
Can read and write songs in the format
"[index];[link];[description]" to a specified
text file and delete them.

Opens the selected song in a new full-screen browser window.
"""


class MusicPlayer:
    def __init__(self, path):
        self.path = path
        self.songs = []
        with open(path) as musicFile:
            lines = musicFile.readlines()
            for line in lines:
                self.songs.append(tuple(line.split(";")))

    def play(self, index):
        pass

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
            del self.songs[index]
        with open(self.path, "w") as musicFile:
            for newIndex, song in enumerate(self.songs):
                link, description = song[1:]
                musicFile.write(f"{newIndex};{link};{description}")

    def show(self):
        return self.songs
