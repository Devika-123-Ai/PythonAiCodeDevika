#string methods()
#.upper() / .lower() / .title() / .capitalize()

text='hi devika'
print(text.upper())
print(text.lower())
print(text.title())                    #first letter of each word makes capital letter
print(text.capitalize())             #it makes first character uppercase 

#.strip() / .lstrip() / .rstrip() Remove whitespace or specified characters from the ends.
text = "  Python @@ " 
print(text.strip("@"))
print(text.strip())
text = "  Python @@" 
print(text.strip("@"))

#.split() / .rsplit() / .splitlines() ***Split text into a list.
text='rama,devika'
print(text.split("."))