Psuedocode:

* Get input from user of an XML file (filename-agnostic), need input validation here
* Load the file into memory (read or readline?), strip the first three header lines
* Ask the user how many messages to read?
* Using a loop:
  * Read each column, delimited on whitespace or "" marks
  * Assign each column value to a variable (name, date, type, duration, etc)
  * Once the entire file is looped through and read, close the file.
* Print the output in a nice format, using a GUI of some kind?
