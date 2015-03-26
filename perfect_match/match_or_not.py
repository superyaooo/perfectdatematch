"""
search for same words in two different strings.
"""


def match_or_not(a, b):
      
    c = []
    
    for i in a:
        if i in b:
            c.append(i)       # puts words in common from a and b into c.
                       
    if len(c) == 0:        # runs after running the for-loop.
        print "Nothing in common. No match."
    else:
        print "The clients have something in common!"
        print c
        print "Arrange a date!"




