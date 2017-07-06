import os
from shlex import quote

dosyalar = os.listdir()
videolar, sesler, videoSes = [], [], []


for i in dosyalar:
    if i[-4:] == ".mp4":
        videolar.append(i)

    elif i[-4:] == ".m4a":
        sesler.append(i)

for i in videolar:
    for j in sesler:
        if i[:-4] == j[:-4]:
           videoSes.append((i,j)) 

for i, j in videoSes:
    komut = "sudo ffmpeg -i {} -i {} -c:v copy -c:a copy out/{}".format(quote(i), quote(j), quote(i))
    os.system(komut)
    print("[MERGED]",i)
