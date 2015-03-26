""" tests for gender match """

def gender_match(x,y):

    if x['gender'] == y['want'] and x['want'] == y['gender']:
        print "Gender match."
        

    else:
        print "Gender doesn't match."
        print "Try again"
        exit(1)     # exits program


        



