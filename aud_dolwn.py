import pafy

file1 = file1 = open("audio.txt","r+")
links = file1.readlines()

for i in range(77,len(links)):
    print("downloading {} auido".format(i+1))
    video = pafy.new(links[i][:-2])
    audiostreams = video.audiostreams
    k=0
    for j in audiostreams:
        if j.extension=="m4a":
            k=1
            j.download()
            break
    if k==0:
        print("m4a not supported for {}".format(l[i]))

