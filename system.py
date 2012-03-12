<div class="syscontrols">
reload <a href="?"><img class="icon" src="static/reload.svg" alt="Reload" /></a><br />
shutdown <a href="?action=shutdown"><img class="icon" src="static/shutdown.svg" alt="Shutdown" /></a>
</div>

<%
if "shutdown-requested" in session:
	del session["shutdown-requested"]
%>
<div class="bottombox">
	<img class="icon" src="static/warning.svg" alt="Warning!" />You have requested a system shutdown!<br />
	<a href="?action=shutdown_confirmed"><img class="icon" src="static/yes.svg" alt="Yes" />Yes, perform shutdown.</a>
	<a href="?"><img class="icon" src="static/no.svg" alt="No" />No, abort shutdown.</a>
</div>
<%
elif "shutdown-confirmed" in session:
%>
This system is going down for shutdown in 5 seconds...
<%
pass
%>
