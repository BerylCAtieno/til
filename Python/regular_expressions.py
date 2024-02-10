#Regex module
import re



string = "The quick black fox jumped over the lazy dog."

#defining patterns
pattern = r"regex_pattern"


result = re.match(pattern, string) #matching patterns at the beginning of a string
result = re.search(pattern, string) #finding patterns anywhere in the string
matches = re.findall(pattern, string) #returns a list of all matching patterns

match_iterator = re.finditer(pattern, string) 
"""function returns an iterator that yields 
match objects for all matches of a pattern in the string."""
for match in match_iterator:
    print(match.group())


#Match Objects - contains information about the match, such as the matched string and groups.
match.group()   # Returns the matched string
match.start()   # Returns the start position of the match
match.end()     # Returns the end position of the match
match.span()    # Returns a tuple containing the (start, end) positions




#Metacharacters and Escapes
#character classes and quantifiers
#Anchors and boundaries


