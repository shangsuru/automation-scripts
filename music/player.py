"""
Can read and write and delete songs in the format
"[index];[link];[description]" to a specified
text file. 

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
        index = len(self.songs) + 1
        link.replace(";", "")
        description.replace(";", ".")

        self.songs.append((index, link, description))
        with open(self.path, "a") as musicFile:
            musicFile.write(f"{index};{link};{description}")
            musicFile.write("\n")

    def remove(self, indexes):
        pass

    def show(self):
        return self.songs
