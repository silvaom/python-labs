#!/usr/bin/python
#searches for patterns that are written in re_string
#not using compile objects
#if you want to use compile objects \
# change it to re_obj = re.compile("{{(.*?)}}")
# and re_obj.findall(some_string):


import re 
re_string = "{{(.*?)}}"

some_string = "this is a string with {{words}} embedded in\
    {{curly brackets}} to show an {{example}} of {{regular expressions}}"

for match in re.findall(re_string, some_string):
    print ("MATCH -> " , match)
