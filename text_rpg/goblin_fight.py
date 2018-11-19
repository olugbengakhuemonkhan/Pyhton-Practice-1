# Scope = global (all the way left(anyone can see))
       # Local (tabbed(only those inside))
# this is a procedural approach to a text based rpg game
# The hero is fighting the goblin
# The hero has the option to:
# 1. Fight
# 2. Dance
# 3. Flee

# Get hero name from the player
hero_name = raw_input("What is thy name, brave adventure? ")

def fight():
   # declare some variables
   # These variables are only accessible in the function scope
   hero_health = 10
   hero_power = 5
   goblin_health = 6
   goblin_power = 2

   # run the game as long as BOTH characters have health > 0
   while hero_health > 0 and goblin_health > 0:
       print """You have %d health and %d power.
       The goblin has %d health and %d power.
       What do you want to do?
       1. fight goblin
       2. do a little dance
       3. flee
       > """ % (hero_health, hero_power, goblin_health, goblin_power)
    
       user_input = raw_input("")

       if user_input == "1":
       #     The hero has decided to attack!
       #     subtract goblins health by hero power
           goblin_health -= hero_power
           print "You have done %d damage to the goblin!" % hero_power
       elif user_input == "2":
           hero_health += 10
           print """The goblin stares at you in disbelief of your stupidity.
           His jaw drops as your wounds heal."""
           print "Your health is now %d" % hero_health
       elif user_input == "3":
           print "Goodbye, cowardly %s" % hero_name
           # the break statement will end the loop IMMEDIATELY!!
           break
       else:
           print "Thou fool. Thou hast stumbledith (invalid input)"

# ANYTIME you have ()
fight()