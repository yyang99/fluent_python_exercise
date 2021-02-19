import sys
import re
WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            occurences = index.get(word, [])
            occurences.append(location)
            index[word] = occurences

for word in sorted(index, key=str.upper):
    print(word, index[word])
