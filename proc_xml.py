#!/usr/bin/env python

import sys
import getopt
import string

from lxml import etree

# info we are trying to find
found_BL = ''




# locations are [left, top, right, bottom]
BLKW =  ['BILL OF LADING', 'B/L NUMBER', 'B/L NO', 'B/L-NO']
BLLoc = [0,0,0,0]

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    # main setup from https://www.artima.com/weblogs/viewpost.jsp?thread=4829
#----
    if (argv == None):
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"
        return 0
#----

    inf = 'test_nice.xml'
    doc = etree.parse(inf)



    for elt in doc.getiterator('textbox'):
        box_s = ''
        
        for tlelt in elt.iterchildren('textline'):
            # get the words in this line and check if it's a keyword
            line_s = ''
            for celt in tlelt.iterchildren('text'):
                line_s = line_s + celt.text
                line_s = line_s.upper()
            for KW in BLKW:
                if KW in line_s:
                    print ('found ' + KW + ' in ' + line_s)
                    #Check if B/L is in the same line
                    line_s = line_s.strip(KW) 
                    line_s = line_s.strip(string.punctuation)
                    line_s = line_s.strip()

                    print ('\n' + line_s)
                    if (len(line_s) > 4):
                        # assume this is the correct B/L
                        # BL should be atleast 4 chars
                        found_BL = line_s
                    else:
                        #Save the location because we need to find the corresponding value
                        BLLoc = tlelt.get('bbox').split(',')
                        print (BLLoc)
                    break
        #if 
        #bbox = elt.get('bbox')


        #print box_s


if __name__ == "__main__":
    sys.exit(main())
 
