def formatTime(time):
    time = int(time)
    seconds = time % 60;
    minutes = time / 60;
    return "%d:%02d" % ( minutes, seconds )

def formatTrack(track):
	if "artist" in track and "title" in track:
		return track["artist"] + " - " + track["title"]
	elif "file" in track:
		return track["file"]
	else:
		return str(track)