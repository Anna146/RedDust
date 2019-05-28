#!/usr/bin/env python

import sys

current_author = None
current_prof = "-1"
current_texts = []
current_count = 1

for line in sys.stdin:
    line = line.strip()

    if len(line.split('\t')) != 2:
        continue

    try:
        author, stuff = line.split('\t')
        prof, txt = stuff.split("___")
    except:
        continue

    if current_author == author:
        if current_count <= 102:
            current_texts.append(txt)
            current_count += 1
            if prof != "-1":
                if current_prof != "-1" and current_prof != prof: # if we have found the other predicate value before we don't want the user
                    current_prof = "-2"
                else:
                    current_prof = prof
    else:
        if current_count > 20 and current_count <= 100 and current_prof != "-1" and current_prof != "-2":
            for txt in current_texts[:100]:
                print(u'%s\t%s\t%s' % (current_author, current_prof, txt))
        current_author = author
        current_prof = prof
        current_count = 1
        current_texts = [txt]