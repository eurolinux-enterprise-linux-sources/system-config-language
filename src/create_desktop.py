#!/usr/bin/python

import os
import string

files = os.listdir('.')
desktop = ""
name_translations = []
comment_translations = []

for file in files:
    if file[-8:] == ".desktop":
        print "Processing %s" % file
        desktop = file

fd = open(desktop, 'r')
desktop_lines = fd.readlines()
fd.close()

name = ""

for line in desktop_lines:
    if line[:5] == "Name=":
        tag, name = string.split(line, "=")

    if line[:8] == "Comment=":
        tag, comment = string.split(line, "=")

name = string.strip(name)
print "Name is %s" % name

comment = string.strip(comment)
print "Comment is %s" % comment

files = os.listdir('po/')
print "Searching through po files"

for file in files:
    if file [-3:] == ".po":
        fd = open("po/%s" % file, 'r')
        lines = fd.readlines()
        fd.close()

        for line in lines:
            tmp = string.strip(line)

            if tmp == ('msgid "%s"') % name:
                substring = lines[lines.index(line) + 1]
                tag, translation, eol = string.split(substring, '"')
                locale = file[:-3]
                            
                name_translations.append("Name[%s]=%s" % (locale, translation))

            if tmp == ('msgid "%s"') % comment:
                substring = lines[lines.index(line) + 1]
                tag, translation, eol = string.split(substring, '"')
                locale = file[:-3]
                            
                comment_translations.append("Comment[%s]=%s" % (locale, translation))


fd = open('foobar.desktop', 'w')

for line in desktop_lines:
    if line[:5] == "Name=":
        fd.write(line)
        
        for item in name_translations:
            print item
            fd.write(item + "\n")

    elif line[:8] == "Comment=":
        fd.write(line)
        for item in comment_translations:
           print item
           fd.write(item + "\n")

    else:
        fd.write(line)

fd.close()
