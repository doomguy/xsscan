# xsscan
A simple script to detect unescaped characters in a web application for e.g. Cross Site Scripting (XSS) attacks.

Only GET requests are supported at the moment.

## Usage
To scan for a single character just use something like this:

```
$ ./xsscan.py lib/less_than.lst "http://example.com/page.php?param=" | uniq -c
      2 <|<
      2 <|%3c
      2 <|%3C 
```
The format is as follows: number of found insertion points, the searched for character, the used payload.

To scan for all special characters use the bash script `xsscan_all.sh`:

```
$ ./xsscan_all.sh 'example.com/search?q='
[*] Scanning: example.com/search?q=
      2 &|&
      1 &|%26
      2 @|@
      2 @|%40
      2 :|:
      2 :|%3a
      2 :|%3A
      2 $|$
      2 $|%24
      1 "|"
      1 "|%22
      5 =|=
      2 !|!
      2 !|%21
      2 `|`
      2 `|%60
      7 -|-
      7 -|%2d
      7 -|%2D
      2 %|%
      2 %|%25
      7 .|.
      7 .|%2e
      7 .|%2E
      5 +|+
      2 +|%2b
      2 +|%2B
      7 ?|?
      2 ?|%3f
      2 ?|%3F
      2 ;|;
      2 ;|%3b
      2 ;|%3B
      2 '|'
      2 '|%27
      7 /|/
      2 /|%2f
      2 /|%2F
[*] All done. Exiting..
```
