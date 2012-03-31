<%
current = mpd.currentsong()
playAction = ("play", "pause")[status["state"] == "play"]

#req.write(str(mpd.playlistid(status["nextsong"])))

if "time" in status:
	(elapsed, time) = status["time"].split(":")
else:
	(elapsed, time) = (0, 0)
%>
<div class="volume">
	<a href="?action=volumeup"><img class="icon" src="static/volumeup.svg" alt="Volume up" /></a><br />
	<%=str(status["volume"])%> %<br />
	<a href="?action=volumedown"><img class="icon" src="static/volumedown.svg" alt="Volume down" /></a><br />
</div>

<div class="current">
	<%=utils.formatTrack(current)%>
	<%=utils.formatTime(elapsed)%> / <%=utils.formatTime(time)%>
<%
if status["state"] == "pause":
	req.write("(paused)")
pass
%>
</div>

<div class="controls">
	<a href="?action=previous"><img class="icon" src="static/previous.svg" alt="Previous song" /></a>
	<a href="?action=<%=playAction%>"><img class="icon" src="static/<%=playAction%>.svg" alt="<%=playAction.capitalize()%> song" /></a>
	<a href="?action=next"><img class="icon" src="static/next.svg" alt="Next song" /></a>
<%
for flag in ["consume", "repeat", "random"]:
	state = "enabled" if status[flag] == "1" else "disabled"
%>
	<a href="?action=toggle_<%=flag%>"><img class="icon" src="static/<%=flag%>-<%=state%>.png" alt="<%=flag.capitalize()%> mode" /></a>
<%
pass
%>
</div>

<div class="bottombox">
next:
<%
try:
	req.write(utils.formatTrack(mpd.playlistid(status["nextsong"])[0]))
except Exception:
	req.write("not available")
pass
%>
</div>