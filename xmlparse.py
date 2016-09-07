# Purpose: XML Parser for Python, specifically to read text messages and phone
# call records backed up by an Android app
# Programmer: Kadar Anwar
# Language: Python 3.4
# xmlparse.py
# 9/7/2016

# Variables
total = 0.0

# User input
filename = input('Enter the name of the file you want to open:')

# Open the file to parse
infile = open(filename, 'r')

# Read the number of lines in the file
for line in infile:
    

# display the result in human-readable format
print("This file contains", total, "lines in it")

# close the file
file.close()
