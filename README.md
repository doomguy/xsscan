# xsscan
A simple Python 3 script to detect unescaped characters for Cross Site Scripting

## Usage
To scan for a single character just use something like this:

`./xsscan.py lib/less_than.lst "http://example.com/page.php?param="`

To scan for all characters use this bash one-liner:

`for i in $(ls -1 lib/*); do ./xsscan.py $i "http://example.com/page.php?param="; done`
