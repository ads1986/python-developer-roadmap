#Font: https://www.w3schools.com/python/python_regex.asp

print("#Regex")

import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")