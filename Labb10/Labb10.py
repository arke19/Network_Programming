import re

"""
txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
list = re.findall("or", txt) #finds all "or" in text
list_dot = re.findall( "or.", txt) #or then one more letter e.g oro ori
list_all_dot = re.findall( ".", txt) #finds everything
look_for_dot = re.findall("..\.", txt) #finds all dots
find_w = re.findall(r"\w", txt) #find all letters
find_W = re.findall(r"\W", txt) #finds all spaces
find_digit = re.findall(r"\d", txt) #find digit
find_nondigit = re.findall(r"\D", txt) #find nondigit
find_separator = re.findall(r"\s", txt)
find_nonseparator = re.findall(r"\S", txt)
"""
#print(list)
#print(list_dot)
#print(list_all_dot)
#print(look_for_dot)
#print(find_w)
#print(find_W)
#print(find_digit)
#print(find_nondigit)
#print(find_separator)
#print(find_nonseparator)


mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

# (?<!\S) negative lookbehind assertion. to remove jox@jox.com https://docs.python.org/3/library/re.html

#first check that we're at the start of the string. then check for word, then it possible to add additional . + words. 
# then check @ + word . word then additional  . + words  can be added

find_email = re.findall(r'(?<!\S)\w+(?:\.\w+)*@\w+\.\w+(?:\.\w+)*', mtxt)

print(find_email)


f = open("Labb10/tabla.html", encoding="utf-8")
txt = f.read()
simpsons = re.findall(r'<td class=\"svtTablaTime\">\s(\d+\.\d+)\s<\/td>\s<td.*?>\s<h4.*?>\sSimpsons\s<\/h4>\s(?:<div.*?>\s)+<p.*>\s.*Säsong (\d*). Del (\d*) av (\d*).\s(.*)', txt)
for item in simpsons:
    print("-----------------------")
    print("Tid:\t ", item[0])
    print("Säsong:\t ", item[1])
    print("Avsnitt: ", item[2]+"/"+item[3])
    print("Handling: ",item[4])