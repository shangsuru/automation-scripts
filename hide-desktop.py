import os
import shutil


desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
hidden = "/Users/henryhelm/Documents/.hidden"

desktopFiles = os.listdir(desktop)
if desktopFiles == ["Google Drive"]:
    # copy all files from hidden to desktop
    for f in os.listdir(hidden):
        shutil.move(hidden + "/" + f, desktop)
else:
    # copy all files from desktop to hidden
    for f in desktopFiles:
        if f != "Google Drive":
            shutil.move(desktop + "/" + f, hidden)
