from lxml import etree


# locations are [left, top, right, bottom]
BLKW =  ['BILL OF LADING', 'B/L NUMBER']
BLLoc = [0,0,0,0]

inf = 'test_nice.xml'
doc = etree.parse(inf)



for elt in doc.getiterator('textbox'):
    box_s = ''
    
    for tlelt in elt.iterchildren('textline'):
        # get the words in this line and check if it's a keyword
        line_s = ''
        for tbelt in tlelt.iterchildren('text'):
            line_s = line_s + tbelt.text

        for KW in BLKW:
            if KW in line_s.upper():
               #Save the location because we need to find the corresponding value
               print ('found BLKW ' + line_s)
               BLLoc = tlelt.get('bbox').split(',')
               print (BLLoc)
               break
    #if 
    #bbox = elt.get('bbox')


    #print box_s



 
