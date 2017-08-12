#!/usr/bin/python3

# imports
import requests
import sys
import re 

# usage
if len(sys.argv)==1:
  print("\nUsage: "+sys.argv[0]+" lib/mychar.lst http://example.com/page.php?param=\n")
  quit() 

# parse arguments
file=str(sys.argv[1])
url=str(sys.argv[2])

# get character to scan for; defined in first line of char-file
with open(file, 'r') as f:
    char = f.readline().strip()

# start scanning
with open(file,'r') as f:
  for x in f:
    #print ('=== '+url+'XSS'+x.rstrip()+'XSS')
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url+'XSS'+x.rstrip()+'XSS', headers = user_agent)
    
    # parse response; print line if char found
    for line in r.text.splitlines():
      line = line.rstrip()
      if re.search('XSS'+re.escape(char)+'XSS', line, re.IGNORECASE) :
        print ('=== '+url+'XSS'+x.rstrip()+'XSS')
        print (line)
