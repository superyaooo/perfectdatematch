import sys
sys.path.append("C:\Users\Yao\projects\Perfect_Date_Match")  # puts module info in the path
from perfect_match import gender
from perfect_match import match_or_not


class ClientInfo(object):
    
    def gender_info(self):

        sex = {}

        print "What's the gender of the client, F or M?"
        sex['gender'] = raw_input("> ").upper()
    
        print "What gender is the client looking for, F or M?"
        sex['want'] = raw_input("> ").upper()

        return sex    # must have to return value of the sex{} dictionary

        

    def other_info(self):

        basic_info = []

        print "What sports does the client like?"
        sports = raw_input("(use comma to seperate)> ").upper().split(',')

        print "What's the client's favorite TV show?"
        tv = raw_input("(use comma to seperate)> ").upper().split(',')

        print "What food does the client like? (e.g. Chinese food, Italian food, etc.)"
        food = raw_input("(use comma to seperate)> ").upper().split(',')

        print "What other interests does the client have?"
        interest = raw_input("(use comma to seperate)> ").upper().split(',')
        
        basic_info = sports + tv + food + interest
        return basic_info  # must have to return value of the basic_info[] list
        

print """
-------------------------------------
data from client A
-------------------------------------
"""
client_a = ClientInfo()
gender1 = client_a.gender_info()


print """
-------------------------------------
data from client B
-------------------------------------
"""
client_b = ClientInfo()
gender2 = client_b.gender_info()

gender.gender_match(gender1, gender2)  #runs module


print """
-------------------------------------
more data from client A
-------------------------------------
"""
info1 = client_a.other_info()


print """
-------------------------------------
more data from client B
-------------------------------------
"""
info2 = client_b.other_info()

match_or_not.match_or_not(info1, info2)




    









    
