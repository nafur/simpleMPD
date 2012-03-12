<%

for var in ["directory", "query", "dbmode"]:
	if var in argv:
		session[var] = argv[var]
	elif not var in session:
		session[var] = ""

directory = session["directory"]
query = session["query"]
dbmode = session["dbmode"]

%>
<form>
	<button name="dbmode" value="browse">Browse</button>
	<input type="text" name="query" value="<%=query%>" />
	<button name="dbmode" value="search">Search</button>
</form>

<%
if dbmode == "search":
%>
<table style="width: 100%">
<%
	for item in mpd.search("any",query):
		if "file" in item:
%>
	<tr>
		<td><img src="static/file.png" alt="File" /></td>
		<td width="100%"><a href="?action=add&amp;file=<%=item["file"]%>"><%=os.path.basename(item["file"])%> (<%=utils.formatTime(item["time"])%>)</a></td>
		<td nowrap="nowrap">
			<a href="?action=add&amp;file=<%=item["file"]%>"><img class="mini" src="static/add.svg" alt="Add file" /></a>
		</td>
	</tr>
<%
		elif "directory" in item:
%>
	<tr>
		<td><img src="static/directory.png" alt="Directory" /></td>
		<td width="100%"><a href="?directory=<%=item["directory"]%>"><%=os.path.basename(item["directory"])%></a></td>
		<td nowrap="nowrap">
			<a href="?action=add&amp;file=<%=item["directory"]%>"><img class="mini" src="static/add.svg" alt="Add directory" /></a>
		</td>
	</tr>
</table>

<%
	pass
else:
	# dbmode != "search"
%>
<table style="width: 100%">
	<tr>
		<td></td>
		<td colspan="2">
<%
	parts = directory.split("/")
	for i in range(0, len(parts)):
%>
			<a href="?directory=<%="/".join(parts[0:i+1])%>"><%=parts[i]%></a> /
<%
		pass
%>
		</td>
	</tr>
<%
	for item in mpd.lsinfo(directory):
		if "file" in item:
%>
	<tr>
		<td><img src="static/file.png" alt="File" /></td>
		<td width="100%"><a href="?action=add&amp;file=<%=item["file"]%>"><%=os.path.basename(item["file"])%> (<%=utils.formatTime(item["time"])%>)</a></td>
		<td nowrap="nowrap">
			<a href="?action=add&amp;file=<%=item["file"]%>"><img class="mini" src="static/add.svg" alt="Add file" /></a>
		</td>
	</tr>
<%
			pass
		elif "directory" in item:
%>
	<tr>
		<td><img src="static/directory.png" alt="Directory" /></td>
		<td width="100%"><a href="?directory=<%=item["directory"]%>"><%=os.path.basename(item["directory"])%></a></td>
		<td nowrap="nowrap">
			<a href="?action=add&amp;file=<%=item["directory"]%>"><img class="mini" src="static/add.svg" alt="Add directory" /></a>
		</td>
	</tr>
</table>
<%
			pass
		pass
	pass
pass
%>
