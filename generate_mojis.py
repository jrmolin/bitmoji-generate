#!/usr/bin/env python

import json

id = "YOUR ID HERE"

BITMOJI_FILE="bitmoji.json"

obj = {}

with open(BITMOJI_FILE, 'r') as f:
    obj = json.load(f)

out = open("me.html", "wb")

imojis = obj["imoji"]

s = """
<style> body * { margin: 0; padding: 0; display: inline-block; } li { display: block; } .friends { width: 300px; } </style>
"""
img = """
<div class="friends"><img src="{url}&width=300" /><ul>
</ul></div>
"""
tag = "<li>%s</li>"
mymojis = []
out.write("<style> body * { margin: 0; padding: 0; display: inline-block; } li { display: block; } .friends { width: 300px; } </style>\n")
for moji in imojis:
    src = moji['src'] % id
    out.write("""<div class="friends"><img src="%s&width=300" /><ul>\n""" % src)
    tags = moji.get('tags', []) + moji.get('categories', []) + moji.get('supertags', [])
    for t in tags:
        out.write("<li>%s</li>\n" % t.encode('utf-8'))

    out.write("</ul></div>\n")

out.close()
