import sys
from introfamily import IntroFam
args = sys.argv

introFam = IntroFam(args[1], args[2], args[3]) 
a=introFam.name_out()
b=introFam.age_out()
c=introFam.cat_out()

print(a)
print(b)
print(c)
        
