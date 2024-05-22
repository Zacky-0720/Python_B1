import sys
args=sys.argv
from introduce import family


outtext=family(args[1],args[2],args[3])


print(outtext.name_out())
print(outtext.age_out())
print(outtext.cat_out())