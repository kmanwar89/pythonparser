Psuedocode:

* Ask the user for a filename of the XML file, include input validation for non-valid entry (can't be blank)
* assign the filename the user enters to a variable
* pass that variable to the file() function and load it with read permissions
* once read into memory, strip the first three lines from the file
* ask the user how many lines they'd like to read
  * assign this value to a variable that controls the loop
* enter the loop:
  * for (the number of lines the user wants):
    * read each value, delimited on whitespace
    * assign each value to a variable
    * output each variable to a neatly-formatted list
* close the file
