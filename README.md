# pythonparser

## Purpose
I recently backed up my call logs and SMS messages on my Samsung Galaxy S6
smartphone using a great app called 'SMS Backup & Restore', made by Carbonite
(the same company that offers unlimited off-site backups, though I haven't
quite looked into their service that much).  Once the 35,000+ SMS's were backed
up, they were dumped into a nicely-formatted .XML file, which my computer
crashes attempting to open (the file is a whopping 480MB in size!).

This led to my thinking about a better solution -- I don't want to/can't
read through that many lines in an XML file. Why not code something in a language that I'm comfortable with (Python) to read the file, parse the data and output it in a nice, human-readable format that'll allow me to search and better organize the data?

So with that, comes this project.  I aim to make use of existing Python libraries and API's that are designed to interface with XML (why re-invent the wheel?) and write a simple parser.  I will eventually implement a GUI, or pose it as a nice semester project for a student in ISAT 252 to take on, but for the time being I just want a way to reference old text messages or phone calls in an easy way.

I aim to handle both call logs and SMS backups in this program, which will require a little bit of modification to my original idea but nothing too terible.

I'm rusty in my Python and haven't ever created a program from scratch to solve a problem, so we'll see how this goes...
