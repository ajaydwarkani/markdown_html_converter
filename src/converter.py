import re

pattern = re.compile('([#*]+\s|\w*\[\w*\]\(\w*\))')

md_html_mapping = {}
md_html_mapping["## "] = "<h2>"
html_closing_tags = {}
html_closing_tags["<h2>"] = "</h2>"

html_doc = open("converted.html", "a")
filename = "test.md"
tags = []
with open(filename) as f:
    content = f.readlines()
    for line in content:
        match = pattern.findall(line)
        print line
        print match
        if match:
            for phrase in match:
                # link
                print phrase
                if phrase[0] == "[":
                    phrase_split = phrase.split("]")
                    text_link = phrase_split[0][1:]
                    url_link = phrase_split[1][1:-1]
                    link_html = "<a href=" + url_link + ">" + text_link + "</a>\n"
                    html_doc.write(link_html)
                # bullet list
                if phrase[0] == "*":
                    
                    bullet_html = "<ul>\n\t <li>" + phrase[0][1:] + "</li>\n</ul>\n"
                    html_doc.write(bullet_html)
                # list
                #elif phrase[0] == "*":
                 #   bullet_text = phrase.split()
                    




    #print content
    """ for sentence in content:
        words = sentence.split()
        print words
        print sentence
        if words[0] in md_html_mapping:
            #print md_html_mapping[words[0]] + sentence + html_closing_tags[md_html_mapping[words[0]]]
            html_doc.write(md_html_mapping[words[0]] + ''.join(words[1:]) + html_closing_tags[md_html_mapping[words[0]]] + "\n") """
  
""" 
#[**](**)
pattern = re.compile('([#*]+\s|\w*\[\w*\]\(\w*\))')
m = pattern.match("* lol [lol](lol)")
print p.findall("* lol [lol](lol)") """