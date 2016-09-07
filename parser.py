# Purpose: Parse an XML file created by 'SMS Backup & Restore' Android app and output results to a clean interface.
# Make use of the Python SAX XML API
# Reference: http://www.tutorialspoint.com/python/python_xml_processing.htm
# Programmer: Kadar Anwar
# Language: Python 3.4
# parser.py
# 9/7/2016

# Import XML SAX API package
import xml.sax

class CallHandler( xml.sax.ContentHandler ):
    # Initialize the class
    def __init__(self):
        self.Number = ""
        self.Duration = ""
        self.Date = ""
        self.Type = ""

    # Define when an element starts
    def startElement(self, number, duration, type, date):
        self.CurrentData = type
        if type == "1":
            print ("Call: Sent")
        elif type == "2":
            print ("Call: Received")

    # Define when an element ends
    def endElement(self, number, duration, type, date):
        if self.CurrentData == "type":
            print ("Type:", self.Type)
        elif self.CurrentData == "number":
            print ("Number:", self.Number)
        elif self.CurrentData == "duration":
            print ("Call Duration:", self.Duration)
        elif self.ReadableDate == "readable_date":
            print ("Date:", self.Date)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "type":
            self.Type = content
        elif self.CurrentData == "number":
            self.Number = content
        elif self.CurrentData == "duration":
            self.Duration = content
        elif self.Date == "date":
            self.Date = content

# Call the main function from within the class
if ( __name__ == "__main__"):

    # Create an XMLReader Object
    parser = xml.sax.make_parser()

    # Turn off namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # Override the default ContextHandler
    Handler = CallHandler()
    parser.setContentHandler( Handler )

    parser.parse("calls.xml")
