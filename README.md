simpleMPD
=========

This is a very simple mpd web client. 

Requirements
------------
simpleMPD is written to work with mod_python within apache2.
It obviously needs a running mpd.
No further services, like mysql and alike, are needed.

What you can expect
-------------------
* small codebase (less than 800 lines, more than 450 lines of those within mpd.py).
* simple and easily extendable web interface that features
	* viewing current status (current song, volume, status flags)
	* changing volume and status flags
	* viewing and editing current playlist, playing songs from the playlist
	* browsing and searching database
	* adding files and folders to the current playlist
* simple, standard compliant interface: no javascript, flash and alike, but proper html5 and css

What you should not expect
--------------------------
* clean code
* any kind of layer separation (MVC)
* Security
* fancy interface (no javascript, no flash, ...)
