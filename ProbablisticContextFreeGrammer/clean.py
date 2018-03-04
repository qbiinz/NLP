"""
This script removes numbers from the generated senteces using cfggen.pl
"""
import re

rem = re.compile("(\d*:\s+)(.*$)")
clean = []
with open('output.sen', 'r') as output:
    for line in output:
        found = rem.match(line)
        clean.append(found.group(2))

with open('output.sen','w') as output:
    for line in clean:
        output.write(line + '\n')

        