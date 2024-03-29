<%
current = status["songid"]
%>

<table style="width: 100%">
	<tr>
		<th></th>
		<th>Artist</th>
		<th style="width: 100%">Title</th>
		<th>Length</th>
		<th></th>
	</tr>
<%
for song in mpd.playlistid():
	if not "time" in song:
		song["time"] = 0
	if song["id"] == current:
		req.write("\t<tr style=\"font-weight: bold;\">\n")
		req.write("\t\t<td><img class=\"mini\" src=\"static/selected.svg\" alt=\"Current song\"/></td>\n")
	else:
		req.write("\t<tr>\n\t\t<td></td>\n")
	pass
	artist = song["artist"] if "artist" in song else "Unknown"
	title = song["title"] if "title" in song else "Unknown"
%>
		<td style="white-space:nowrap;"><%=artist%></td>
		<td><%=title%></td>
		<td><%=utils.formatTime(song["time"])%></td>
		<td style="white-space:nowrap;">
			<a href="?action=playid&amp;id=<%=song["id"]%>"><img class="mini" src="static/play.svg" alt="Play song" /></a>
			<a href="?action=remove&amp;id=<%=song["id"]%>"><img class="mini" src="static/remove.svg" alt="Remove song" /></a>
		</td>
	</tr>
<%
pass
%>
</table>
