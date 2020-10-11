import argparse
from player import MusicPlayer

MUSIC_TEXT_FILE = "music.txt"

parser = argparse.ArgumentParser(description="Open a browser window with music")

parser.add_argument("-p", "--play", nargs=None, type=int, help="Play a song")
parser.add_argument(
    "-r",
    "--remove",
    nargs="+",
    metavar="N",
    type=int,
    help="Remove song from music list",
)
parser.add_argument(
    "-a", "--add", nargs=2, metavar=("LINK", "DESCRIPTION"), help="Add new music"
)
parser.add_argument("-l", "--list", action="store_true", help="Show music list")

args = parser.parse_args()

songs = MusicPlayer(MUSIC_TEXT_FILE)

if args.play:
    songs.play(args.play)
elif args.remove:
    songs.remove(args.remove)
elif args.add:
    link, description = args.add
    songs.store(link, description)
    pass
elif args.list:
    songs.show()
else:
    random = 0
    songs.play(random)
