import os
import shutil


desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
hidden = "/Users/henryhelm/Documents/.hidden"

desktopFiles = os.listdir(desktop)

if len(desktopFiles) == 1:
    hiddenFiles = os.listdir(hidden)
    for f in hiddenFiles:
        shutil.move(hidden + "/" + f, desktop)
else:
    for f in desktopFiles:
        if f != "Google Drive":
            shutil.move(desktop + "/" + f, hidden)
