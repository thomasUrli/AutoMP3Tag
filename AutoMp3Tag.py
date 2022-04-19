import getpass
import os
from mutagen.id3 import ID3NoHeaderError, ID3, APIC, TIT2, TPE1, TALB
from tkinter import Tk
from tkinter import filedialog

osuser = getpass.getuser()
imgsize = "512"


def modify_tag(filepath):
    name = os.path.split(filepath)[1]
    name = name.partition(' - ')
    name = list(name)
    del name[1]
    artist = name[0]
    title = os.path.splitext(name[1])[0]
    downdir = os.path.split(filepath)[0]

    print("Modifying Tag of "+filepath)

    try:
        file = ID3(filepath)
        tags=True

    except ID3NoHeaderError:
        file = ID3()
        tags=False

    # try:
    #     if tags:
    #         if str(file["APIC:"].data).__contains__("b"):
    #             pass
    #
    #     else:
    #         raise ValueError
    #
    # except (KeyError, TypeError, ValueError):
    #     try:
    #         print("\nDownloading cover art...")
    #         os.system("sacad " + "\"" + str(
    #             artist) + "\"" + " \"" + title + "\"" + " \"" + imgsize + "\"" + " \"" + os.path.join(downdir, "cover.jpg") + "\"" + " -d")
    #
    #         with open(os.path.join(downdir, "cover.jpg"), 'rb') as img:
    #             image_data = img.read()
    #             print("Applying cover art...")
    #             file.add(APIC(encoding=0, mime="image/jpeg", type=0, desc="", data=image_data))
    #             os.remove(os.path.join(downdir, "cover.jpg"))
    #
    #     except (FileNotFoundError, Exception):
    #         pass

    try:
        if file["TIT2"] == title:
            pass

        else:
            file["TIT2"] = TIT2(encoding=3, text=title)

    except KeyError:
        file["TIT2"] = TIT2(encoding=3, text=title)

    try:
        if file["TPE1"] == artist:
            pass

        else:
            file["TPE1"] = TPE1(encoding=3, text=artist)

    except KeyError:
            file["TPE1"] = TPE1(encoding=3, text=artist)

    file["TALB"] = TALB(encoding=3, text="")

    file.save(filepath, v2_version=3)

    print("Done!")


if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    root.update()
    files = filedialog.askopenfilenames(title="Choose a file", filetypes=(('MP3 File', '*.mp3'),('All files', '*.*')))
    list(files)

    for file in files:
        modify_tag(str(file))

