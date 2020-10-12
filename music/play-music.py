import argparse
from player import MusicPlayer

"""
Text file where all songs are stored in the format
"[index];[link];[description]"
"""
MUSIC_FILE = "./music.txt"


# ==============================
# Define command line arguments
# ==============================

parser = argparse.ArgumentParser(
    description="Open a browser window and listen to music"
)
parser.add_argument("-p", "--play", nargs=None, type=int, help="Play a song")
parser.add_argument(
    "-r",
    "--remove",
    nargs="+",
    metavar="N",
    type=int,
    help="Remove song from music collection",
)
parser.add_argument(
    "-a",
    "--add",
    nargs=2,
    metavar=("LINK", "DESCRIPTION"),
    help="Add new song to collection",
)
parser.add_argument("-l", "--list", action="store_true", help="Show music collection")


# =============================
# Execute command
# =============================

args = parser.parse_args()
songs = MusicPlayer(MUSIC_FILE)

if args.play:
    songs.play(args.play)

elif args.remove:
    songs.remove(args.remove)

elif args.add:
    link, description = args.add
    songs.store(link, description)

elif args.list:
    songs = songs.show()
    for song in songs:
        index, link, description = song
        print(f"[{index}] {link} - {description}")

else:
    songs.play()
