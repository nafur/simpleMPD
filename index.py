<%
req.content_type = "application/xhtml+xml"

# imports
from mod_python import apache, util, Session
import os, time
apache_import = lambda mod: apache.import_module(mod, path=["/var/www/simpleMPD/utilities/"])

mmpd = apache_import("mpd")
mpd = mmpd.MPDClient().connect("localhost", "6600")
utils = apache_import("utils")

actions = apache_import("actions")

# session
if not hasattr(req, "session"):
	session = Session.Session(req)
session.load()

# arguments
argv = util.FieldStorage(req)
actions.mpd = mpd
actions.session = session

action = argv.get("action", "")
actions.performAction(action, argv)

# common stuff
status = mpd.status()

%><!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta charset="utf-8" />
		<title>MPD - simpleMPD</title>
		<link rel="stylesheet" type="text/css" href="static/std.css.py" />
	</head>
	<body>
		<table style="width: 100%">
			<tr>
				<td class="box" style="width: 50%">
					<%@	include file="status.py"%>
				</td>
				<td class="box" colspan="2" style="width: 50%">
					<%@ include file="system.py"%>
				</td>
			</tr>
			<tr>
				<td class="box" colspan="2">
					<%@	include file="playlist.py"%>
				</td>
				<td class="box" style="width: 40%">
					<%@ include file="database.py"%>
				</td>
			</tr>
		</table>
	</body>
</html>
<%
session.save()
%>