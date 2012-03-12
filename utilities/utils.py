def formatTime(time):
    time = int(time)
    seconds = time % 60;
    minutes = time / 60;
    return "%d:%02d" % ( minutes, seconds )

def formatTrack(track):
	return track["artist"] + " - " + track["title"]