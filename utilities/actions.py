import sys, os, threading

mpd = None
session = None

def performAction(action, argv):
	if globals().has_key(action):
		method = globals()[action]
		return method(argv)

def volumeup(argv):
	mpd.setvol(int(mpd.status()["volume"]) + 5)

def volumedown(argv):
	mpd.setvol(int(mpd.status()["volume"]) - 5)

def play(argv):
	mpd.pause(0)
def pause(argv):
	mpd.pause(1)
def playid(argv):
	mpd.playid(argv["id"])
def remove(argv):
	try:
		mpd.deleteid(argv["id"])
	except Exception:
		pass

def next(argv):
	mpd.next()
def previous(argv):
	mpd.previous()

def add(argv):
	try:
		mpd.add(argv["file"])
	except Exception:
		pass

def shutdown(argv):
	session["shutdown-requested"] = True	
def shutdown_confirmed(argv):
	session["shutdown-confirmed"] = True
	t = threading.Timer(5, os.system, ["sudo shutdown -h now"])
	t.start()

def toggle_consume(argv):
	mpd.consume(1 - int(mpd.status()["consume"]))
def toggle_repeat(argv):
	mpd.repeat(1 - int(mpd.status()["repeat"]))
def toggle_random(argv):
	mpd.random(1 - int(mpd.status()["random"]))
